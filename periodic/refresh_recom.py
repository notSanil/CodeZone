from apscheduler.schedulers.background import BackgroundScheduler
import psycopg2
import atexit

from model.generate_predictions import recommendations
import db_handler


def get_user_recommendations(username, solved):
    return recommendations(username, 10, solved) 

def refresh_recommendations():
    
    cursor = db_handler.db().get_db()

    _query = """Select id, handle, solved, recommended FROM userdata WHERE handle IS NOT NULL AND solved IS NOT NULL
    """
    insert_query = """UPDATE userdata
                    SET recommended='{1}'
                    WHERE id='{0}'"""

    cursor.execute(query=_query)
    res = cursor.fetchall()
    print("Recommendations refreshed")
    for row in res:
        if len(row[3]) > 6:
            continue
        if not len(row[2]):
            recoms = [95640, 96120, 95580, 50040, 94920, 94744, 93600, 93060, 92520, 92220]
        else:
            recoms = get_user_recommendations(row[1], row[2])
        
        cursor.execute(insert_query.format(row[0], recoms))
        cursor.execute("commit")
            

sched = BackgroundScheduler(daemon=True)
sched.add_job(refresh_recommendations, 'interval', minutes=1) # TODO: Change this to something more reasonable
sched.start()


atexit.register(lambda: sched.shutdown())