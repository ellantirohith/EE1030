

#include <math.h>
#include <stdlib.h>

// Function to generate points for the parabola y^2 = 6x
// It returns an array of points (x, y)
void generate_parabola(double* x_vals, double* y_vals, int num_points, double x_min, double x_max) {
    double step = (x_max - x_min) / (num_points - 1);
    for (int i = 0; i < num_points; i++) {
        x_vals[i] = x_min + i * step;
        y_vals[i] = sqrt(6 * x_vals[i]);
    }
}

// Function to generate points for the circle x^2 + y^2 = 16
// It returns an array of points (x, y)
void generate_circle(double* x_vals, double* y_vals, int num_points) {
    double theta_step = 2 * M_PI / num_points;
    for (int i = 0; i < num_points; i++) {
        double theta = i * theta_step;
        x_vals[i] = 4 * cos(theta);
        y_vals[i] = 4 * sin(theta);
    }
}

