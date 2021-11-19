import pandas as pd
from generate_data import get_frequency

db = pd.read_csv('./problem_set.csv')
getrating = db.set_index('problem_id').to_dict()['rating']

verdicts = {'CHALLENGED': (1,10),'COMPILATION_ERROR' : (2,10),'CRASHED' : (5,20),'FAILED': (1,10) , 'IDLENESS_LIMIT_EXCEEDED': (2,20), 'MEMORY_LIMIT_EXCEEDED':(2,50),'PRESENTATION_ERROR':(0,0), 'RUNTIME_ERROR': (5,20), 'SKIPPED': (0,0),'TIME_LIMIT_EXCEEDED': (4,20), 'WRONG_ANSWER' : (5,30), 'TESTING': (0,0), 'OK': (1,-100)}

# this map gives the max attempts to be considered as well as the change in XP it will accomodate

def XP(freq, rating):
    global verdicts
    for key in verdicts.keys() : 
        n,f = verdicts[key]
        rating -= min(n,freq[key])*f
    return rating


def convert_into_df(username):    
    df = pd.DataFrame.from_dict(get_frequency(username)).transpose().reset_index()
    result = []
    for i in range(len(df.iloc[:, 0])):
        d = {}
        d['username'] = username
        d['problem_id'] = df.iat[i, 0]
        if d['problem_id'] not in getrating.keys():
            continue
        # extracting freq map from X[i][problem] and generating the XP and relevant score
        xp = XP(df.iloc[i],getrating[d['problem_id']])
        d['score'] = (xp - getrating[d['problem_id']] + 590)/138.0
        d['XP'] = xp
        result.append(d)
    
    return result


if __name__ == '__main__':
    print(convert_into_df('notSanil'))
