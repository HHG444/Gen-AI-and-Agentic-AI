# Problem statement
# You are working for a team and are trying to understand which features users want added
# to a new version of an app/device the most.Your team has received a large number of feature Requests
# from users.

# Write an algorithm that identifies the most popular N feature requests out of a list of feature 
# requests & possible features. Your algorithm should output the most frequently mentioned features.

# Input:
# The input to the function/method consists of 5 arguements:
# numFeatures: an integer representing the number of possible features.
# topFeatures: an integer representing the number of top features that your function 
# retuns (N)
# possibleFeatures: a list of single-word strings representing the possible features
# numFeatureRequests: an integer representing the number of feature requests.
# featureRequests: a list of strings where each element is a string that consists of space-separated 
# words representing feature requests.

# Output:
# Return a list of strings representing the most popular N feature requests in order of 
# most to least to least frequently mentioned.

# Note** the comparision of strings is case sensitive.
# If the value of topFeatures is  more than the number of possible features, return the names of
# only the features mentioned in the possible features.
# Multiple occurence of a feature in a quote should be considered as a single mention
# If features are mentioned an equal number of times in feature requests(eg:newshop=2,
# shownow=2,mymarket=4),sort alphabetically.topFeatures=2,Output=[mymarket,newshop]

# For example function can be:
# def popularFeatures(numFeatures, topFeatures, possibleFeatures,
#                     numFeatureRequests, featureRequests):
#     //write your code here
#     pass

# For example:
# Input: 
# numFeatures=6
# topFeatures=2
# possibleFeatures=['storage','battery','disk','memory','waterresistent','processor']
# numFeatureRequests=6
# featureRequests=['I wish my device had more storage','I wish the battery life on 
# my device was good','I travel a lot and would enjoy if device was waterresistent',
# 'waterresistent and good processor are my two top requirements','I want to use 
# my device under water,waterresistent please Waterresistent!','How cool would it be if my device
# had strong processor']

# Output:
# [waterresistent,processor]
##################################################

#finding most features requested from available 
#list of possible features
topFeatures = 2
possibleFeatures = ["storage","space","memory","cpu"]
featureRequests = ["i wish i had more storage",
"it would be good to have more cpu",
"i wish i had more memory",
"memory and cpu should be more",
"i need more storage",
"i need more cpu",
"i wish i had more memory",
"i wish i had more space"]
numFeatures = len(possibleFeatures)
print(numFeatures)

numFeatureRequests = len(featureRequests)
print(numFeatureRequests)

frlist = list(map(lambda n: n.split(),featureRequests ))
print(frlist)

frlistCcat = []
for sublist in frlist: 
    for item in sublist:
        frlistCcat.append(item)
print(frlistCcat)

SupportedFeatures = []
dictio = {}

for i in possibleFeatures:
    for j in frlistCcat:
        if i==j:
           m = i
           n = frlistCcat.count(m)
           dictio[m]=n
SupportedFeatures.append(sorted(dictio.items(),key=lambda x:x[1],reverse=True))

print(dictio)
print(SupportedFeatures)

#finding 2 features based on highest demands by customers
SupportedFeatures[0][0:topFeatures]

#-----------------------------------------------#

#Function:
def popularFeatures(possibleFeatures,featureRequests,topFeatures,numFeatures=0, 
                     numFeatureRequests=0):
    n = topFeatures
    numFeatures = len(possibleFeatures)
    print('numFeatures: ',numFeatures)

    numFeatureRequests = len(featureRequests)
    print('numFeatureRequests: ',numFeatureRequests)

    frlist = list(map(lambda n: n.split(),featureRequests ))
    #print(frlist)

    frlistCcat = []
    for sublist in frlist: 
        for item in sublist:
            frlistCcat.append(item)
    #print('Features that can be considered: ',frlistCcat)

    SupportedFeatures = []
    dictio = {}

    for i in possibleFeatures:
        for j in frlistCcat:
            if i==j:
                m = i
                n = frlistCcat.count(m)
                dictio[m]=n
    SupportedFeatures.append(sorted(dictio.items(),key=lambda x:x[1],reverse=True))

    #print(dictio)
    print(SupportedFeatures[0][0:n])
    #print(SupportedFeatures)

#finding 2 features based on highest demands by customers
#SupportedFeatures[0][0:topFeatures]

#Assign values & Pass these in function
topFeatures = 2
possibleFeatures = ["storage","space","memory","cpu"]
featureRequests = ["i wish i had more storage",
"it would be good to have more cpu",
"i wish i had more memory",
"memory and cpu should be more",
"i need more storage",
"i need more cpu",
"i wish i had more memory",
"i wish i had more space"]

popularFeatures(possibleFeatures,featureRequests,numFeatures=0, topFeatures=0,
                     numFeatureRequests=0)
           
           






