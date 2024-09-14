import matplotlib.pyplot as plt
import numpy as np
import ctypes
from mpl_toolkits.mplot3d import Axes3D

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

# Plot the vector path with black color
ax.plot(data[:, 0], data[:, 1], data[:, 2], color='black', label=r'Vector $\vec{r}$')

# Draw the arrow at the end of the vector with black color
start_point = [0, 0, 0]
end_point = [3, 3, 3]
ax.quiver(start_point[0], start_point[1], start_point[2], 
          end_point[0] - start_point[0], 
          end_point[1] - start_point[1], 
          end_point[2] - start_point[2], 
          color='black', 
          arrow_length_ratio=0.05)  # Adjust this value to control the arrow size
          
# Labeling the plot
ax.set_xlabel(r'X axis', color='black')
ax.set_ylabel(r'Y axis', color='black')
ax.set_zlabel(r'Z axis', color='black')
ax.legend()

# Set title with black color
plt.title(r'Vector $\vec{r}$', color='black')

# Show the plot
plt.show()

