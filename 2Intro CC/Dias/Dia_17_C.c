#include <stdio.h>
#include <stdlib.h>

/*int main()
{
	int m;
	float *A;
   printf ("\n\t Ingrese el número de componentes del arreglo = ");
   scanf("%d",&m);
   A = malloc(m*sizeof(float));
   if (A==NULL)
   {
   		printf("\n Memoria insuficiente ");
   		exit(1);
   }

   printf("\n\n ***** INGRESANDO ARREGLO ***** ");
	for (int i=0; i < m ; ++i)
	{  printf("\n");
	   printf("\n A[%d] =",i);
     scanf("    ",&A[i]);
	}
    printf("\n");
	printf("\n\n *****  ARREGLO LEIDO ***** ");
	for (int i=0; i < m ; ++i)
	{  printf("\n");
	      printf("\t %5.3f", A[i]);
	   printf("\n");
	}
	free(A);//Permite liberar la memoria reservada para A.
	return (0);
}*/

int main()
{
	int m,n;
	float **A;
    printf("\n\t Ingrese el número de fila = ");
	scanf("%d",&m);
	printf("\n\t Ingrese el número de columnas = ");
	scanf("%d",&n);
   A = malloc(m*sizeof(float));
   if (A==NULL)
   {
   		printf("\n Memoria insuficiente ");
   		exit(1);
   }

   for (int i=0; i < m ; ++i)
   	 {
   	  	 A[i]= malloc(n*sizeof(float));
   	  	 if (A[i]==NULL)
   	  	 {
	   		printf("\n Memoria insuficiente ");
	   		exit(1);
   	  	 }
   	  }

	printf("\n\n ***** INGRESANDO MATRIZ ***** ");
	for (int i=0; i < m ; ++i)
	{   printf("\n");
	   for (int j=0; j < n ; ++j)
	     {
	     	 printf("\n A[%d][%d] = ",i,j);
             scanf("%f",&A[i][j]);
	     }
	    printf("\n");
	}
	printf("\n\n \t ***** MATRIZ LEIDA ***** ");
	for (int i=0; i < m ; ++i)
	{  printf("\n \t");
	   for (int j=0; j < n ; ++j)
	    printf("  %3.2f",A[i][j]);
	   printf("\n");
	}
}
