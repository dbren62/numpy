import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

# ROWS - grades for each student
# COLS - grades for each test

a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

print(grades)

g = grades.mean(axis=0)  # col by row
print("Average of each test:", g)

h = grades.mean(axis=1)
print("Average of each student:", h)

numbers = np.array([1, 4, 9, 16, 25, 36])

sqrt = np.sqrt(numbers)
print(sqrt)

numbers2 = np.arange(1, 7) * 10

add = np.add(numbers, numbers2)
print(add)

multiply = np.multiply(numbers2, 5)
print(multiply)

numbers3 = numbers2.reshape(2, 3)

numbers4 = np.array([2, 4, 6])

multiply2 = np.multiply(numbers3, numbers4)
print(multiply2)

"""This works because numbers4 has the same length as each row of numbers3,
so NumPy can apply the multiply operation by treating numbers4 as if it were the 
following array:

array([[2,4,6],
[2,4,6]]) """

# Indexing and Slicing

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

a = grades[0, 1]
print(a)
# 96

b = grades[1]
print(b)
# array([100, 87, 90])

# To select multiple sequential rows
# notation (remember upper limit is not included)
first_two = grades[0:2]
print(first_two)
# array([[87, 96, 70],
# [100, 87, 90]])

# To select multiple non-sequential rows, use a list of row indices:
k = grades[[1, 3]]
print(k)
# arry([[100, 87, 90],
# [100, 81, 82]])

# all rows and only first column
c = grades[:, 0]
print(c)

# You can select consectuve columns using a slice
d = grades[:, 1:3]
print(d)

# or specific columns using a list of column indices:
e = grades[:, [0, 2]]
print(e)

"""Use NumPy random-number generator to create an array of twelve random grades
in the range 60 through 100, then reshape the result into a 3-by-4 array.
Calculate the average of all the grades, the averages of the grades for each test
and the averages of the grades for each student."""

rand = np.array(np.random.randint(60, 101, 12).reshape(3, 4))
print(rand.mean())
print(rand.mean(axis=0))
print(rand.mean(axis=1))

# Shallow copies (view)
# The array method view returns a new array object with a view of the original array

numbers = np.arange(1, 6)

numbers2 = numbers.view()
print(numbers2)

numbers[1] *= 10
print(numbers2)

# Changing a value in the view also changes that value in the original array:
numbers2[1] /= 10

print(numbers)

# Slice Views
# Slices also create views. Let's make numbers2 a slice that views only the first
# three elements of the numbers:

numbers2 = numbers[0:3]
# to verify it is a view, lets modify an element in the original array and see
# the view array
numbers[1] *= 20

print(numbers2)
# array [1, 40, 3]

# Deep copies (copy)
# the array method copy returns a new array object with a deep
# copy of the original story
numbers = np.arange(1, 6)
numbers2 = numbers.copy()

# To prove that numbers2 has a seperate copy of the data in numbers, lets modify
# an element in numbers, then display both arrays:

numbers[1] *= 10
# array([1,20,3,4,5])

print(numbers2)
# array([1,2,3,4,5])

"""The array methods reshape and resize both enable you to change an array's dimension.
Method reshape returns a view (Shallow copy) pf the original array with the new
dimensions. It does not modify the original array."""

grades = np.array([[87, 96, 70], [100, 87, 90]])

a = grades.reshape(1, 6)
print(a)
print(grades)

b = grades.resize(1, 6)
print(grades)

# Method flatten deep copies the original array's data:

flattened = grades.flatten()

# alternatively, Method ravel produces a view (shallow copy) of the original array,
# which shares the grades array's data:
raveled = grades.ravel()

# confirm that they share the same data
raveled[0] = 100

raveled[5] = 99

# since it is a view and they share the same data, we can look at grades to see
# that the 6th element has been updated
print(grades)

# You can quickly transpose an array's rows and columns - that is, "flip" the array,
# so that rows become the columns and the columns become the rows. The T attribute
# returns a transposed view (shallow copy) of the array.

transposed = grades.T
print(transposed)


# You can combine arrays by adding more columns or more rows - known as
# horizontal stacking and vertical stacking.

# HSTACK
# Let's assume grades2 represents three additional exam grades for the
# two students in the grades array.

grades = np.array([[87, 96, 70], [100, 87, 90]])
grades2 = np.array([[94, 77, 90], [100, 81, 82]])

# we can combine grades and grades2 with NumPy's hstack
h_grades = np.hstack((grades, grades2))

# new array
print(h_grades)

# old array is not affected
print(grades)

# VSTACK

# lets assume that grades2 represents twp more students' grades on three exams.
v_grades = np.vstack((grades, grades2))
print(v_grades)