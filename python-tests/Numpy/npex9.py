marks = np.array([[23,34,45,56],[23,23,34,67]])
marks
marks.transpose()
marks.reshape(4,2)

marks = np.array([[23,34],[23,23]])
marks
from numpy import linalg
np.linalg.inv(marks)

np.trace(marks)