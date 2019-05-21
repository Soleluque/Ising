#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <string.h>

int main(int argc, char *argv[]) {

  int *red;
  float random;
  int i,j,dim;

  sscanf(argv[1],"%d",& dim);

  srand(1);
  dim=dim+2; //dimension con las condiciones de contorno periodicas
  red = malloc(dim*dim*sizeof(int));


  for (i=0;i<dim*dim;i++)
  {
    *(red+i)=0;
  }

  for (i=1;i<dim-1;i++) //pueblo 1ero la matriz con 1 y -1 sin los bordes
    {
      for (j=1;j<dim-1;j++)

      {
        *(red+i*dim+j)=-1;
        random=((float)rand())/((float) RAND_MAX);
        if (random<0.5)
        {
          *(red+i*dim+j)=1;
        }

      }

    }

    for (i=0;i<dim;i++) //Para imprimir la red si pinta verla
      {for (j=0;j<dim;j++)
        {
          printf("%d ", *(red+dim*i+j));
        }
          printf("\n");
      }

      printf("\n");


  for (i=1;i<dim-1;i++)
  {
    for(j=1;j<dim-1;j++)
    {
      *(red+i)=*(red+(dim-2)*dim+j); //primera fila contorno
      //*(red+dim*dim+i)=*(red+j+dim); //ultima fila contorno
      //*(red+i*dim)=*(red+j*dim+(dim-2)); //primera columna
      //*(red+i*(dim-1))=*(red+j*dim+1); //ultima columna

    }
  }



  for (i=0;i<dim;i++) //Para imprimir la red si pinta verla
    {for (j=0;j<dim;j++)
      {
        printf("%d ", *(red+dim*i+j));
      }
        printf("\n");
    }





  return 0;
}
