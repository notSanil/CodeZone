import requests
import json
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

import psycopg2
import pandas

from model.gen_data import XP
import db_handler


def get_user_submission_stats(username):
    url = "https://codeforces.com/api/user.status"
    args = {'handle':username}
    response = requests.get(url, params=args)
    if not response.status_code == 200:
        return None

    result = json.loads(response.content.decode())
    result = result['result']
    response = None# Clear heavy variables

    questions = {}
    for row in result:
        qId = row['contestId'] * 60
        if len(row['problem']['index']) == 2:
            offset = 2 * ord(row['problem']['index'][0]) + (bool)(row['problem']['index'][1] == '2') - 130
        else:
            offset = 2*(ord(row['problem']['index']) - 65)
        qId += offset

        if qId not in questions:
            questions[qId] = {'OK': 0, 'WRONG_ANSWER': 0, 'TIME_LIMIT_EXCEEDED': 0, 
            'COMPILATION_ERROR': 0, 'RUNTIME_ERROR': 0, 'IDLENESS_LIMIT_EXCEEDED': 0, 'MEMORY_LIMIT_EXCEEDED': 0,
            'SKIPPED': 0, 'TESTING': 0, 'PRESENTATION_ERROR': 0, 'FAILED': 0, 'CRASHED': 0,
            'CHALLENGED': 0}
        
        questions[qId][row['verdict']] += 1
    
    return questions

def refresh():
    print("Data refreshed")
    
    cursor = db_handler.db().get_db()

    ratings = pandas.read_csv('data\problem_set.csv')
    ratings = ratings.set_index('problem_id').to_dict()['rating']
    _query = """Select id, handle, recommended, xp, qpd FROM userdata
    """
    insert_query = """UPDATE userdata
                    SET solved='{1}', recommended='{2}', xp={3}, qpd='{4}'
                    WHERE id='{0}'"""

    cursor.execute(query=_query)
    res = cursor.fetchall()
    for row in res:
        stats: dict = get_user_submission_stats(row[1])
        if stats is None:
            continue
        awarded = 0
        recom = set(row[2])
        for qId in stats:
            if qId in recom and stats[qId]['OK'] > 0:
                recom.remove(qId)
                awarded += XP(stats[qId], int(qId))
        qpd = row[4]
        if len(qpd) == 0:
            qpd = [len(stats)]
        
        cursor.execute(insert_query.format(row[0], json.dumps(stats), list(recom), awarded+row[3], qpd))
        cursor.execute("commit")
            

sched = BackgroundScheduler(daemon=True)
sched.add_job(refresh, 'interval', seconds=30) # TODO: Change this something more reasonable
sched.start()

atexit.register(lambda: sched.shutdown())