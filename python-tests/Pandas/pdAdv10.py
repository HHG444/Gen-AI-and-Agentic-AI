import pandas as pd
import numpy as np

df_student_math = pd.DataFrame({'student':['Tom','Jack','Dan','Ram','Jeff','David'],
'ID':[10,56,31,85,9,22]})

#student dataframe with science data
df_student_science = pd.DataFrame({'student':['Tom','Ram','David'],
'ID':[10,12,22]})
#Merge both dataframes to create 1 DF
pd.merge(df_student_math,df_student_science)
#merge with key on student
pd.merge(df_student_math,df_student_science,on = 'student')
#merge left join on key ID and also fill NAN values with X
pd.merge(df_student_math,df_student_science,on = 'ID',how='left').fillna('X')
#concatenate dataframes
pd.concat([df_student_math,df_student_science],ignore_index=True)
#define new data frame with student survey data
df_student_survey_data = pd.DataFrame({'student':['Tom','Jack','Tom','Ram','Jeff','Jack'],
'ID':[10,56,10,85,9,56]})
#view the dataframe
df_student_survey_data
#check for duplicated values
df_student_survey_data.duplicated()
#drop duplicate values with student as key
df_student_survey_data.drop_duplicates('student')
#drop duplicates with ID as Key
df_student_survey_data.drop_duplicates('ID')



