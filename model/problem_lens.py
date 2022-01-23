import csv
import re

from surprise import Dataset
from surprise import Reader

from collections import defaultdict
import pandas as pd



'''
In case of item based collaborative filtering, this file is only required to train the model. For getting predictions from the model, we just need 2 files obtained during the training period
'''

class ProblemLens:

    ratingsPath = './data/user_data_1.csv'
    problemsPath = './data/problem_set.csv'

    def loadProblemLens(self):

        score_dataset = 0
        
        df = pd.read_csv(self.ratingsPath).iloc[:, 0:3]
        
        reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)
        score_dataset = Dataset.load_from_df(df= df, reader=reader)
        
        index = df.index
        number_of_rows = len(index)
        return score_dataset, number_of_rows

    def gettags(self):
        tags = defaultdict(list)
        tagIDs = {}
        maxtagID = 0
        with open(self.problemsPath, newline='', encoding='ISO-8859-1') as csvfile:
            problemReader = csv.reader(csvfile)
            next(problemReader)  #Skip header line
            for row in problemReader:
                problemID = int(row[0])
                tagList = row[2]
                tagIDList = []
                for tag in tagList:
                    if tag in tagIDs:
                        tagID = tagIDs[tag]
                    else:
                        tagID = maxtagID
                        tagIDs[tag] = tagID
                        maxtagID += 1
                    tagIDList.append(tagID)
                tags[problemID] = tagIDList
        for (problemID, tagIDList) in tags.items():
            bitfield = [0] * maxtagID
            for tagID in tagIDList:
                bitfield[tagID] = 1
            tags[problemID] = bitfield            
        
        return tags

    def get_problem_ratings(self):
        p = re.compile(r"(?:\((\d{4})\))?\s*$")
        ratings = defaultdict(int)
        with open(self.problemsPath, newline='', encoding='ISO-8859-1') as csvfile:
            problemReader = csv.reader(csvfile)
            next(problemReader)
            for row in problemReader:
                problemID = int(row[0])
                rating = row[1]
                if rating:
                    ratings[problemID] = int(rating)
        return ratings

if __name__ == '__main__':
    ProblemLens().loadProblemLens('notSanil')
