
import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./libline_segment.so')  

# Define the argument and return types of the shared library function
lib.get_line_segment.argtypes = [ctypes.POINTER(ctypes.c_float)]

# Number of points
NUM_POINTS = 1000

# Create a buffer to hold the points
points = (ctypes.c_float * (2 * NUM_POINTS))()

# Call the function
lib.get_line_segment(points)

# Extract points from ctypes buffer
points_np = np.array(points[:], dtype=np.float32).reshape((NUM_POINTS, 2))

# Separate the points into X and Y coordinates
x = points_np[:, 0]
y = points_np[:, 1]
label_color = 'black'

# Define points
points = {'A (0, 6)': (0, 6), 'B (0, -2)': (0, -2)}

# Plot the line segment
plt.plot(x, y, marker='o', color='black')  # Color of the line segment

# Add labels for each point using plot
for point, coord in points.items():
    plt.plot(*coord, 'o', color=label_color, markersize=10)  # Mark points
    plt.text(coord[0], coord[1], f' {point}', color=label_color, fontsize=16)

# Set the limits of the axes
plt.xlim(-1, 1)
plt.ylim(-4, 8)

# Set labels and title
plt.title(f'Line Segment from (0, 6) to (0, -2)')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

