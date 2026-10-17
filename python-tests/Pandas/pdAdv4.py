import pandas as pd
import numpy as np

data = pd.DataFrame({'k1': ['one'] * 3 + ['two'] * 4,'k2': [1, 1, 2, 3, 3, 4, 4]})
data
print(data)

data.duplicated
print(data.duplicated)

data.drop_duplicates()
#data.drop_duplicates(['k1'])
print(data.drop_duplicates())

#using funcs or mappings
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami',
'corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'],
'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
data
print(data)

meat_to_animal = {
'bacon': 'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}

data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
data['animal'] = data['food'].map(str.lower).map(lambda n: n.upper())
print(data)

#using lambda
#data['food'].map(lambda x: meat_to_animal[x.lower()])
print(data['food'].map(lambda x: meat_to_animal[x.lower()]))

#replacing value
data = pd.Series([1., -999., 2., -999., -1000., 3.])
#data.replace(-999, np.nan)
print(data.replace(-999, np.nan))

#replacing multiple values
data.replace([-999, -1000], np.nan)

#different replacement for each value
data.replace([-999, -1000], [np.nan, 0])
#or using a dict
data.replace({-999: np.nan, -1000: 0})

data = pd.DataFrame(np.arange(12).reshape((3, 4)),index=['james', 'john', 'mary'],
columns=['1st', '2nd', '3rd', '4th'])
data.index.map(str.upper)
data.index = data.index.map(str.upper)
data

#to create a transformed version of a data set without modifying the original
data.rename(index=str.title, columns=str.upper)

data.rename(index={'JOHN': 'JOHNY'},columns={'3RD': '3rd'})
#to modify a data set in place, pass inplace=True

