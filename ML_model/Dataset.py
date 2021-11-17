from csv import writer
import pandas as pd

df = pd.read_csv('shiraz_data.csv')
db = pd.read_csv('problem_set.csv')
getrating = db.set_index('problem_id').to_dict()['rating']

verdicts = {'CHALLENGED': (1,10),'COMPILATION_ERROR' : (2,10),'CRASHED' : (5,20),'FAILED': (1,10) , 'IDLENESS_LIMIT_EXCEEDED': (2,20), 'MEMORY_LIMIT_EXCEEDED':(2,50),'PRESENTATION_ERROR':(0,0), 'RUNTIME_ERROR': (5,20), 'SKIPPED': (0,0),'TIME_LIMIT_EXCEEDED': (4,20), 'WRONG_ANSWER' : (5,30), 'TESTING': (0,0), 'OK': (1,-100)}

# this map gives the max attempts to be considered as well as the change in XP it will accomodate

def XP(freq, rating):
    global verdicts
    for key in verdicts.keys() : 
        n,f = verdicts[key]
        rating -= min(n,freq[key])*f
    return rating

with open('user_data_1.csv', 'a') as f_object:
    for i in range(len(df.iloc[:, 0])):
        d = {}
        d['username'] = 'dhruv_bansal15'
        d['problem_id'] = df.iat[i, 0]
        if d['problem_id'] not in getrating.keys():
            continue
        # extracting freq map from X[i][problem] and generating the XP and relevant score
        xp = XP(df.iloc[i],getrating[d['problem_id']])
        d['score'] = (xp - getrating[d['problem_id']] + 590)/138.0
        d['XP'] = xp
        # Pass this file object to csv.writer() and get a writer object
        writer_object = writer(f_object)
        # Pass the list as an argument into the writerow()
        writer_object.writerow(d.values())
    
    # Close the file object
    f_object.close()

