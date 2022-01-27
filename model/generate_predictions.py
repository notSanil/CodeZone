from collections import defaultdict
from operator import itemgetter
import pandas as pd


def recommendations(k, questions):
    """
    Takes the solved problems, and gives k recommendations
    """
    max_ = max(questions.values())
    questions = list(questions.items())
    
    db = pd.read_csv('./raw_to_inner.csv')
    
    a = db.set_index('1').T.to_dict('index')
    b = db.set_index('0').T.to_dict('index')
    # Storing two dicts to map raw_id to inner_id and inner to raw
    raw_to_inner_iid = b[list(b.keys())[0]]
    inner_to_raw = a[list(a.keys())[0]]
    
    
    df = pd.read_csv('./data/trained_data.csv')
    simsMatrix = df.values.tolist()     #loading the similarity matrix obtained by training model

    
    threshold = min(max_, 4.4)
    # Get similar items to stuff we liked (weighted by score)
    candidates = defaultdict(float)
    for itemID, rating in questions:
        if rating < threshold:
            continue
        similarityRow = simsMatrix[raw_to_inner_iid[itemID]]
        for innerID, score in enumerate(similarityRow):
            candidates[innerID] += score * (rating / 5.0)
    
    # Build a dictionary of stuff the user has already seen
    solved = {}
    for itemID, rating in questions:
        solved[raw_to_inner_iid[itemID]] = 1

    # Get top-rated items from similar users:
    pos = 0
    output = []
    for itemID, sum in sorted(candidates.items(), key=itemgetter(1), reverse=True):
        
        if not itemID in solved:
            problemID = inner_to_raw[itemID]
            problemID = int(problemID)
            output.append(problemID)
            pos += 1
            if (pos > k):
                break

    return output
# print(recommendations(10, {96060 : 1}))
