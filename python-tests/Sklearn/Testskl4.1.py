#Creating our own K Nearest Neighbors
import numpy as np
import matplotlib.pyplot as plt
import warnings
from matplotlib  import style
from collections import Counter
style.use('fivethirtyeight')
from math import sqrt


#numpy as a inbuilt function to calculate euclidean distance or 
#we can use our own created one

#k class of features & r class of labels
dataset = {'k':[[1,2],[2,3],[3,1]],'r':[[6,5],[7,7],[8,6]]}
dataset
#new point to be classified
new_features = [5,7]

#To look at points in a plot
# [[plt.scatter(ii[0],ii[1], s = 100, color = i) for ii in dataset[i]] for i in dataset]
# plt.scatter(new_features[0],new_features[1],s = 100)
# plt.show()

#problem in knn is , we need to calculate the distance of prediction pt to all othr points
#we can use other approaches such as considering a radius and look within it and forget the outliers

def k_nearest_neighbors(data,predict, k =3):
    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups')
    #knnalgo
    distances = []
    for group in data:
        for features in data[group]:
            #euclidean_distance = sqrt( (features[0]-predict[0])**2 + (features[1]-predict[1])**2) #good only for 2D
            #euclidean_distance = np.sqrt(np.sum ((np.array(features)-np.array(predict))**2)) #using numpy
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance, group])
        
        votes = [i[1] for i in sorted(distances)[:k]]
        print(Counter(votes).most_common(1))
        vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result 

result = k_nearest_neighbors(dataset,new_features,k = 3)  
print(result)  

#thus our point to be predicted belongs to r type 
#To look at points in a plot
[[plt.scatter(ii[0],ii[1], s = 100, color = i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_features[0],new_features[1],color=result,s=100)
plt.show()

#============================
#Using our own knn algo on a public dataset
#Creating our own K Nearest Neighbors
import numpy as np
import warnings
from collections import Counter
from math import sqrt
import pandas as pd
import random

def k_nearest_neighbors(data,predict, k =3):
    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups')
    #knnalgo
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance, group])
        
        votes = [i[1] for i in sorted(distances)[:k]]
        print(Counter(votes).most_common(1))
        vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result 

df = pd.read_csv("https://raw.githubusercontent.com/ajaykuma/Datasets/master/breast-cancer-wisconsin.data")
df.replace('?', -99999,inplace=True) 
df.drop(['id'], 1, inplace=True)
full_data = df.astype(float).values.tolist() 

#print(full_data[:10])

random.shuffle(full_data)
#print(full_data[:5])

test_size = 0.2
train_set = {2:[],4:[]}
test_set = {2:[],4:[]}
#everthing upto last 20%
train_data = full_data[:-int(test_size*len(full_data))]
#last 20% of data 
test_data = full_data[-int(test_size*len(full_data)):]

#to populate train and test set
for i in train_data:
    train_set[i[-1]].append(i[:-1])

for i in test_data:
    test_set[i[-1]].append(i[:-1])

correct = 0
total = 0

for group in test_set:
    for data in test_set[group]:
        vote = k_nearest_neighbors(train_set, data, k =5)
        if group == vote:
            correct +=1
        total += 1
print('Accuracy', correct/total)
 

#=============================
# code can be modified to get confidence levels along with accuracy
#==============================



