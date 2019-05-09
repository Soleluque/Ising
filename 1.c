#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>


int main(int argc, char *argv[]) {
  float delta, x_n, x_v, r,pa=0;
  float *xs;
  int i,it=1000000;
  FILE *C_int;

  sscanf(argv[1], "%f", & delta);

  xs = malloc(it*sizeof(float));


  C_int = fopen("integral.txt", "a");

  srand(time(NULL));

  x_v = -0.5;    //x inicial.

  for(i=0;i<it;i++)
  {
    *(xs+i)=0;
  }


  *(xs) = x_v;


  fprintf(C_int, "%0.2f\n", *(xs));

  while(abs(pa-0.4)<0.2)
  { pa=0.0;

    for(i=1;i<it;i++) {
      r = ((float)rand())/((float)RAND_MAX);

      x_n = x_v + ((float)rand())/((float)RAND_MAX) * (2*delta) - delta;    //x nuevo dentro del intervalo.

      if((pow(x_n,2)*exp(-pow(x_n,2)/2))/pow(x_v,2)*exp(-pow(x_v,2)/2) > r) {
        *(xs+i) = x_n;
        x_v = x_n;
        pa=pa+1;

      }

      ;

      if((pow(x_n,2)*exp(-pow(x_n,2)/2))/pow(x_v,2)*exp(-pow(x_v,2)/2) < r) {
        *(xs+i) = x_v;
      }



      fprintf(C_int, "%0.2f\n", *(xs+i));

    }
    pa=pa/it;
    printf("%f\n",pa);
    delta=delta+0.0001;
  }

/*
  for(i=0; i<10; i++) {
    printf("%f ", *(xs+i));
  }
  printf("\n");

  printf("%0.2f %0.2f\n", x_v, x_n);
*/
printf("%f ",delta);
free(xs);
  return 0;
}
