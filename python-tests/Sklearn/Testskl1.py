import pandas as pd
#ML-Linear Regression model
import numpy as np
import sklearn

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

#create an object to instantiate a dataset
boston_dataset = load_boston()
boston_dataset

#built in methods to explore the dataset (
# to see no of observations,instances, attributes and other properties)
print(boston_dataset['DESCR'])

#look into features in dataset
print(boston_dataset['feature_names'])
print(boston_dataset['target'])

#store dataset in a dataframe
df_boston = pd.DataFrame(boston_dataset.data)

#set features as columns in dataframe
df_boston.columns = boston_dataset.feature_names

#view first 5 observations
df_boston.head()

#print shape
print(boston_dataset.data.shape)

#to see labels or responses
print(boston_dataset.target.shape)

#view target/response
print(boston_dataset['target'])

#Prices of houses in boston area is one of the columns,define it as target/response
df_boston['Price'] = boston_dataset.target

#check if price was added as a column
df_boston.head()

#assign attributes/features to x-axis
X_features = boston_dataset.data

#assign target on Y axis
Y_target = boston_dataset.target

#To use sklearn lr model import its class & create an object called estimator 
#to instantiate

from sklearn.linear_model import LinearRegression
lineReg = LinearRegression()

#since model is created, fit the dataset ,both features and target values into
#into estimator (ie model object lineReg)
lineReg.fit(X_features,Y_target)

#print the intercept
#%2f is used to round of decimal numbers to 2
print('the estimated intercept %.2f ' %lineReg.intercept_)

#print coefficients
print('the coefficients is %d ' %len(lineReg.coef_))

#use cross validation to train the model
#import cross validation class & split data for train & test
#from sklearn import cross_validation
#X_train,X_test,Y_train,Y_test = cross_validation.train_test_split(X_features,Y_target)

X_train,X_test,Y_train,Y_test = train_test_split(X_features,Y_target)

print(boston_dataset.data.shape)
print(X_train.shape, X_test.shape,Y_train.shape,Y_test.shape)

#fit training dataset into estimator/model object
lineReg.fit(X_train,Y_train)

y_pred = lineReg.predict(X_test)
print(y_pred)
Y_test

#Regression accuracy metrics : MSE(Mean squared error),MAE(Mean absolute error),
#RMSE(Root Mean squared error), R-Squared( coefficient of determination)

#mean square error or residual sum of sqaures
print('MSE value is %.2f ' % np.mean((lineReg.predict(X_test)-Y_test) ** 2))
#calc variance
#use score method, closer the value to 1, higher would be the accuracy
print('variance score is %.2f ' % lineReg.score(X_test,Y_test))

#print the intercept
#%2f is used to round of decimal numbers to 2
print('the estimated intercept %.2f ' %lineReg.intercept_)

#print coefficients
print('the coefficients is %d ' %len(lineReg.coef_))

#import required libs for calculating MSE to test accuracy of model
from sklearn import metrics
print(np.sqrt(metrics.mean_squared_error(Y_test,y_pred)))

#for extra information on using python for regression problems and using
#spark as processing framework

import numpy as np
import sklearn.metrics as metrics
import matplotlib.pyplot as plt

yorig = np.array([-3,-1,-2,1,-1,1,2,1,3,4,3,5])
ypred = np.array([-2,1,-1,0,-1,1,2,2,3,3,3,5])
x = list(range(len(yorig)))

plt.scatter(x,yorig, color="red",label="original")
plt.scatter(x,ypred,color="blue",label="predicted")
plt.legend()
plt.show()

#manual approach
diff = Y_test - y_pred
mse = np.mean(diff**2)
mae = np.mean(abs(diff))
rmse = np.sqrt(mse)
r2 = 1-(sum(diff**2)/sum(Y_test-np.mean(Y_test))**2)
print("mse:",mse)
#similarly other print statements

#sklearn approach
mae = metrics.mean_absolute_error(Y_test,y_pred)
mse = metrics.mean_squared_error(Y_test,y_pred)
rmse = np.sqrt(mse)
r2 = metrics.r2_score(Y_test,y_pred)









