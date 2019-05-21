#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>


int main(int argc, char *argv[]) {
  float delta, x_n, x_v,r,pa=0;
  float *xs;
  int i,it=1000000;
  FILE *C_int;


  //sscanf(argv[1], "%f", & delta);

  xs = malloc(it*sizeof(float));



  C_int = fopen("correlacion.txt", "a");


  srand(time(NULL));

  x_v = -0.5;    //x inicial.

  for(i=0;i<it;i++)
  {
    *(xs+i)=0;
  }




  *(xs) = x_v;



  //fprintf(C_int, "%0.2f\n", *(xa));

  for(delta=2.6;delta<3;delta=delta+0.01)
  { pa=0.0;
    fprintf(C_int, "%f\n",delta);

    for(i=1;i<it;i++) {
      r = ((float)rand())/((float)RAND_MAX);

      x_n = x_v + ((float)rand())/((float)RAND_MAX) * (2*delta) - delta;    //x nuevo dentro del intervalo.

      if(exp((x_v*x_v-x_n*x_n)/2.0) > r) {
        *(xs+i) = x_n;
        x_v = x_n;

        pa=pa+1;

      }



      else {
        *(xs+i) = x_v;
      }


      fprintf(C_int, " %f\n",*(xs+i));
      //fprintf(C_int, "%0.2f\n", *(xa+i));

    }

    //xi=xi/it;
    //xi2=xi2/it;

    //printf("%f\n",pa);
    //pa=pa/it;


  }

/*
  for(i=0; i<10; i++) {
    printf("%f ", *(xs+i));
  }
  printf("\n");

  printf("%0.2f %0.2f\n", x_v, x_n);
*/
free(xs);

fclose(C_int);
  return 0;
}
