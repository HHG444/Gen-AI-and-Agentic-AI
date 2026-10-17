#pipeline using more than one estimator
#
#import pipeline class
from sklearn.pipeline import Pipeline

#import Logistic regression estimator
from sklearn.linear_model import LogisticRegression

#import linear estimator
from sklearn.linear_model import LinearRegression

#import PCA estimator for dimensionality reduction
from sklearn.decomposition import PCA

#chain the estimators together
#Incorrect chaining[as either "LogisticRegression()" or "LinearRegression()" can be used but 
# not both ]: estimator = [('dim_reduction', PCA(),('Logres_model', LogisticRegression()), 
# ('Linear_model'), LinearRegression())]

#correct chaining
estimator = [('dim_reduction', PCA()), ('Linear_model', LinearRegression())]

#put chain of estimators in a pipeline object
pipeline_estimator = Pipeline(estimator)

#check the chain of estimator
print(pipeline_estimator.steps[0])
print(pipeline_estimator.steps[1])
print(pipeline_estimator.steps)


