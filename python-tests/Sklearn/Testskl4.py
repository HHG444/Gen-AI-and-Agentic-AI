#K Nearest Neighbors
# https://github.com/ajaykuma/Datasets/blob/master/breast-cancer-wisconsin.data
# https://github.com/ajaykuma/Datasets/blob/master/breast-cancer-wisconsin.names
# The headers in data were created based on entries in names file.
#Looking in names also shows about Missing attributes denoted by "?"

import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/ajaykuma/Datasets/master/breast-cancer-wisconsin.data")
df.replace('?', -99999,inplace=True) #giving this value, makes it huge outlier
df.head()

#getting rid of useless columns/features which do not affect on our result/predicting labels
df.drop(['id'], 1, inplace=True)
df.head()

X = np.array(df.drop(['class'],1))
#X[0]
y = np.array(df['class'])
#y[0]

#split data into training and test set
X_train, X_test, y_train,y_test = train_test_split(X,y,test_size=0.2)

#define classifier
clf = neighbors.KNeighborsClassifier()

#use the fit 
clf.fit(X_train, y_train)

#measuring accuracy/confidence
accuracy = clf.score(X_test, y_test)

print(accuracy)

#try repeating the whole code without dropping the ID column i.e. commenting
#df.drop(['id'], 1, inplace=True)

#summary : We have trained and tested our classifier

#Making Predictions
#below we are not taking the 'id' and 'class' column and creating an array with 
#unique combination of attributes
example_measures = np.array([4,2,1,1,1,2,3,2,1])
example_measures = example_measures.reshape(1,-1)
example_measures
prediction = clf.predict(example_measures)
#predictionTest = clf.predict(X_test)
#print(predictionTest)

print(prediction)

#considering more set of values
example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,1,1,2,3,2,1]])
example_measures = example_measures.reshape(2,-1)
example_measures
prediction = clf.predict(example_measures)

print(prediction)

#if length of example_measures unknown, we can instead provide the length in reshape
example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,1,1,2,3,2,1]])
example_measures = example_measures.reshape(len(example_measures),-1)
prediction = clf.predict(example_measures)

print(prediction)

#Euclidean distance calculation
from math import sqrt
plot1 = [1,3]
plot2 = [2,5]

euclidean_distance = sqrt( (plot1[0]-plot2[0])**2 + (plot1[1]-plot2[1])**2)
print(euclidean_distance)






