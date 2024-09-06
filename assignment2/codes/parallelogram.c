// parallelogram.c
#include <stdlib.h>

typedef struct {
    double x;
    double y;
} Point;

void get_parallelogram_points(Point *points) {
    points[0].x = 1.0; points[0].y = 2.0; // Point A
    points[1].x = 4.0; points[1].y = 3.0; // Point B
    points[2].x = 6.0; points[2].y = 6.0; // Point C
    points[3].x = 3.0; points[3].y = 5.0; // Point D
}

