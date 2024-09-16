#include <stdlib.h>

// Function to generate vector data and return a pointer to the array
double* generate_vector_data(double x, double y, double z, int num_points) {
    // Allocate memory for num_points * 3 (for x, y, z components)
    double *output = (double *)malloc(num_points * 3 * sizeof(double));
    if (output == NULL) {
        return NULL;  // Return NULL if memory allocation fails
    }

    // Generate points along the vector
    for (int i = 0; i < num_points; ++i) {
        double t = (double)i / (num_points - 1);  // Parameter to vary from 0 to 1
        output[3 * i] = t * x;     // x component
        output[3 * i + 1] = t * y; // y component
        output[3 * i + 2] = t * z; // z component
    }

    return output;  // Return the pointer to the array
}

