import csv
import os


question_dat = {}
with open(os.path.join(os.path.curdir, 'data/problem_data.csv'), 'r', encoding='utf-8') as file:
    rd = csv.reader(file)
    for row in rd:
        question_dat[int(row[0])] = tuple(row[1:])

def get_recommendations(userID, db):
    cursor = db.get_db()
    query = """SELECT recommended FROM userdata
            WHERE id = '{}'""".format(userID)
    cursor.execute(query)

    res = cursor.fetchone()[0]
    output = []
    for qID in res:
        link = str(question_dat[qID][0]) + '/' + str(question_dat[qID][1])
        output.append((question_dat[qID][2], link))

    return output

    