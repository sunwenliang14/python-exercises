import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
mask = a < 0
mask.sum()

mask = a > 0
mask.sum()

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
b = a + 3
mask = b > 0
mask.sum()

c = a**2
c.mean()

c.std()

d = a - a.mean()

z = (a - a.mean())/a.std()

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sum_of_a = a.sum()
sum_of_a

min_of_a = a.min()
min_of_a

max_of_a = a.max()
max_of_a

mean_of_a = a.mean()
mean_of_a

product_of_a = a.prod()
product_of_a

squares_of_a = a**2
squares_of_a

odds_in_a = a[a % 2 == 1]
odds_in_a

evens_in_a = a[a % 2 == 0]
evens_in_a

b = np.array([[3, 4, 5],[6, 7, 8]])
b.sum()

b.min()

b.max()

b.mean()

b.prod()

b**2

b.shape

b = np.array([[3, 4, 5],[6, 7, 8]])
b.T

b.flatten()

b.reshape(6, 1)

c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Exercise 1 - Find the min, max, sum, and product of c.
c.min(), c.max(), c.sum(), c.prod()

# Exercise 2 - Determine the standard deviation of c.
c.std()

# Exercise 3 - Determine the variance of c.
c.std() ** 2

# Exercise 4 - Print out the shape of the array c
c.shape

# Exercise 5 - Transpose c and print out transposed result.
c.T

# Exercise 6 - Get the dot product of the array c with c.
c.dot(c)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
(c * c.T).sum()

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
(c * c.T).prod()


## Setup 4
d = [[90, 30, 45, 0, 120, 180], [45, -90, -30, 270, 90, 0], [60, 45, -45, 90, -45, 180]]

d = np.array(d)

# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)

# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)

# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)

# Exercise 4 - Find all the negative numbers in d
d[d < 0]

# Exercise 5 - Find all the positive numbers in d
d[d > 0]

# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)

# Exercise 7 - Determine how many unique numbers there are in d.
np.unique(d).size

# Exercise 8 - Print out the shape of d.
d.shape

# Exercise 9 - Transpose and then print out the shape of d.
d.T.shape

# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(9, 2)
