#import required library PCA
#

from sklearn.decomposition import PCA

#import the dataset
from sklearn.datasets import make_blobs

#define sample and random state
n_sample = 20
random_state = 20

#generate the dataset with 10 features (dimension)
X,y = make_blobs(n_samples=n_sample,n_features=10,random_state=None)
#Aim is to reduce the no of features present in dataset to defined/desired 
# low dimensional value

#view the shape of dataset
print(X.shape)

#define the PCA estimator with number of reduced components
#to reduce features from 10 to say 3
pca = PCA(n_components=3)

#fit the data into the PCA-estimator
pca.fit(X)
print(pca.explained_variance_ratio_)

#print the find PCA component
first_pca = pca.components_[0]
print(first_pca)

#transform the fitted data using transform method to apply dimensionality reduction
pca_reduced = pca.transform(X)

print(pca_reduced.shape)
