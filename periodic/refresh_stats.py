from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import random
import pandas

import db_handler

def refresh_qpd():
    curr = db_handler.db().get_db()
    curr.execute("""SELECT id, solved, qpd from userdata where solved is not NULL""")
    res = curr.fetchall()
    for row in res:
        qpd = row[2]
        total = sum(qpd)
        new = len(row[1]) - total
        qpd.append(new)
        curr.execute("""UPDATE table userdata set qpd='{0}' where id='{1}'""".format(qpd, row[0]))
        curr.execute('commit')

def refresh_xp():
    curr = db_handler.db().get_db()
    curr.execute("""SELECT id, xp, xp_pd FROM userdata""")
    res = curr.fetchall()

    for row in res:
        xp = row[2]
        xp.append(row[1])
        curr.execute("""UPDATE userdata set xp_pd='{0}' where id='{1}'""".format(xp, row[0]))
        curr.execute("commit")

def refresh_ranks():
    curr = db_handler.db().get_db()
    curr.execute("""SELECT id, rpd FROM userdata ORDER BY xp DESC""")
    res = curr.fetchall()

    for i in range(len(res)):
        ranks = res[i][1]
        ranks.append(i+1)
        curr.execute("""UPDATE userdata set rpd='{0}' where id='{1}'""".format(ranks, res[i][0]))
        curr.execute("commit")

def refresh_problem():
    total = 7361
    ind = random.randint(1, total)
    df = pandas.read_csv("./data/problem_data.csv")
    prob = df.iloc[ind, :]
    link = str(prob[1]) + "/" + str(prob[2])
    with open('problem_day.txt', 'w') as file:
        file.write(link)

def refresh_stats():
    refresh_qpd()
    refresh_xp()
    refresh_ranks()
    refresh_problem()


sched = BackgroundScheduler(daemon=True)
sched.add_job(refresh_stats, 'cron', day='*') # TODO: Change this something more reasonable
sched.start()

atexit.register(lambda: sched.shutdown())
