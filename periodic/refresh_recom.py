from apscheduler.schedulers.background import BackgroundScheduler
import psycopg2
import atexit

from model.generate_predictions import recommendations


def get_user_recommendations(username, solved):
    return recommendations(username, 10, solved) 

def refresh_recommendations():
    conn = psycopg2.connect(database='data', user='postgres', password='a', port=5432)
    cursor = conn.cursor()

    _query = """Select id, handle, solved FROM userdata
    """
    insert_query = """UPDATE userdata
                    SET recommended='{1}'
                    WHERE id='{0}'"""

    cursor.execute(query=_query)
    res = cursor.fetchall()
    print("Recommendations refreshed")
    for row in res:
        recoms = get_user_recommendations(row[1], row[2])
        
        cursor.execute(insert_query.format(row[0], recoms))
        cursor.execute("commit")
            

sched = BackgroundScheduler(daemon=True)
sched.add_job(refresh_recommendations, 'interval', seconds=43) # TODO: Change this to something more reasonable
sched.start()


atexit.register(lambda: sched.shutdown())