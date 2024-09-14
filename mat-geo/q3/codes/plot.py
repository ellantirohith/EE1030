import matplotlib.pyplot as plt
import numpy as np
import ctypes

# Load the shared library
lib = ctypes.CDLL('./libvector_data.so')

# Define the argument types for the function
lib.generate_vector_data.argtypes = [ctypes.c_char_p, ctypes.c_int]

# Specify the filename and number of points
filename = 'vector_data.txt'
num_points = 1000

# Call the C function to generate data
lib.generate_vector_data(filename.encode('utf-8'), num_points)

# Read the data from the file
data = np.loadtxt(filename)

# Configure LaTeX rendering in Matplotlib
plt.rcParams['text.usetex'] = True

# Plot the data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vector path
ax.plot(data[:, 0], data[:, 1], data[:, 2], label=r'Vector $\vec{r}$')

# Plot the endpoint of the vector
ax.scatter([3], [3], [3], color='red', label=r'Endpoint of $\vec{r}$')

# Labeling the plot
ax.set_xlabel(r'X axis')
ax.set_ylabel(r'Y axis')
ax.set_zlabel(r'Z axis')
ax.legend()

# Show the plot
plt.title(r'Vector $\vec{r}$')
plt.show()

