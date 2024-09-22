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
Point* generate_triangle_points(int num_points, Point v1, Point v2, Point v3) {
    // Allocate memory for the points array (num_points * 3 points in total)
    Point* points = (Point*)malloc(sizeof(Point) * num_points * 3);

    double x, y;
    int index = 0;

    for (int i = 0; i < num_points; i++) {
        double t = (double)i / (num_points - 1);  // Parameter t to space the points evenly

        // Generate a continuous point on side 1 (v1 to v2)
        generate_continuous_point(v1.x, v1.y, v2.x, v2.y, t, &x, &y);
        points[index].x = x;
        points[index].y = y;
        index++;

        // Generate a continuous point on side 2 (v2 to v3)
        generate_continuous_point(v2.x, v2.y, v3.x, v3.y, t, &x, &y);
        points[index].x = x;
        points[index].y = y;
        index++;

        // Generate a continuous point on side 3 (v3 to v1)
        generate_continuous_point(v3.x, v3.y, v1.x, v1.y, t, &x, &y);
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

