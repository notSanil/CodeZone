import requests
import json
import csv


url = "https://codeforces.com/api/user.status"
args = {'handle': 'dhruv_bansal15'}
data = requests.get(url, params=args).content
result = json.loads(data.decode())
data = None # Clear heavy data
result = result['result']

questions = dict()

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
    

with open("/Users/uttammittal02/Desktop/CodeZone/shiraz_data.csv", 'w', newline='') as file:
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow(['ID', 'OK', 'WRONG_ANSWER', 'TIME_LIMIT_EXCEEDED', 
        'COMPILATION_ERROR', 'RUNTIME_ERROR', 'IDLENESS_LIMIT_EXCEEDED', 'MEMORY_LIMIT_EXCEEDED',
        'SKIPPED', 'TESTING', 'PRESENTATION_ERROR', 'FAILED', 'CRASHED',
        'CHALLENGED'])

    for questionId in questions:
        qDat = [questionId, ]
        qDat.extend(list(questions[questionId].values()))
        print(qDat)
        csv_writer.writerow(qDat)
