import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./generate_points.so")  # Use .dll for Windows, .so for Linux/Mac

# Define the Point structure to match the C structure
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

# Define the function's argument and return types
lib.generate_triangle_points.restype = ctypes.POINTER(Point)
lib.generate_triangle_points.argtypes = [ctypes.c_int, Point, Point, Point]

# Define the number of points and vertices of the triangle
num_points = 9999
v1 = Point(1.161, 0.671)
v2 = Point(0.0, 0.0)
v3 = Point(6.0, 0.0)

# Call the C function to generate the points
points = lib.generate_triangle_points(num_points, v1, v2, v3)

# Extract the points into Python lists
x_coords = [points[i].x for i in range(num_points * 3)]
y_coords = [points[i].y for i in range(num_points * 3)]

# Free the allocated memory in C
lib.free_points(points)

# Plot the points using matplotlib
plt.figure(figsize=(6, 6))
plt.scatter(x_coords, y_coords, color='lightblue', s=5)  # Plot points as small blue dots

# Annotate the vertices A, B, C
plt.text(v1.x, v1.y, 'A', fontsize=20, ha='right', color='green')
plt.text(v2.x, v2.y, 'B', fontsize=20, ha='right', color='green')
plt.text(v3.x, v3.y, 'C', fontsize=20, ha='right', color='green')

# Annotate the sides
mid_ab = ((v1.x + v2.x) / 2, (v1.y + v2.y) / 2)
mid_bc = ((v2.x + v3.x) / 2, (v2.y + v3.y) / 2)
mid_ca = ((v3.x + v1.x) / 2, (v3.y + v1.y) / 2)

plt.text(mid_ab[0], mid_ab[1], 'c', fontsize=20, ha='center', color='blue')
plt.text(mid_bc[0], mid_bc[1], 'a', fontsize=20, ha='center', color='blue')
plt.text(mid_ca[0], mid_ca[1], 'b', fontsize=20, ha='center', color='blue')

# Plot triangle sides
plt.fill([v1.x, v2.x, v3.x], [v1.y, v2.y, v3.y], 'lightblue', alpha=0.5)

# Set plot labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Triangle ABC")
plt.grid(True)
plt.axis("equal")

# Show the plot
plt.show()

