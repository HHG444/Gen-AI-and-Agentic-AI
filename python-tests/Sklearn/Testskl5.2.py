#K-Means using sklearn
#kmeans test
import numpy as np
#import KMeans class from sklearn.cluster
from sklearn.cluster import KMeans
#scikit has random sample generators
#import make_blobs dataset from sklearn.cluster
#they are used to create artifical datasets of a specified complexity n size

from sklearn.datasets import make_blobs

#specify property of dataset to be generated
#define number of samples
n_samples = 300 #defines total no of points distributed equally

#define random state value to intialize the cluster
random_state = 20 # to intialize the centroid

#define how many features the sample will have
X,y = make_blobs(n_samples=n_samples,n_features=5,random_state=None)

#Test this
# X,y = make_blobs(n_samples=10, centers=2, n_features=2,random_state=0)

#define the number of clusters to be formed as 3 and fit features in model
predict_y = KMeans(n_clusters=3,random_state=random_state).fit_predict(X)

#if we print the estimator object, it returns lable value of each datapoint

print(predict_y)

#Another example:
N,y = make_blobs(n_samples=2,n_features=5,random_state=None)
predict_n = KMeans(n_clusters=2,random_state=random_state).fit_predict(N)
print(predict_n)

#Using plotting and looking at coordinates

X = np.array([[1,2],[1.5,1.8],[5,8],[8,8],[1,0.6],[9,11]])
clf = KMeans(n_clusters=2)
clf.fit(X)
centroids = clf.cluster_centers_
labels = clf.labels_
centroids
labels

colors = 10 * ["g.","r.","c.","b.","k."]
colors
X
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
for i in range(len(X)):
    plt.plot(X[i][0],X[i][1], colors[labels[i]],markersize = 15)
plt.scatter(centroids[:,0], centroids[:,1], marker='x',s=150, linewidths=5)
plt.show()
predict_y = KMeans(n_clusters=2,random_state=random_state).fit_predict(X)
print(predict_y)




