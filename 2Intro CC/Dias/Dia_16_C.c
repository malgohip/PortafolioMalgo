#include <stdio.h>      /* printf, scanf, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

/*int main ()
{
  int NSecreto, NAdivinado;
  srand (time(NULL)); / inicializa la semilla aleatoria /
                      /rand genera aleatoriamente un entero entre 0 y 32767/
  NSecreto = rand() % 10 + 1; / genera un numero secreto entre 1 y 10 inclusive /
  do
 {
    printf ("Adivine un numero de (1 a 10): ");
    scanf ("%d",&NAdivinado); / scanf permite leer un valor dado por teclado/
    if (NSecreto < NAdivinado)
        printf ("\tEl numero secreto es menor\n");
    else if (NSecreto > NAdivinado)
        printf ("\tEl numero secreto es mayor\n");
  } while (NSecreto != NAdivinado);

  printf ("Felicitaciones adivinó el número !");
  return (0);
}*/
/*
// Variables Globales
int A = 10;
int B = 15;

int Suma()
{
    return A + B;
}

int main()
{
    int respuesta; // Variable local
    respuesta = Suma();
    printf(" %d + %d = %d\n",A,B,respuesta);
    return (0);
}*/

/*int g = 20;
void variableglobal()
 {
    printf ("valor global de g = %d\n",  g);
 }
int main ()
{
  int g = 10;
  printf ("valor local de g = %d\n",  g);
  variableglobal();
  return 0;
}*/

