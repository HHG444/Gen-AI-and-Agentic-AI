#Performing Sentence Analysis
import string
from nltk.corpus import stopwords

#view first 10 stopwords present in english corpus
stopwords.words('english')[0:10]

#create a test sentence
test_sentence = 'This is my first test string. Wow! we are doing fine'

#eliminate the punctuation in form of characters and print them
no_punctuation = [char for char in test_sentence if char not in string.punctuation]
no_punctuation

#eliminate the punctuation and print them as a whole sentence
no_punctuation = ''.join(no_punctuation)
no_punctuation

#split each word present in new sentence
#removing stop words
no_punctuation.split()
# for i in no_punctuation.split():
#     if i.lower() not in stopwords.words('english'):
#         print(i)

clean_sentence = [word for word in no_punctuation.split() if word.lower() not in stopwords.words('english')]

#getting your cleaned sentence
clean_sentence

