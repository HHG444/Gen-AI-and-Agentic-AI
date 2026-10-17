#Formatting and printing
#import
from bs4 import BeautifulSoup
import requests

#define url for simplilearn
url = 'http://simplilearn.com'

#access result through requests object
result = requests.get(url)

#load the page content
page_content = result.content

#create soup object
soup = BeautifulSoup(page_content,'html.parser')

#view the contents
soup.contents

#prettify the output
print(soup.prettify())

#view the original encoding
soup.original_encoding

#format the tag a to xml
#to be checked....> soup.body.a.prettify(formatter="html")

#define a custom function to convert string values to uppercase
def upperCaseFn(strtext):
    return strtext.upper()

#format using custom function for outputting string texts in uppercase
soup.body.a.prettify(formatter=upperCaseFn)



