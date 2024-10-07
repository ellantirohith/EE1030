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


typedef struct {
    double V[2][2];  
    double U[2];    
    double f;        
} Conic1, Conic2;


void solve_conic_intersection(double* x_vals, double* y_vals,  Conic1* conic1, Conic2* conic2,double a) {
    
    double A1 = conic1->V[0][0]; 
    double B1 = 2 * conic1->U[0];
    double C1 = conic1->f;      
    
    double A2 = conic2->V[0][0];  
    double B2 = 2 * conic2->U[0]; 
    double C2 = conic2->f;        
    
    
    double discriminant = (B1 - B2) * (B1 - B2) - 4 * (A1 - A2) * (C1 - C2);
    
    if (discriminant < 0) {
        
        return;
    }
    
 
    x_vals[0] = (-B1 + B2 + sqrt(discriminant)) / (2 * (A1 - A2)); 
    x_vals[1] = (-B1 + B2 - sqrt(discriminant)) / (2 * (A1 - A2)); 
    x_vals[2]=x_vals[0];
    x_vals[3]=x_vals[1];
  y_vals[0]=sqrt(6*a*x_vals[0]);
y_vals[1]=sqrt(6*a*x_vals[1]);
y_vals[2]=-sqrt(6*a*x_vals[2]);
y_vals[3]=-sqrt(6*a*x_vals[3]);
    
  
}


