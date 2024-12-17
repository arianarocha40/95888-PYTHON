"""
@author: arian
Andrew ID: afrocha
Name: Ariana Rocha
Data Focused Python hw3.1 -- SECTION 4
Basically did the HW1 thing on chapter 4 to satisfy this requirement
"""
# CHAPTER 4: NumPy Basics: Array and Vectorized Computation

import numpy as np

my_arr = np.arange(1_000_000)

my_list = list(range(1_000_000))

## 4.1 The NumPy ndarray: A Multidimensional Array Object
# Create a small array
data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])

# Multiply all elements by 10
data10 = data * 10

# Add data to itself
data2 = data + data

# Check the shape of the array
dataShape = data.shape

# Check the data type of the array
dataType = data.dtype

print("4.1 The NumPy ndarray: A Multidimensional Array Object\n",data,data10,data2,dataShape,dataType)

##Creating ndArrays
# Create a 1D array from a list
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

# Create a 2D array from nested lists
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)

# Check dimensions of arr2
dim = arr2.ndim

# Check shape of arr2
shape = arr2.shape

# Check data types of arr1 and arr2
Dtype1 = arr1.dtype

Dtype2 = arr2.dtype

print("Creating ndArrays\n", arr1, arr2, dim, shape, Dtype1, Dtype2)

##Creating Arrays with zeros, ones, empty
# Create a 1D array of zeros
NP0 = np.zeros(10)

# Create a 2D array of zeros
NP1 = np.zeros((3, 6))

# Create an uninitialized array
NP2 = np.empty((2, 3, 2))

# Create a 1D array with `arange`
NP3 = np.arange(15)

print("Creating Arrays with zeros, ones, empty\n", NP0,NP1,NP2)

##Data Types for ndarrays
# Explicitly convert data type during array creation
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)

# Check data types of arrays
arr1type = arr1.dtype

arr2type = arr2.dtype
print("Data Types for ndarrays\n",arr1, arr2,arr1type,arr2type)


##Arithmetic with NumPy Arrays
# Element-wise multiplication of two arrays
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
Xarr = arr * arr

# Subtraction
Sarr = arr - arr

# Scalar division
Darr = 1 / arr

# Scalar exponentiation
Earr = arr ** 2

print("Arithmetic with NumPy Arrays\n", arr, Xarr, Sarr, Darr, Earr)

##Basic Indexing and Slicing
# 1D array slicing
arr = np.arange(10)
arr5 = arr[5]

# Slice of 1D array
arr58 = arr[5:8]

# Modify array slice
arr5812 = arr[5:8] = 12

# 2D array indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d2 = arr2d[2]

# Access element at row 0, column 2
arr202 = arr2d[0, 2]

# Slice along first axis
arr2_2 = arr2d[:2]

# Slice along both axes
arr2d21 = arr2d[:2, 1:]

print("Basic Indexing and Slicing\n", arr, arr5, arr58, arr5812, arr2d, arr2d2, arr202, arr202, arr2_2, arr2d21)

##Boolean Indexing python
# Create arrays for Boolean indexing example
names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
data = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2], [-12, -4], [3, 4]])

# Select rows where names == "Bob"
Bob = data[names == "Bob"]

# Select rows where names != "Bob"
NotBob = data[names != "Bob"]

# Use a Boolean condition for filtering data
ZeroData = data[data < 0] = 0
print("Boolean Indexing python\n",names, data, Bob, NotBob, ZeroData )


##Fancy Indexing python
# Create an 8x4 array and assign rows
arr = np.zeros((8, 4))
for i in range(8):
    arr[i] = i

# Select specific rows
rowSelect = arr[[4, 3, 0, 6]]

# Negative indices
NegIndices = arr[[-3, -5, -7]]


##Transposing Arrays and Swapping Axes python
# Create an array and transpose it
arr15 = np.arange(15).reshape((3, 5))
transArr = arr.T

# Matrix product
arr = np.array([[0, 1, 0], [1, 2, -2], [6, 3, 2], [-1, 0, -1], [1, 0, 1]])
np.dot(arr.T, arr)
print("Fancy Indexing pythonn\n", arr, rowSelect, NegIndices,arr15, transArr, arr)

##4.2 Pseudorandom Number Generation
from random import normalvariate

# Create a 4x4 array of samples from the standard normal distribution
samples = np.random.standard_normal(size=(4, 4))

# Measure the time to generate 1,000,000 random numbers with Python's built-in random module
N = 1_000_000

# Generate random numbers using the normalvariate function
%timeit samples_python = [normalvariate(0, 1) for _ in range(N)]

# Measure the time to generate random numbers using numpy's standard_normal function
%timeit samples_numpy = np.random.standard_normal(N)

# Create a random number generator with a fixed seed
rng = np.random.default_rng(seed=12345)

# Generate a 2x3 array of standard normal samples using the new random generator
data_rng = rng.standard_normal((2, 3))

# Print section
print("\n4.2 Pseudorandom Number Generation")
print("samples:\n", samples)
print("\nRandom generator (rng) data:\n", data_rng)

## 4.3 Universal Functions: Fast Element-Wise Array Functions
# Create an array from 0 to 9
arr = np.arange(10)

# Compute square root and exponent of the array
sqrt_arr = np.sqrt(arr)
exp_arr = np.exp(arr)

# Generate two sets of random numbers
x = rng.standard_normal(8)
y = rng.standard_normal(8)

# Compute the element-wise maximum of x and y
max_xy = np.maximum(x, y)

# Break down an array into fractional and whole parts
arr_rand = rng.standard_normal(7) * 5
frac_part, whole_part = np.modf(arr_rand)

# Output the results using a print section
print("\n4.3 Universal Functions: Fast Element-Wise Array Functions")
print("Array (arr):", arr)
print("Square root of arr:", sqrt_arr)
print("Exponential of arr:", exp_arr)
print("\nRandom arrays x and y:\n", x, "\n", y)
print("Element-wise maximum of x and y:", max_xy)
print("\nRandom array (arr_rand):", arr_rand)
print("Fractional part of arr_rand:", frac_part)
print("Whole part of arr_rand:", whole_part)

##Array-Oriented Programming with Arrays
# Create a grid of points using numpy.meshgrid
points = np.arange(-5, 5, 0.01)  # 1000 equally spaced points
xs, ys = np.meshgrid(points, points)

# Evaluate the function sqrt(x^2 + y^2) across the grid
z = np.sqrt(xs ** 2 + ys ** 2)

# Use matplotlib to visualize the result
import matplotlib.pyplot as plt

plt.imshow(z, cmap=plt.cm.gray, extent=[-5, 5, -5, 5])
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()

# Print section
print("\n4.4 Array-Oriented Programming with Arrays")
print("Points grid (xs):", xs)
print("Points grid (ys):", ys)
print("\nEvaluated function (z):", z)

##File Input and Output with Arrays
# Create a simple array
arr = np.arange(10)

# Save the array to a .npy file
np.save("some_array", arr)

# Load the array back from the file
loaded_arr = np.load("some_array.npy")

# Save multiple arrays in an uncompressed archive
np.savez("array_archive.npz", a=arr, b=arr)

# Load from the archive
arch = np.load("array_archive.npz")
a_loaded = arch["a"]
b_loaded = arch["b"]

# Save compressed arrays
np.savez_compressed("arrays_compressed.npz", a=arr, b=arr)

# Print section
print("\n4.5 File Input and Output with Arrays")
print("Original array:", arr)
print("Loaded array from .npy:", loaded_arr)
print("Loaded arrays from archive (a):", a_loaded)
print("Loaded arrays from archive (b):", b_loaded)

##4.5 File Input and Output with Arrays
arr = np.arange(10)
np.save("some_array", arr)
loaded_arr = np.load("some_array.npy")
np.savez("array_archive.npz", a=arr, b=arr)
arch = np.load("array_archive.npz")
a_loaded = arch["a"]
b_loaded = arch["b"]
np.savez_compressed("arrays_compressed.npz", a=arr, b=arr)

print("\n4.5 File Input and Output with Arrays")
print("Original array:", arr)
print("Loaded array from .npy:", loaded_arr)
print("Loaded arrays from archive (a):", a_loaded)
print("Loaded arrays from archive (b):", b_loaded)

##4.6 Linear Algebra
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1., 7.], [8., 9.]])
dot_product = x.dot(y)
one_d_result = x @ np.ones(3)

from numpy.linalg import inv, qr
X = np.random.default_rng(seed=12345).standard_normal((5, 5))
mat = X.T @ X
inv_mat = inv(mat)
product_check = mat @ inv_mat

print("\n4.6 Linear Algebra")
print("x:\n", x)
print("y:\n", y)
print("Dot product of x and y:\n", dot_product)
print("Matrix product with ones:\n", one_d_result)
print("Matrix X.T @ X:\n", mat)
print("Inverse of matrix:\n", inv_mat)
print("Check mat @ inv(mat):\n", product_check)

## 4.7EX: Random Walks
# Single random walk with 1000 steps
nsteps = 1000
rng = np.random.default_rng(seed=12345)  
draws = rng.integers(0, 2, size=nsteps)
steps = np.where(draws == 0, 1, -1)
walk = steps.cumsum()
min_walk = walk.min()
max_walk = walk.max()
first_crossing = (np.abs(walk) >= 10).argmax()

# Simulating many random walks
nwalks = 5000
draws_multiple = rng.integers(0, 2, size=(nwalks, nsteps))
steps_multiple = np.where(draws_multiple > 0, 1, -1)
walks = steps_multiple.cumsum(axis=1)
max_walks = walks.max()
min_walks = walks.min()

# Find the crossing time for walks hitting 30 or -30
hits30 = (np.abs(walks) >= 30).any(axis=1)
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(axis=1)
avg_crossing_time = crossing_times.mean()

print("\n4.7 Example: Random Walks")
print("Single random walk: min =", min_walk, ", max =", max_walk)
print("First crossing time of 10 or -10:", first_crossing)
print("Multiple random walks: max =", max_walks, ", min =", min_walks)
print("Number of walks hitting 30 or -30:", hits30.sum())
print("Average crossing time for 30 or -30:", avg_crossing_time)

##4.8 Conclusion
print("Finally done with Ch4 NumPy Basics!")
