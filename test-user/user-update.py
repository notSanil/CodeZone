import requests
import json
from apscheduler.schedulers.background import BackgroundScheduler
import time
import psycopg2

dummy = {'question': 41704, 'xp': 10}

def get_user_submission_stats(username):
    url = "https://codeforces.com/api/user.status"
    args = {'handle':username}
    response = requests.get(url, params=args)
    if not response.status_code == 200:
        return None

    result = json.loads(response.content.decode())
    data = result['result']
    response = None
    result = None # Clear heavy variables

    user_statistics = dict()
    for question in data:
        id = question['problem']['contestId'] * 26 + ord(question['problem']['index'][0]) - 65
        if id not in user_statistics:
            user_statistics[id] = {'correct':0, 'incorrect':0}
        if question['verdict'] == 'OK':
            user_statistics[id]['correct'] += 1
        else:
            user_statistics[id]['incorrect'] += 1
    
    return user_statistics

def refresh_hourly():
    conn = psycopg2.connect(database='data', user='postgres', password='a', port=5432)
    cursor = conn.cursor()


    _query = """Select id, name, handle FROM userdata
    """
    cursor.execute(query=_query)
    res = cursor.fetchall()
    for row in res:
        stats = get_user_submission_stats(row[2])
        if stats is not None:
            if dummy['question'] in stats:
                if stats[dummy['question']]['correct'] >= 1:
                    print('xp awarded')

sched = BackgroundScheduler(daemon=True)
sched.add_job(refresh_hourly, 'interval', seconds=10)
sched.start()

if __name__ == '__main__':
    while True:
        time.sleep(1)