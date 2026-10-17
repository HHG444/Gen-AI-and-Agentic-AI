#using unpacking feature
coordinates = (1,2,3)
#say if we want to use these values multiple times
#in our program
#x = coordinates[0]
#y = coordinates[1]
#z = coordinates[2]
x,y,z = coordinates
print(x)
print(y)
print(z)
print('-'* 40)

#Python interpreter looks into tuple and
#assigns values to x,y and z i.e. unpacks the tuple
#to variables
#similarly
coordinates = [1,2,3]
x,y,z = coordinates
print(x)


