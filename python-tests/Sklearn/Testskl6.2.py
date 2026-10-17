import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#%matplotlib inline
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
cancer.keys()
cancer

print(cancer['DESCR'])
print(cancer['target'])


df = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
df.head()

#to reduce 30 dimensions as seen in head to 2 dimensions 
#we need to do standard scaling for PCA as the values seen in head show big difference
#to create a new vector space with reduced dimensions the difference in values should be minimal

from sklearn.preprocessing import StandardScaler

#using sdev=1, mean =0,  StandardScaler scales down the values
#we can also use MinMaxScaler which converts all values between 0 and 1
#create object
scaler = StandardScaler() 

#fit operation
scaler.fit(df)

scaled_data = scaler.transform(df)

scaled_data
scaled_data.shape

#Applying PCA technique
from sklearn.decomposition import PCA
pca = PCA(n_components=2)

pca.fit(scaled_data)

x_pca = pca.transform(scaled_data)

scaled_data.shape
x_pca.shape

x_pca

plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer['target'])
plt.xlabel('First principal component')
plt.ylabel('Second principal component')
plt.show()

#