#Parsing a part of document
#import required library
from bs4 import BeautifulSoup

#sample web document from www.simplilearn.com website
data_SL = """<ul class= "content-col_discover">
<h5>Discover</h5>
<li><a href="/resources" id="free_resources">Free resources</a></li>
<li><a href="http://community.simplilearn.com/" id="community">Simplilearn community</a></li>
<li><a href="/career-data-labs" id="lab">Career data labs</a></li>
<li><a href="/scholarships-for-veterans" id="scholarship">Veterans scholarship</a></li>
<li><a href="http://www.simplilearn.com/feed/" id="rss">RSS Feed</a></li>
</ul>
"""
#create soup object
soup_SL = BeautifulSoup(data_SL,'html.parser')

#parse only part of the document , text(string) values for tags using getText method
print(soup_SL.get_text())

#import SoupStrainer class for parsing the desired part of web document
from bs4 import SoupStrainer

#create object to parse only the id(link) with lab
tags_with_LabLink = SoupStrainer(id="lab")

#print the part of parsed document
print(BeautifulSoup(data_SL,'html.parser',parse_only=tags_with_LabLink).prettify())