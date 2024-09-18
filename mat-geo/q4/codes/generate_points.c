#include <stdlib.h>

// Structure to store a point with x and y coordinates
typedef struct {
    double x;
    double y;
} Point;

// Function to generate a continuous point on a line between two vertices based on parameter t
void generate_continuous_point(double x1, double y1, double x2, double y2, double t, double *x, double *y) {
    *x = (1 - t) * x1 + t * x2;  // Linear interpolation
    *y = (1 - t) * y1 + t * y2;
}

// Function to generate continuous points on triangle sides and return them as an array
Point* generate_triangle_points(int num_points) {
    // Vertices of the triangle
    double x1 = 1.161, y1 = 0.671;
    double x2 = 0.0, y2 = 0.0;
    double x3 = 6.0, y3 = 0.0;

    // Allocate memory for the points array (num_points * 3 points in total)
    Point* points = (Point*)malloc(sizeof(Point) * num_points * 3);

    double x, y;
    int index = 0;

    for (int i = 0; i < num_points; i++) {
        double t = (double)i / (num_points - 1);  // Parameter t to space the points evenly

        // Generate a continuous point on side 1 (x1, y1) to (x2, y2)
        generate_continuous_point(x1, y1, x2, y2, t, &x, &y);
        points[index].x = x;
        points[index].y = y;
        index++;

        // Generate a continuous point on side 2 (x2, y2) to (x3, y3)
        generate_continuous_point(x2, y2, x3, y3, t, &x, &y);
        points[index].x = x;
        points[index].y = y;
        index++;

        // Generate a continuous point on side 3 (x3, y3) to (x1, y1)
        generate_continuous_point(x3, y3, x1, y1, t, &x, &y);
        points[index].x = x;
        points[index].y = y;
        index++;
    }

    return points;
}

// Function to free the allocated memory for the points array
void free_points(Point* points) {
    free(points);
}

