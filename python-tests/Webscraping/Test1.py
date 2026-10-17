#Scraping a web document, parsing it and use objects to extract information
#import libraries
from bs4 import BeautifulSoup

#create a html document
#create a soup object and pass web document as a parameter
html_doc = """<html>
<body>
<h1>My First Heading</h1>
<b><!--This is a comment line ---></b>
<p title="About me " class ="test">My First Paragraph</p>
<div class="cities">
<h2>London</h2>
</div>
</body>
</html>
"""
#parse it using html parser
soup = BeautifulSoup(html_doc,'html.parser')

#view the soup type
type(soup)

#View the soup object
print(soup)

#Create a tag object
tag = soup.p

#view the tag object type
type(tag)

#print the tag
print(tag)

#create a comment object type
comment = soup.b.string

#view the comment object type
type(comment)

#view commment
comment

#View tag attributes
tag.attrs

#view the tag value
tag.string

#view the tag type(Navigable string)
type(tag.string)
