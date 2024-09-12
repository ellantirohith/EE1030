// generate_data.c
#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

typedef struct {
    double x;
    double y;
} Point;

int main() {
    Point points[4];

    // Load the shared library
    void *handle = dlopen("./libparallelogram.so", RTLD_LAZY);
    if (!handle) {
        fprintf(stderr, "%s\n", dlerror());
        return EXIT_FAILURE;
    }

    // Get the function from the shared library
    void (*get_parallelogram_points)(Point *) = dlsym(handle, "get_parallelogram_points");
    if (!get_parallelogram_points) {
        fprintf(stderr, "%s\n", dlerror());
        dlclose(handle);
        return EXIT_FAILURE;
    }

    // Retrieve the points
    get_parallelogram_points(points);

    // Close the shared library
    dlclose(handle);

    // Write the points to a file for Python to read
    FILE *file = fopen("parallelogram.txt", "w");
    if (!file) {
        perror("fopen failed");
        return EXIT_FAILURE;
    }

    for (int i = 0; i < 4; ++i) {
        fprintf(file, "%f %f\n", points[i].x, points[i].y);
    }
    fclose(file);

    return EXIT_SUCCESS;
}

