#Applying Pipeline and Grid Search
import pandas as pd
import string
from pprint import pprint 
from time import time

#import the dataset
df_spam_collection = pd.read_csv('I:\\GitContent\\Datasets\\SpamCollection',sep='\t',names = ['response','message'])

df_spam_collection.head()

#import text processing libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

#import SGD classfier (to classify message in dataset)
from sklearn.linear_model import SGDClassifier

#import for gridsearch
from sklearn.model_selection import GridSearchCV

#import for pipeline

from sklearn.pipeline import Pipeline

#define the pipeline
#create pipeline by instantiating the pipeline class and passing vectorized, transformed and model classifier as arguments
pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf',SGDClassifier())
])

#paramters for gridsearch (tfidf paramters will be used to weigh the terms present in msg)
parameters = {'tfidf__use_idf':(True,False)}

#perform the gridsearch with pipeline and parameters
grid_search = GridSearchCV(pipeline,parameters,n_jobs=-1,verbose=1)
print('performing grid search now..')
print('paramters: ')
pprint(grid_search)

t0 = time()
grid_search.fit(df_spam_collection['message'],df_spam_collection['response'])
print('done in %0.3fs'%(time()-t0))



