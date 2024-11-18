
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
typedef struct {
	int size;
	 complex double ** matrix;
} mat;



mat* newmat(int m) {
    mat *n = malloc(sizeof(mat));
    n->matrix = malloc(sizeof(complex double*) * m);
    for (int i = 0; i < m; i++) {
        n->matrix[i] = calloc(m, sizeof(complex double));
    }
    n->size = m;
    for(int i=0;i<m;i++){
        for(int j=0;j<m;j++){
            n->matrix[i][j]=0;
        }
    }
    
    return n;
}


void delmat(mat *m)
{
    free(*(m->matrix+0));
    free(m->matrix);
    free(m);
}

void tpmat(mat *m)
{
    int i, j;
    complex double t;
    for (i = 0; i < m->size; i++) {
        for (j = 0; j < i; j++) {
            t = m->matrix[i][j];
            m->matrix[i][j] = m->matrix[j][i];
            m->matrix[j][i] = t;
        }
    }
}

mat* copymat(int n, complex double a[][n])
{
    mat *x = newmat(n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            x->matrix[i][j] = a[i][j];
    return x;
}

mat* mulmat(mat *x, mat *y) {
    if (x->size!= y->size) return NULL;
    mat *r = newmat(x->size);
    for (int i = 0; i < x->size; i++) {
        for (int j = 0; j < y->size; j++) {
            r->matrix[i][j] = 0;  
            for (int k = 0; k < x->size; k++) {
                r->matrix[i][j] += x->matrix[i][k] * y->matrix[k][j];
            }
        }
    }
    return r;
}



void conj_tpmat(mat *m) {
    int i, j;
    complex double t;

    for (i = 0; i < m->size; i++) {
        for (j = 0; j < i; j++) {
         
            t = m->matrix[i][j];
            m->matrix[i][j] = conj(m->matrix[j][i]);
            m->matrix[j][i] = conj(t);
        }
    }

    for (i = 0; i < m->size; i++) {
        m->matrix[i][i] = conj(m->matrix[i][i]);
    }
}


mat* takemat(mat *x, int d)
{
    mat *m = newmat(x->size);
    
    for (int i = 0; i < d; i++)
        m->matrix[i][i] = 1;
    
    for (int i = d; i < x->size; i++)
        for (int j = d; j < x->size; j++)
            m->matrix[i][j] = x->matrix[i][j];
    return m;
}

complex double *vadd(double complex a[], double complex b[], double complex s, double complex c[], int n)
{
    for (int i = 0; i < n; i++)
        c[i] = a[i] + s * b[i];
    return c;
}



mat* conjugatemul(double complex v[], int n) {
   
    mat *x = newmat(n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            x->matrix[i][j] = -2 * v[i] * conj(v[j]); 
        }
    }

    for (int i = 0; i < n; i++) {
        x->matrix[i][i] += 1;
    }

    return x;
}

complex double norm(complex double x[], int n) {
    double sum = 0.0;
    for (int i = 0; i < n; i++) {
        sum += creal(x[i] * conj(x[i])); 
    }
    return sqrt(sum);
}



complex double* scalev(complex double  x[],  complex double  d, complex double y[], int n)
{
    for (int i = 0; i < n; i++) {
        y[i] = x[i] / d;
    }
    return y;
}


complex double* excol(mat *m,complex double *v, int c)
{
    for (int i = 0; i < m->size; i++)
        v[i] = m->matrix[i][c];
    return v;
}

void matrix_show(mat *m)
{
    for (int i = 0; i < m->size; i++) {
        for (int j = 0; j < m->size; j++) {
            printf(" %.6f + %.6fi", creal(m->matrix[i][j]),cimag(m->matrix[i][j]));
        }
        printf("\n");
    }
    printf("\n");
}





void householder(mat *m, mat **R, mat **Q)
{
	
    if(m->size == 1 ){
        mat *dum = newmat(1);
        dum->matrix[0][0] = 1.0;
        *Q = dum;
        mat *dum2 = newmat(1);
        dum2->matrix[0][0] = 1.0* m->matrix[0][0];
        *R = dum2;
    }else{
        mat *q[m->size];
        mat *a1 = m, *a2;
        int ite_n;
        int min =  m->size - 1;
        if(m->size == 2){
            min = 2;
        }
      
        for (int k = 0; k < min; k++) {
           
            complex double e[m->size], x[m->size], a;
          
            a2 = takemat(a1, k);
            if (a1 != m) delmat(a1);
            a1 = a2;
           
            excol(a1, x, k);
           
            a = norm(x, m->size);
           if(cabs(m->matrix[k][k])!=0 )
            a = (1)*(m->matrix[k][k]*a)/cabs(m->matrix[k][k]);

            

            for (int i = 0; i < m->size; i++)
                e[i] = (i == k) ? 1 : 0;
            
            vadd(x, e, a, e, m->size);
            if(norm(e,m->size)!=0)
          {  
            scalev(e, norm(e, m->size), e, m->size);
          }
            q[k] = conjugatemul(e, m->size);
            

           
            a2 = mulmat(q[k], a1);
            if (a1 != m) delmat(a1);
           a1 = a2;
            
        }
        delmat(a1);
        *Q = q[0];
        *R = mulmat(q[0], m);
        
        for (int i = 1; i < min; i++) {
            
            a2 = mulmat(q[i], *Q);
            
            if (i > 1) delmat(*Q);
            
            *Q = a2;
                 delmat(q[i]);
        }
        delmat(q[0]);
                a1 = mulmat(*Q, m);
        delmat(*R);
        *R = a1;
                conj_tpmat(*Q);
    }
}






mat *input_matrix(int *size) {
    printf("Enter the  size: ");
    scanf("%d", size);
   

    mat* matrix = newmat(*size);
    printf("Enter matrix values (row by row):\n");
    for (int i = 0; i < *size; i++) {
        for (int j = 0; j < *size; j++) {
            double real_part, imag_part;

            printf("Enter the real and imaginary parts for element (%d, %d): ", i + 1, j + 1);
            scanf("%lf %lf", &real_part, &imag_part);

            matrix->matrix[i][j] = real_part + imag_part * I;
        }
    }
    
    return matrix;
}
void printeigenvalues(mat *A, double tolerance) {
    for (int i = 0; i < A->size; i++) {
        if (i < A->size - 1 && cabs(A->matrix[i+1][i]) > tolerance && cabs(A->matrix[i][i+1]) > tolerance) {
            
            complex double a = A->matrix[i][i];
            complex double b = A->matrix[i][i+1];
            complex double c = A->matrix[i+1][i];
            complex double d = A->matrix[i+1][i+1];
            
            complex double tr = a + d;
            complex double det = a * d - b * c;
            complex double e1 = tr / 2.0 + csqrt(tr * tr / 4.0 - det);
            complex double e2 = tr / 2.0 - csqrt(tr *tr / 4.0 - det);

            printf("Complex eigenvalues: %.6f + %.6fi and %.6f + %.6fi\n", 
                   creal(e1), cimag(e1), creal(e2), cimag(e2));
            i++;  
        } else {
            if(cimag(A->matrix[i][i])==0){
                 printf("Real eigenvalue: %.6f\n", creal(A->matrix[i][i]));
                
            }
             else{ 
                printf("Complex eigenvalue: %.6f + %.6fi\n", creal(A->matrix[i][i]),cimag(A->matrix[i][i]));
            }    
           
            }        
        }
    }


int main() {
    int size;
    mat *Q, *R;

    mat *A = input_matrix(&size);

    householder(A, &R, &Q);
    
   
    
        

        int max_iterations = 1000;
        double tolerance = 1e-6;  
        int count = 0;
        double maxval = 0.0;
        
        for (int i = 0;  count < max_iterations; i++) {
            A = mulmat(R, Q);
            householder(A, &R, &Q);
            maxval = 0.0;
            for (int j = 0; j < A->size; j++) {
                for (int k = 0; k < j; k++) {
                    if (j != k) {
                        maxval = fmax(maxval, cabsl(A->matrix[j][k]));
                    }
                }
            }


            if (maxval < tolerance) {
                printf("Converged  after %d iterations\n", count + 1);
                break;
            }
            
            count++; }

      
        if (count>= max_iterations) {
            printf("Maximum iterations (%d) reached.\n", max_iterations);
        }
    

    printeigenvalues(A, 1e-6); 
   
    delmat(A);
    delmat(Q);
    delmat(R);

    return 0;
}

