import numpy as np
new_cyclist_trials = np.array([[10,15,17,26,13,19],[12,13,14,24,14,23]])
new_cyclist_trials
new_cyclist_trials.ndim
x = new_cyclist_trials.ravel()
x
x.ndim

y = new_cyclist_trials.reshape(3,4)
y
y.ndim
new_cyclist_trials.resize(6,2)
new_cyclist_trials.ndim
new_cyclist_trials.shape

#flatten the dataset
print(new_cyclist_trials.ravel())
x = new_cyclist_trials.ravel()
x
y = x.reshape(3,4)
y
z = y.reshape(4,3)
z

#reshaping dataset
print(new_cyclist_trials.reshape(3,4))
print(new_cyclist_trials.reshape(4,3))
print(new_cyclist_trials.reshape(2,6))
new_cyclist_trials

#resize
new_cyclist_trials.resize(6,2)
new_cyclist_trials


#split array into 2
new_cyclist_trials = np.array([[10,15,17,26,13,19],[12,13,14,24,14,23]])
new_cyclist_trials
print(np.hsplit(new_cyclist_trials,2))

new_cyclist_1 = [10,15,17,26,13,19]
new_cyclist_2 = [12,13,14,24,14,23]

#stack the arrays together
print(np.hstack([new_cyclist_1,new_cyclist_2]))



