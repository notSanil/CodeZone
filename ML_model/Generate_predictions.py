from surprise.model_selection import train_test_split
from ML_model.Problemlens import ProblemLens
from collections import defaultdict
from operator import itemgetter
import pandas as pd


def recommendations(username = 'harasees_singh', k = 10) :
    #k = number of recommendations
    ml = ProblemLens()
    data, size = ml.loadProblemLens(username)

    size = 1 - 292805/size # ratio of data that's part of our testSet
    trainset, testSet = train_test_split(data, test_size=size, shuffle=False)

    testSet = data.build_full_trainset()

    df = pd.read_csv('./Ml_model/trained_data.csv')
    simsMatrix = df.values.tolist()     #loading the similarity matrix obtained by training model

    testUserInnerID = testSet.to_inner_uid(username)
    # Get the top K items we rated
    testUserRatings = testSet.ur[testUserInnerID]
    # kNeighbors = heapq.nlargest(k, testUserRatings, key=lambda t: t[1])

    # Get similar items to stuff we liked (weighted by score)
    candidates = defaultdict(float)
    for itemID, rating in testUserRatings:
        if (rating <= 4.4):
            continue
        similarityRow = simsMatrix[itemID]
        for innerID, score in enumerate(similarityRow):
            candidates[innerID] += score * (rating / 5.0)
    
    # Build a dictionary of stuff the user has already seen
    solved = {}
    for itemID, rating in testSet.ur[testUserInnerID]:
        solved[itemID] = 1

    # Get top-rated items from similar users:
    pos = 0
    output = []
    for itemID, ratingSum in sorted(candidates.items(), key=itemgetter(1), reverse=True):
        
        if not itemID in solved:
            problemID = trainset.to_raw_iid(itemID)
            problemID = int(problemID)
            output.append(problemID)
            pos += 1
            if (pos > k):
                break

    return output

if __name__ == '__main__':
    print(recommendations('notSanil'))
