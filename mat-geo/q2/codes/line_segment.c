#include <stdio.h>

#define NUM_POINTS 1000

// Function to fill an array with points of a line segment
void get_line_segment(float *points) {
    float x1 = 0.0f;
    float y1 = 6.0f;
    float x2 = 0.0f;
    float y2 = -2.0f;

    float dx = (x2 - x1) / (NUM_POINTS - 1);
    float dy = (y2 - y1) / (NUM_POINTS - 1);

    for (int i = 0; i < NUM_POINTS; ++i) {
        points[2 * i] = x1 + i * dx; // X coordinate
        points[2 * i + 1] = y1 + i * dy; // Y coordinate
    }
}



