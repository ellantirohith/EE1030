import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./libgeometry.so')

# Define the argument and return types for the C functions
lib.generate_parabola.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                  ctypes.c_int, ctypes.c_double, ctypes.c_double]
lib.generate_circle.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                ctypes.c_int]

# Parameters
num_points = 1000
x_min, x_max = 0, 20

# Allocate memory for the x and y arrays
x_parabola = np.zeros(num_points, dtype=np.float64)
y_parabola = np.zeros(num_points, dtype=np.float64)

# Call the C function to generate the parabola
lib.generate_parabola(x_parabola.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                      y_parabola.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                      num_points, x_min, x_max)

# Allocate memory for the x and y arrays of the circle
x_circle = np.zeros(num_points, dtype=np.float64)
y_circle = np.zeros(num_points, dtype=np.float64)

# Call the C function to generate the circle
lib.generate_circle(x_circle.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                    y_circle.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                    num_points)

# Plotting
plt.figure()
plt.plot(x_circle, y_circle, label='Circle', color='blue')
plt.plot(x_parabola, y_parabola, label='Parabola', color='orange')
plt.plot(x_parabola, -y_parabola,  color='orange')
inside_circle = (x_parabola )**2 + (y_parabola )**2 <=4**2

# Fill the area between the two curves where the parabola is below the circle
plt.fill_between(x_parabola, y_parabola, 0,where = inside_circle,  color='green', alpha=0.5, label='Required Area')
plt.fill_between(x_parabola, -y_parabola, 0,where = inside_circle,  color='green', alpha=0.5 )
plt.fill_between(x_circle, y_circle, 0,where =x_circle>=2,  color='green', alpha=0.5 )



# Set aspect ratio to equal for proper scaling
plt.gca().set_aspect('equal', adjustable='box')

# Adding labels and title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Region Between the Parabola and Circle with Conditions")
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

