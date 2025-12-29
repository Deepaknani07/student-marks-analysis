import numpy as np

marks = np.array([78, 85, 92, 60, 74, 88, 90])


print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))


passed = marks[marks >= 75]
print("Passed Students Marks:", passed)


scaled_marks = marks + 5
print("Scaled Marks:", scaled_marks)
