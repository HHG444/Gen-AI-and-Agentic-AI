#creating a file
a = open("C:\\PythonCodes\\pytestcr.txt","w+")

#Writing data into a file
for i in range(10):
     a.write("This is line %d\r\n" % (i+1))

#closing the file
a.close()

#opening and appending
a = open("C:\\PythonCodes\\pytestcr1.txt","a+")
for i in range(5):
     a.write("This is appended line %d\r\n" % (i+1))
a.close()
#reading
a = open("C:\\PythonCodes\\pytestcr.txt","r")
if a.mode == 'r':
    contents =a.read()
print(contents)



