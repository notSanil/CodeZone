import os
import csv
import sys
import re

from surprise import Dataset
from surprise import Reader

from collections import defaultdict
import numpy as np
import pandas as pd
class ProblemLens:

    ratingsPath = '/Users/uttammittal02/Desktop/CodeZone/user_data_1.csv'
    problemsPath = '/Users/uttammittal02/Desktop/CodeZone/problem_set.csv'

    def loadProblemLens(self):

        # Look for files relative to the directory we are running from
        os.chdir(os.path.dirname(sys.argv[0]))

        score_dataset = 0
        df = pd.read_csv(self.ratingsPath)
        reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)
        score_dataset = Dataset.load_from_df(df= df, reader=reader)
        
        index = df.index
        number_of_rows = len(index)
        return score_dataset, number_of_rows

    # def getUserRatings(self, user):
    #     userRatings = []
    #     hitUser = False
    #     with open(self.ratingsPath, newline='') as csvfile:
    #         ratingReader = csv.reader(csvfile)
    #         next(ratingReader)
    #         for row in ratingReader:
    #             userID = int(row[0])
    #             if (user == userID):
    #                 movieID = int(row[1])
    #                 rating = float(row[2])
    #                 userRatings.append((movieID, rating))
    #                 hitUser = True
    #             if (hitUser and (user != userID)):
    #                 break

    #     return userRatings

    def gettags(self):
        tags = defaultdict(list)
        genreIDs = {}
        maxGenreID = 0
        with open(self.problemsPath, newline='', encoding='ISO-8859-1') as csvfile:
            movieReader = csv.reader(csvfile)
            next(movieReader)  #Skip header line
            for row in movieReader:
                movieID = int(row[0])
                genreList = row[2]
                genreIDList = []
                for genre in genreList:
                    if genre in genreIDs:
                        genreID = genreIDs[genre]
                    else:
                        genreID = maxGenreID
                        genreIDs[genre] = genreID
                        maxGenreID += 1
                    genreIDList.append(genreID)
                tags[movieID] = genreIDList
        for (movieID, genreIDList) in tags.items():
            bitfield = [0] * maxGenreID
            for genreID in genreIDList:
                bitfield[genreID] = 1
            tags[movieID] = bitfield            
        
        return tags

    def get_problem_ratings(self):
        p = re.compile(r"(?:\((\d{4})\))?\s*$")
        years = defaultdict(int)
        with open(self.problemsPath, newline='', encoding='ISO-8859-1') as csvfile:
            movieReader = csv.reader(csvfile)
            next(movieReader)
            for row in movieReader:
                movieID = int(row[0])
                year = row[1]
                if year:
                    years[movieID] = int(year)
        return years

