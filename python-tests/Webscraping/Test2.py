#Searching in a Tree using filters
#Open the web scraping sample html file with python open method (read only method)
from bs4 import BeautifulSoup

#create a soup object and pass the web document as a paramter and use lxml parser for parsing
HTMLfilepath = "Webscraping/web_scraping_example.html" 
with open(HTMLfilepath,"r") as organization:
    soup = BeautifulSoup(organization,"lxml")

#view contents of soup object
soup.contents

#search using find methods (later we can search in tree using filters)
tag_li=soup.find("li")
tag_li

#create a tag object and print it
print(type(tag_li))

#using id, print the associated information
print(tag_li)

#search the document using find method for an ID
find_id = soup.find(id="HR")

#print the find_id object
print(find_id)

#print the string value
print(find_id.li.div.string)

#search using string only
search_for_StringOnly = soup.findAll(text = ["Kelly","Jack"])

#print the search values
print(search_for_StringOnly)

#search based on css class name(present as an attribute)
css_class_search = soup.find(attrs={"class":"ITmanager"})
print(css_class_search)

#create a function to search the document based upon the tag passed as paramter
#use this function to find attribute id with the tag Finance
def is_account_manager(tag):
    return tag.has_attr("id") and tag.get("id") == "Finance"

#search the document using function and print it
account_manager = soup.find(is_account_manager)
print(account_manager.li.div.string)

#print tag name using True - which returns all the tags present in the document
for tag in soup.findAll(True):
    print(tag.name)

#search using findall method for the given class
find_class = soup.findAll(class_= 'HRmanager')

#view type of class
type(find_class)
find_class
#print the second resultset
print(find_class[0])

#print the second result
print(find_class[1])

#find parents using 'find parent' method
find_class = find_class[0]
find_parent = find_class.find_parent("ul")
print(find_parent)

#Create another soup object and find id 'IT' and view the contents
#using find mthod to search based on the id
org = soup.find(id = "IT")

#looking at seach object
print(org)

#find the next siblings
next_sibling = org.findNextSiblings()
next_sibling

#print parents
parent = org.findParent
print(parent)

#find and print previous (search all previous tags)
all_previous = org.findAllPrevious()
print(all_previous)

#search and print previous sibling
previous_sibling = org.findPreviousSibling()
previous_sibling

#search and print all next
all_next = org.findAllNext()
print(all_next)

#use regular expression to search the document
#we create a sample example to extract email id
import re
email_example = """ <br/>
<p>my email id is </p>
abc@example.com"""
soup_email = BeautifulSoup(email_example,"lxml")

#use compile method to compile the information which contains regular expression
emailid_regexp = re.compile("\w+@\w+\.\w+")

#find and print the email id using regular expression
email_id = soup_email.find(text = emailid_regexp)
print(email_id)


