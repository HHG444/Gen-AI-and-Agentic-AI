import numpy as np
#addition
np.add(45,20)
print(np.add(45,20))

#subtraction
np.subtract(45,23)
print(np.subtract(45,23))

#ndarray multiplication
#create ndarray which contains number of hrs worked for 5 days
#hourly rate 45$
np_daily_wage = np.array([7,8,9,11,13])*45
print(np_daily_wage)

#using sum to add all elements of an array
print(sum(np_daily_wage))

#comparision operators
#Let's say we have a dataset showing total hrs/week a person has worked for 5 weeks
np_weekly_hrs = np.array([23,41,55,47,38])
print(np_weekly_hrs[np_weekly_hrs>40])
print(np_weekly_hrs[np_weekly_hrs!=40])

#logical operators
#logical and
print(np.logical_and(np_weekly_hrs>20,np_weekly_hrs<50))
np_weekly_hrs[np.logical_and(np_weekly_hrs>20,np_weekly_hrs<50)]

#logical not
print(np.logical_not(np_weekly_hrs>35))
np_weekly_hrs[np.logical_not(np_weekly_hrs>35)]


#not using numpy
weeklydur = [23,41,55,47,38]
seldur = []
for i in weeklydur:
    if i>40:
        seldur.append(i)
seldur

#using lambda
seldur = list(filter(lambda n: n>40,weeklydur))
seldur
        






