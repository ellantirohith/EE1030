import ctypes
import numpy as np
import matplotlib.pyplot as plt
import math

# Load the shared library
lib = ctypes.CDLL('./geometry.so')

# Define the argument and return types for the C functions
lib.generate_parabola.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                  ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.generate_circle.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                ctypes.c_int, ctypes.c_double]

class Conic1(ctypes.Structure):
    _fields_ = [("V", ctypes.c_double * 2 * 2),  # 2x2 matrix
                ("U", ctypes.c_double * 2),      # 2-element vector
                ("f", ctypes.c_double)]          # Scalar

class Conic2(ctypes.Structure):
    _fields_ = [("V", ctypes.c_double * 2 * 2),  # 2x2 matrix
                ("U", ctypes.c_double * 2),      # 2-element vector
                ("f", ctypes.c_double)]          # Scalar

# Define the argument and return types for the C functions
lib.solve_conic_intersection.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                          ctypes.POINTER(Conic1), ctypes.POINTER(Conic2),ctypes.c_double]

# Parameters
num_points = 1000

# Initialize the Conic1 and Conic2 struct
conic1 = Conic1()
conic2 = Conic2()

# Taking user input for V matrix of Conic1
for i in range(2):
    for j in range(2):
        conic1.V[i][j] = float(input(f"Enter element V[{i}][{j}] of Conic1 V matrix: "))

# Taking user input for U vector of Conic1
for i in range(2):
    conic1.U[i] = float(input(f"Enter element U[{i}] of Conic1 U vector: "))

# Taking input for the scalar F of Conic1
conic1.f = float(input("Enter the scalar f for Conic1: "))

# Taking user input for V matrix of Conic2
for i in range(2):
    for j in range(2):
        conic2.V[i][j] = float(input(f"Enter element V[{i}][{j}] of Conic2 V matrix: "))

# Taking user input for U vector of Conic2
for i in range(2):
    conic2.U[i] = float(input(f"Enter element U[{i}] of Conic2 U vector: "))

# Taking input for the scalar F of Conic2
conic2.f = float(input("Enter the scalar f for Conic2: "))

# Allocate memory for the x and y arrays (intersection points)
x_vals = np.zeros(4, dtype=np.float64)
y_vals = np.zeros(4, dtype=np.float64)


# Get the value of 'a' for the parabola equation y^2 = 6ax and 'r' for the circle x^2 + y^2 = r^2 from the user
a = float(input("Enter the value of 'a' for the parabola equation y^2 = 6ax: "))
# Call the C function to solve the conic intersection problem
lib.solve_conic_intersection(x_vals.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                             y_vals.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                              ctypes.byref(conic1), ctypes.byref(conic2),a)


# Allocate memory for the x and y arrays for the parabola
x_parabola = np.zeros(num_points, dtype=np.float64)
y_parabola = np.zeros(num_points, dtype=np.float64)

# Call the C function to generate the parabola
lib.generate_parabola(x_parabola.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                      y_parabola.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                      num_points, 0, 20, 6*a)

# Allocate memory for the x and y arrays for the circle
x_circle = np.zeros(num_points, dtype=np.float64)
y_circle = np.zeros(num_points, dtype=np.float64)

# Call the C function to generate the circle
lib.generate_circle(x_circle.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                    y_circle.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                    num_points, 4*a)

# Print the intersection points
print(x_vals[0], y_vals[0], x_vals[1], y_vals[1], x_vals[2], y_vals[2], x_vals[3], y_vals[3])

# Plotting
plt.figure()

# Plot the circle
plt.plot(x_circle, y_circle, label=f'Circle (r = 4a)', color='blue')

# Plot the parabola (both positive and negative y-values)
plt.plot(x_parabola, y_parabola, label=f'Parabola (y^2 = 6ax)', color='orange')
plt.plot(x_parabola, -y_parabola, color='orange')
num_intersections = ctypes.c_int(4)

# Highlight and label the intersection points
if num_intersections.value > 0:
    plt.scatter(x_vals[:num_intersections.value], y_vals[:num_intersections.value],
                color='red', zorder=5, label='Intersection Points')

    # Label each intersection point with a format (x = value a, y = 2√3 a)
    for i in range(num_intersections.value):
        label = r"$(x = {:.2f}, y = {:.2f})$".format(x_vals[i], y_vals[i])
        plt.text(x_vals[i], y_vals[i] + 0.5, label, fontsize=12, color='black')

# Fill the region between the parabola and the circle
inside_circle = (x_parabola)**2 + (y_parabola)**2 <= (4*a)**2
plt.fill_between(x_parabola, y_parabola, 0, where=inside_circle, color='green', alpha=0.5, label='Shaded Area')
plt.fill_between(x_parabola, -y_parabola, 0, where=inside_circle, color='green', alpha=0.5)
plt.fill_between(x_circle, y_circle, 0, where=x_circle >= 2, color='green', alpha=0.5)

# Set aspect ratio to equal for proper scaling of the plot
plt.gca().set_aspect('equal', adjustable='box')

# Add labels, title, and legend
plt.xlabel("x")
plt.ylabel("y")
plt.title("Parabola and Circle Intersection with Labeled Points")
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

