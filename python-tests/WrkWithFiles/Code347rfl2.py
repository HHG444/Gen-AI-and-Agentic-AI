#The script uses the os module to make sure that the passed in file path is a file 
# that exists on the disk. If the path exists then each line of the file is read and 
# passed to a function called record_word_cnt as a list of strings, delimited the spaces
#  between words as well as a dictionary called bag_of_words. The record_word_cnt 
# function counts each instance of every word and records it in the bag_of_words 
# dictionary.
#Once all the lines of the file are read and recorded in the bag_of_words dictionary,
#  then a final function call to order_bag_of_words is called, which returns a 
# list of tuples in (word, word count) format, sorted by word count. The returned 
# list of tuples is used to print the most frequently occurring 10 words.
#Note** This can be also done in a mapreduce way

import sys
import os

def main():
   filepath = 'I:\\Trainings\\MyContent\\Books\\MetadataInfo.txt'

   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()
  
   bag_of_words = {}
   with open(filepath) as fp:
       cnt = 0
       for line in fp:
           print("line {} contents {}".format(cnt, line))
           record_word_cnt(line.strip().split(' '), bag_of_words)
           cnt += 1
   sorted_words = order_bag_of_words(bag_of_words, desc=True)
   print("Most frequent 10 words {}".format(sorted_words[:10]))
  
def order_bag_of_words(bag_of_words, desc=False):
   words = [(word, cnt) for word, cnt in bag_of_words.items()]
   return sorted(words, key=lambda x: x[1], reverse=desc)

def record_word_cnt(words, bag_of_words):
   for word in words:
       if word != '':
           if word.lower() in bag_of_words:
               bag_of_words[word.lower()] += 1
           else:
               bag_of_words[word.lower()] = 1

if __name__ == '__main__':
   main()