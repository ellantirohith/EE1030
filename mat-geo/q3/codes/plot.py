import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# Load the shared library
lib = ctypes.CDLL('./libvector_data.so')

# Define the return type of the function (pointer to double)
lib.generate_vector_data.restype = ctypes.POINTER(ctypes.c_double)

# Define the argument types for the function
lib.generate_vector_data.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]

# Python function to call the C function and get the points
def generate_vector_data(x, y, z, num_points):
    # Call the C function, which returns a pointer to the array
    output_ptr = lib.generate_vector_data(x, y, z, num_points)

    # Convert the pointer into a numpy array (num_points * 3 for x, y, z components)
    output_array = np.ctypeslib.as_array(output_ptr, shape=(num_points * 3,))

    # Reshape the array to have dimensions (num_points, 3) for x, y, z components
    points = output_array.reshape(num_points, 3)

    return points

# Example usage
x, y, z = 3.0, 3.0, 3.0  # Vector components
num_points = 1000  # Number of points to generate

# Call the function to get the points directly as an array
points = generate_vector_data(x, y, z, num_points)
# Configure LaTeX rendering in Matplotlib
plt.rcParams['text.usetex'] = True

# Plot the data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vector path with black color
ax.plot(points[:, 0], points[:, 1], points[:, 2], color='black', label=r'Vector $\vec{r}$')

# Draw the arrow at the end of the vector with black color
start_point = [0, 0, 0]
end_point = [3, 3, 3]
ax.quiver(start_point[0], start_point[1], start_point[2], 
          end_point[0] - start_point[0], 
          end_point[1] - start_point[1], 
          end_point[2] - start_point[2], 
          color='black', 
          arrow_length_ratio=0.05)

# Function to plot the circumference of an arc
def plot_arc(ax, center, start_vec, axis_vec, radius, theta_start, theta_end, color):
    theta = np.linspace(theta_start, theta_end, 100)
    x = center[0] + radius * np.cos(theta) * start_vec[0] + radius * np.sin(theta) * axis_vec[0]
    y = center[1] + radius * np.cos(theta) * start_vec[1] + radius * np.sin(theta) * axis_vec[1]
    z = center[2] + radius * np.cos(theta) * start_vec[2] + radius * np.sin(theta) * axis_vec[2]
    ax.plot(x, y, z, color=color)

# Define the radius for the arcs and angles for each axis
arc_radius = 1
theta_start = 0
theta_end =(np.pi / 3)*1.55  # 60 degrees arc, roughly corresponding to ~54.74 degrees

# Plot arcs between the vector and the axes
plot_arc(ax, center=[0, 0, 0], start_vec=[1, 0, 0], axis_vec=[0.578, 0.578, 0.578], radius=arc_radius, theta_start=theta_start, theta_end=theta_end, color='red')  # X axis arc
plot_arc(ax, center=[0, 0, 0], start_vec=[0, 1, 0], axis_vec=[0.578, 0.578, 0.578], radius=arc_radius, theta_start=theta_start, theta_end=theta_end, color='green')  # Y axis arc
plot_arc(ax, center=[0, 0, 0], start_vec=[0, 0, 1], axis_vec=[0.578, 0.578, 0.578], radius=arc_radius, theta_start=theta_start, theta_end=theta_end, color='blue')  # Z axis arc

ax.text(1.5, 0, 0, r'$\theta_X = \cos^{-1}\left(\frac{1}{\sqrt{3}}\right) $', color='red', fontsize=12)  # Angle with X axis
ax.text(0, 1.5, 0, r'$\theta_Y = \cos^{-1}\left(\frac{1}{\sqrt{3}}\right) $', color='green', fontsize=12)  # Angle with Y axis
ax.text(0, 0, 1.5, r'$\theta_Z = \cos^{-1}\left(\frac{1}{\sqrt{3}}\right) $', color='blue', fontsize=12)  # Angle with Z axis

# Draw the axes as lines
ax.plot([0, 4], [0, 0], [0, 0], color='red', linestyle='--', label=r'X axis')  # X axis
ax.plot([0, 0], [0, 4], [0, 0], color='green', linestyle='--', label=r'Y axis')  # Y axis
ax.plot([0, 0], [0, 0], [0, 4], color='blue', linestyle='--', label=r'Z axis')  # Z axis

# Labeling the plot
ax.set_xlabel(r'X axis', color='black')
ax.set_ylabel(r'Y axis', color='black')
ax.set_zlabel(r'Z axis', color='black')
ax.legend()

# Set title with black color
plt.title(r'Vector $\vec{r}$ and Angles with Axes', color='black')

# Show the plot
plt.show()

