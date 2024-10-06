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
void solve_intersection(double* x_vals, double* y_vals, int* num_intersections, double a) {
    // Parameters for the parabola y^2 = 6ax
    double V1[2][2] = {{0, 0}, {0, 1}};
    double u1[2] = {-3 * a, 0};
    double f1 = 0;
    
    // Parameters for the circle x^2 + y^2 = r^2 (expressed as conic)
    double V2[2][2] = {{ 1, 0}, {0, 1}};
    double u2[2] = {0, 0};
    double f2 = -16 * a * a;
    
    // Subtract conic parameters: V1 - V2, u1 - u2, f1 - f2
    double V_diff[2][2] = {{V1[0][0] - V2[0][0], V1[0][1] - V2[0][1]},
                           {V1[1][0] - V2[1][0], V1[1][1] - V2[1][1]}};
    
    double u_diff[2] = {u1[0] - u2[0], u1[1] - u2[1]};
    double f_diff = f1 - f2;
    
    // Solving for the intersection points (quadratic equation solution)
    // The intersection equation is: V_diff * x^2 + 2 * u_diff * x + f_diff = 0
    // For simplicity, we assume a particular y and solve for x, or vice versa.

    // Example: Solving for x when y = 0
    double A = V_diff[0][0];  // Coefficient of x^2
    double B = 2 * u_diff[0]; // Coefficient of x
    double C = f_diff;        // Constant term
    
    // Discriminant of the quadratic equation
    double discriminant = B * B - 4 * A * C;
    
    if (discriminant < 0) {
        *num_intersections = 0;  // No real solutions
        return;
    }
    
    // Compute solutions for x
    double x1 = (-B + sqrt(discriminant)) / (2 * A);
    double x2 = (-B - sqrt(discriminant)) / (2 * A);
    
    // Corresponding y values using the parabola equation y^2 = 6ax
    x_vals[0] = x1;
    y_vals[0] = sqrt(6 * a * x1);
    
    x_vals[1] = x1;
    y_vals[1] = -sqrt(6 * a * x1);  // Negative root
    
    x_vals[2] = x2;
    y_vals[2] = sqrt(6 * a * x2);
    
    x_vals[3] = x2;
    y_vals[3] = -sqrt(6 * a * x2);  // Negative root
    
    *num_intersections = 4;  // Four intersection points
}

