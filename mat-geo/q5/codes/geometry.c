#include <math.h>
#include <stdio.h>

// Function to generate points for the parabola y^2 = ax
void generate_parabola(double* x_vals, double* y_vals, int num_points, double x_min, double x_max, double a) {
    double step = (x_max - x_min) / (num_points - 1);
    for (int i = 0; i < num_points; i++) {
        x_vals[i] = x_min + i * step;
        y_vals[i] = sqrt(a * x_vals[i]);  // Parabola equation y^2 = ax
    }
}

// Function to generate points for the circle x^2 + y^2 = r^2
void generate_circle(double* x_vals, double* y_vals, int num_points, double r) {
    double theta_step = 2 * M_PI / num_points;
    for (int i = 0; i < num_points; i++) {
        double theta = i * theta_step;
        x_vals[i] = r * cos(theta);
        y_vals[i] = r * sin(theta);
    }
}

// Function to solve the intersection points between parabola y^2 = ax and circle x^2 + y^2 = r^2
void solve_intersection(double* x_vals, double* y_vals, int* num_intersections, double a, double r) {
    double b = a;
    double c = -r * r;  // Circle equation x^2 + y^2 = r^2
    
    // Calculate discriminant for the quadratic equation
    double discriminant = b * b - 4 * c;
    
    if (discriminant < 0) {
        *num_intersections = 0;
        return;
    }

    // Calculate both solutions for x
    double x1 = (-b + sqrt(discriminant)) / 2;
    double x2 = (-b - sqrt(discriminant)) / 2;
    
    // Calculate corresponding y values using y^2 = ax
    x_vals[0] = x1;
    y_vals[0] = sqrt(a * x1);
    
    x_vals[1] = x1;
    y_vals[1] = -sqrt(a * x1);  // Negative root
    
    x_vals[2] = x2;
    y_vals[2] = sqrt(a * x2);
    
    x_vals[3] = x2;
    y_vals[3] = -sqrt(a * x2);  // Negative root
    
    *num_intersections = 4;
}

