#Model persistence
#

from sklearn.datasets import load_iris
iris_dataset = load_iris()

print(iris_dataset.feature_names)

print(iris_dataset.target)

#assign features and target objects
X_feature = iris_dataset.data
Y_target = iris_dataset.target

#create object with new values for prediction
X_new = [[3,5,4,1],[5,3,4,2]]

#use logistic regression estimator
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()

#fit data into estimator
logreg.fit(X_feature,Y_target)

#predict the outcome
logreg.predict(X_new)
print(logreg.predict(X_new))

#import library for model persistence
import pickle as pkl

#use dumps method to persist the model
persist_model = pkl.dumps(logreg)
print(persist_model)

#use joblib.dump to persist the model to a file
from sklearn.externals import joblib
joblib.dump(logreg, 'regresfilename.pkl')

#use joblib.load to create new estimator from the saved model
new_logreg_estimator = joblib.load('regresfilename.pkl')

print(new_logreg_estimator)

#validate and use new estimator to predict
print(new_logreg_estimator.predict(X_new))

