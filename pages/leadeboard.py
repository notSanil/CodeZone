from user import User
import math

def xp_to_lev(xp):
    level = xp / 100
    level = math.pow(level, 1/3)
    return int(level)


def create_league_leadeboard(userid, db):
    level = User.get_level(userid, db)
    level -= 1 # The default level is 1
    league = level // 5 # Scale level down to value of 0-3

    xp_lower = ((1 + league * 5) ** 3) * 100
    xp_higher = ((5 + league * 5) ** 3) * 100
    query = """SELECT name, xp FROM userdata
            WHERE xp <= {0} AND xp >= {1}
            ORDER BY xp DESC""".format(xp_higher, xp_lower)
    cursor = db.get_db()
    cursor.execute(query)

    res = cursor.fetchall()
    leaderboard = []
    for user in res:
        lev = xp_to_lev(user[1])
        leaderboard.append((user[0], lev))
    return leaderboard
