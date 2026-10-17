import numpy as np
names = np.array(['patrick','john','sean','jack','aimie','tack'])
names2 = names

names
names2

names is names2
names[0]= 'pat'
names
names2
names is names2

###########################
names
names3 = names.view()
names is names3
names[0]='sharon'
names
names3

names is names3
################
names
names4 = names.copy()
names is names4
names4
names[0]= 'johny'
names
names4


