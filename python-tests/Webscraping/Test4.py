#Modifying a web tree to get the desired result with the help of an example
#import
from bs4 import BeautifulSoup

#Create employee html document
employee_html_doc = """<employees>
<employee class="accountant">
<firstname>John</firstname>
<lastname>Doe</lastname>
</employee>
<employee class="manager">
<firstname>Anna</firstname>
<lastname>Smith</lastname>
</employee>
<employee class="developer">
<firstname>Peter</firstname>
<lastname>Jones</lastname>
</employee>
</employees>
"""

#create soup object
soup_emp = BeautifulSoup(employee_html_doc,'html.parser')

#access and view the tag
tag = soup_emp.employee
tag

#Modify the tag (add a new tag and insert a string value)
tag['class'] = 'manager'

#view the tag to see the modification
tag

#view the soup object to verify the modification
soup_emp

#add a tag 
tag = soup_emp.new_tag('rank')
tag.string = 'Manager 1'

#modify using insert_after method
soup_emp.employees.employee.insert_after(tag)

#View the soup object
print(soup_emp)

#clear all the modified tags (if performed modification was wrong)
tag.clear()

#view the soup object
soup_emp

#create a tag object and view it
tag = soup_emp.employees.employee
tag

#extract the information using extract method
tag.firstname.string.extract()

#modify the tag name
tag.firstname.replace_with('first name')

#view the change
soup_emp.employees

