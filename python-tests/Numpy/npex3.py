import numpy as np
first_trial_cyclist = [10,15,17,24]
second_trial_cyclist = [12,11,21,24]
np_first_trial_cyclist = np.array(first_trial_cyclist)
np_second_trial_cylist = np.array(second_trial_cyclist)
result = np_first_trial_cyclist+np_second_trial_cylist
print(result)

trials_new = np.array([first_trial_cyclist,second_trial_cyclist])
trials_new
trials_new.ndim
trials_new.dtype
trials_new[1:]
trials_new[:]
trials_new[:,0]
trials_new[:,1:3]
trials_new[:,1:3].shape

for n in trials_new[1:]:
    for j in n:
         print(j,n)

for n in trials_new:
    print(n)

for n in trials_new:
    for j in n:
         print(j,n)

trials_new
trials_sel = trials_new>17
trials_sel

trials_self = trials_new[trials_sel]
trials_self

trials_new
trials_sel
trials_self







