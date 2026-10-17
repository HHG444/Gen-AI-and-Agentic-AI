import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.model_selection import train_test_split #instead of cross_validation
import pandas as pd


X = np.array([[1,2],[1.5,1.8],[5,8],[8,8],[1,0.6],[9,11]])
X

plt.scatter(X[:,0],X[:,1], s= 100, linewidth=5)
plt.show()

#define classifier
clf = KMeans(n_clusters=2)

clf.fit(X)

centroids = clf.cluster_centers_

labels = clf.labels_

colors = 10 * ["g.","r.","c.","b.","k."]

for i in range(len(X)):
    plt.plot(X[i][0],X[i][1], colors[labels[i]],markersize = 15)
plt.scatter(centroids[:,0], centroids[:,1], marker='x',s=150, linewidths=5)
plt.show()

#==========================================
#KMeans on a public dataset
#https://pythonprogramming.net/static/downloads/machine-learning-data/titanic.xls

#@@conversion error

# Pclass Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
# survival Survival (0= No; 1 = Yes)
# name Name
# sex Sex
# age Age
# sibsp Number of Siblings/Spouses Aboard
# parch Number of Parents/Children Aboard
# ticket Ticket Number
# fare Passenger Fare (British Pound)
# cabin Cabin
# embarked Port of embarkation ( C = Cherbourg; Q = Queenstown ; S = Southampton)
# boat Lifeboat
# body Body Identification Number
# home.dest Home/Destination

#Using KMeans to separate people in two groups of ppl who would survive or die 

df = pd.read_excel("https://raw.githubusercontent.com/ajaykuma/Datasets/master/titanic.xls")
df.head()

#sex-imp characteristic but not numerical
#cabin-imp characteristic but not numerical
#embarked-imp characteristic but not numerical
#home.dest-imp characteristic but not numerical

#ML would prefer numerical data
df.drop(['body','name'],1,inplace=True)
#df.convert_objects(convert_numeric=True)
df.fillna(0, inplace =True)
df
columns = df.columns.values
def handle_non_numerical_data(df):
    columns = df.columns.values

    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]
        
        if df[column].dtype != np.int64 and df[column].dtype != np.float:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x +=1
            df[column] = list(map(convert_to_int, df[column]))   
    return df

df = handle_non_numerical_data(df)
#print(df.head())  

X = np.array(df.drop(['survived'],1))
y = np.array(df['survived'])

clf = KMeans(n_clusters=2)
clf.fit(X)

correct = 0
for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = clf.predict(predict_me)
    if prediction[0] == y[1]:
        correct += 1
        
print(correct/len(X))
