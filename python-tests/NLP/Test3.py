#Organizing the data
# Let's take a look at our dataframe
data_df

# Let's add the comedians' full names as well
full_names = ['Ali Wong', 'Anthony Jeselnik', 'Bill Burr', 'Bo Burnham', 'Dave Chappelle', 'Hasan Minhaj',
              'Jim Jefferies', 'Joe Rogan', 'John Mulaney', 'Louis C.K.', 'Mike Birbiglia', 'Ricky Gervais']

data_df['full_name'] = full_names
data_df

# Let's pickle it for later use
data_df.to_pickle("Nlp/corpus.pkl")

#Creating Document-Term Matrix
# We are going to create a document-term matrix using CountVectorizer, 
# and exclude common English stop words
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(stop_words='english')
data_cv = cv.fit_transform(data_clean.transcript)
data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
data_dtm.index = data_clean.index
data_dtm

# Let's pickle it for later use
data_dtm.to_pickle("Nlp/dtm.pkl")

# Let's also pickle the cleaned data (before we put it in document-term matrix format) and the CountVectorizer object
data_clean.to_pickle('Nlp/data_clean.pkl')
pickle.dump(cv, open("Nlp/cv.pkl", "wb"))

