# -*- coding: utf-8 -*-
"""
The below code trains the model based upon the item-based collaborative filtering approach and exports the result in the form of a 2d matrix stored as a CSV file
"""
from surprise import Dataset, Reader, SVD, accuracy
from surprise.model_selection import train_test_split
from Problemlens import ProblemLens
from surprise import KNNBasic
import heapq
from collections import defaultdict
from operator import itemgetter
import pandas as pd      

ml = ProblemLens()
data, size = ml.loadProblemLens()

size = 1 - 292805/size
trainSet, testSet = train_test_split(data, test_size=size, shuffle=False)

# trainSet = trainSet.build_full_trainset()

sim_options = {
                'name': 'cosine',
                'user_based': False
               }

model = KNNBasic(sim_options=sim_options)
model.fit(trainSet)
simsMatrix = model.compute_similarities()

df = pd.DataFrame(simsMatrix)
df.to_csv('trained_data.csv', index=False)


