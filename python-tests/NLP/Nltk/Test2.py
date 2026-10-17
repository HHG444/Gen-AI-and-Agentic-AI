#Process documents using bag of words

#this class helps tokenizing the documents,it converts text into vector by assigning
#numeric values to each word
from sklearn.feature_extraction.text import CountVectorizer

#create an object vectorizer by instantiating the class
vectorizer = CountVectorizer()

#create random documents
document1 = "Hi How are you"
document2 = "today is a very very very pleasant day and we can have some fun fun fun"

document3 = 'This was an amazing experience'

#putting them togther as a list
listofdocuments = [document1,document2,document3]
listofdocuments

# for i in listofdocuments:
#     for j in i.split():
#         print(i,j,i.count(j))


#Creating a bag of words for list of documents
#we can use fit method and fit the documents to the vectorized object
bag_of_words = vectorizer.fit(listofdocuments)
bag_of_words
#check the bag of words
bag_of_words

#apply transform method and tranform the list fo documents
bag_of_words = vectorizer.transform(listofdocuments)

#print bag of words and see properties of vectorized object 
# (1st being tuple and 2nd being freq of words)
print(bag_of_words)

#tuple indicates the document number feature indices of each word which belongs 
# to document
#feature indices are generated from the transform method by feature extraction process

#check for repeated words
print(vectorizer.vocabulary_.get('very'))
print(vectorizer.vocabulary_.get('fun'))

vectorizer.vocabulary_.get('day')

#check the type of bag of words
type(bag_of_words)

