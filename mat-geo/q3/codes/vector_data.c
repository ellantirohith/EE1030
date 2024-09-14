
#include <stdio.h>
#include <stdlib.h>

// Function to generate data for plotting
void generate_vector_data(const char *filename, int num_points) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        perror("Unable to open file");
        exit(EXIT_FAILURE);
    }

    // Vector components
    double ix = 3.0;
    double jy = 3.0;
    double kz = 3.0;

    // Generate points along the vector
    for (int i = 0; i < num_points; ++i) {
        double t = (double)i / (num_points - 1);  // Parameter to vary from 0 to 1
        fprintf(file, "%f %f %f\n", t * ix, t * jy, t * kz);
    }

    fclose(file);
}


