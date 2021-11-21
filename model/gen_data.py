import pandas as pd

db = pd.read_csv('./data/problem_set.csv')
getrating = db.set_index('problem_id').to_dict()['rating']
db = None

verdicts = {'CHALLENGED': (1,10),'COMPILATION_ERROR' : (2,10),'CRASHED' : (5,20),'FAILED': (1,10) ,
 'IDLENESS_LIMIT_EXCEEDED': (2,20), 'MEMORY_LIMIT_EXCEEDED':(2,50),'PRESENTATION_ERROR':(0,0),
  'RUNTIME_ERROR': (5,20), 'SKIPPED': (0,0),'TIME_LIMIT_EXCEEDED': (4,20), 'WRONG_ANSWER' : (5,30),
   'TESTING': (0,0), 'OK': (1,-100)}

# this map gives the max attempts to be considered as well as the change in XP it will accomodate

def XP(freq, id):
    """
    Gives the XP for questions, given the frequency of user and id of question

    """
    global verdicts

    rating = getrating[id]
    for key in verdicts.keys() : 
        n,f = verdicts[key]
        rating -= min(n,freq[key])*f
    return rating


def convert_into_df(username, solved):
    """
    Converts the solved question data of a user into an appropriate format
    Format req for it to work:
    {
        username problem_id score xp
        Sanil    12345      4.35  900
        .
        .
        .
        .
    }

    """
    df = pd.DataFrame.from_dict(solved).transpose().reset_index()
    result = []
    for i in range(len(df.iloc[:, 0])):
        d = {}
        d['username'] = username
        d['problem_id'] = int(df.iat[i, 0]) # Hack required to ensure that the program doesn't break
        # Basically the json id's are in form of strings, this is needed to convert it into ints
        if d['problem_id'] not in getrating.keys():
            continue
        # extracting freq map from X[i][problem] and generating the XP and relevant score
        xp = XP(df.iloc[i], d['problem_id'])
        d['score'] = (xp - getrating[d['problem_id']] + 590)/138.0
        d['XP'] = xp
        result.append(d)
    return result
