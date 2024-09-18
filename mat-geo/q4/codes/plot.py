import ctypes
from ctypes import Structure, POINTER, c_double, c_int
import matplotlib.pyplot as plt

# Define a Python equivalent for the C struct `Point`
class Point(Structure):
    _fields_ = [("x", c_double),
                ("y", c_double)]

# Load the shared library (adjust the file path if necessary)
triangle_lib = ctypes.CDLL("./libtriangle_points.so")  # Use ".dll" if on Windows

# Set the return type and argument types for the functions in the shared library
triangle_lib.generate_triangle_points.restype = POINTER(Point)  # Returns a pointer to Point
triangle_lib.generate_triangle_points.argtypes = [c_int]  # Takes one int argument (number of points)

triangle_lib.free_points.argtypes = [POINTER(Point)]  # Free function takes pointer to Point array

# Call the C function to generate the points
num_points = 9999  # Number of continuous points to generate on each triangle side
points_ptr = triangle_lib.generate_triangle_points(num_points)

# Convert the returned C array into a Python list
points = [(points_ptr[i].x, points_ptr[i].y) for i in range(num_points * 3)]  # 3 points per triangle side

# Free the allocated memory in C after we're done with it
triangle_lib.free_points(points_ptr)

# Extract x and y coordinates
x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]
A = (1.161, 0.671)
B = (0.0, 0.0)
C = (6.0, 0.0)
# Compute midpoints of the triangle sides to place the labels for sides a, b, and c
mid_ab = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)  # Midpoint of side AB
mid_bc = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)  # Midpoint of side BC
mid_ca = ((C[0] + A[0]) / 2, (C[1] + A[1]) / 2)  # Midpoint of side CA


plt.figure(figsize=(6, 6))
plt.scatter(x_coords, y_coords, color='lightblue', s=5)  # Plot points as small blue dots

# Annotate the vertices A, B, C
plt.text(A[0], A[1], 'A', fontsize=20, ha='right', color='green')
plt.text(B[0], B[1], 'B', fontsize=20, ha='right', color='green')
plt.text(C[0], C[1], 'C', fontsize=20, ha='right', color='green')
# Annotate the sides with 'a', 'b', 'c'
plt.text(mid_bc[0], mid_bc[1], 'a', fontsize=20, ha='center', color='blue')  # Side a (between B and C)
plt.text(mid_ca[0], mid_ca[1], 'b', fontsize=20, ha='center', color='blue')  # Side b (between C and A)
plt.text(mid_ab[0], mid_ab[1], 'c', fontsize=20, ha='center', color='blue')  # Side c (between A and B)

plt.fill([A[0], B[0], C[0]], [A[1], B[1], C[1]], 'lightblue',alpha=0.5)




# Set plot labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Triangle ABC")
plt.grid(True)
plt.axis("equal")

# Show the plot
plt.show()

