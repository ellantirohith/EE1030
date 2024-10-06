import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./libgeometry.so')

# Define the argument and return types for the C functions
lib.generate_parabola.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                  ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.generate_circle.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                ctypes.c_int, ctypes.c_double]
lib.solve_intersection.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                   ctypes.POINTER(ctypes.c_int), ctypes.c_double]

# Parameters
num_points = 1000
x_min, x_max = 0, 20

# Get the value of 'a' for the parabola equation y^2 = ax and 'r' for the circle x^2 + y^2 = r^2 from the user
a = float(input("Enter the value of 'a' for the parabola equation y^2 = 6ax: "))

# Allocate memory for the x and y arrays for the parabola
x_parabola = np.zeros(num_points, dtype=np.float64)
y_parabola = np.zeros(num_points, dtype=np.float64)

# Call the C function to generate the parabola
lib.generate_parabola(x_parabola.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                      y_parabola.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                      num_points, x_min, x_max, 6*a)

# Allocate memory for the x and y arrays for the circle
x_circle = np.zeros(num_points, dtype=np.float64)
y_circle = np.zeros(num_points, dtype=np.float64)

# Call the C function to generate the circle
lib.generate_circle(x_circle.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                    y_circle.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                    num_points, 4*a)

# Allocate memory for the intersection points
x_intersections = np.zeros(4, dtype=np.float64)
y_intersections = np.zeros(4, dtype=np.float64)
num_intersections = ctypes.c_int()

# Call the C function to solve for intersection points with the given 'a' and 'r'
lib.solve_intersection(x_intersections.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                       y_intersections.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                       ctypes.byref(num_intersections), a)

# Plotting
plt.figure()

# Plot the circle
plt.plot(x_circle, y_circle, label=f'Circle (r = 4a)', color='blue')

# Plot the parabola (both positive and negative y-values)
plt.plot(x_parabola, y_parabola, label=f'Parabola (y^2 = 6ax)', color='orange')
plt.plot(x_parabola, -y_parabola, color='orange')

# Highlight and label the intersection points
if num_intersections.value > 0:
    plt.scatter(x_intersections[:num_intersections.value], y_intersections[:num_intersections.value],
                color='red', zorder=5, label='Intersection Points')
    
    # Label each intersection point with custom format: (x = value a, y = 2√3 a)
    for i in range(num_intersections.value):
        label = r"$(x = 2a, y = \pm2\sqrt{{3}}a)$".format(x_intersections[i])
        plt.text(x_intersections[i], y_intersections[i] + 0.5, label, fontsize=12, color='black')

# Determine the points that are inside the circle for the shading
inside_circle = (x_parabola)**2 + (y_parabola)**2 <= (4*a)**2

# Fill the region between the parabola and the circle
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

