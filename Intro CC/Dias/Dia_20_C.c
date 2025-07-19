/*#include <stdio.h>
// DECLARACION DEL PROTOTIPO DE LA ESTRUCTURA COMPLEJO
 struct complejo{
  float re;
  float im;
};
// DECLARACION DE LOS PROTOTIPOS DE LAS FUNCIONES
struct complejo leer_complejo();
struct complejo suma(struct complejo, struct complejo);
struct complejo resta(struct complejo,  struct complejo);
// INICIO DEL PROGRAMA PRINCIPAL
int main()
{
  struct complejo a,b,s,r;
  printf("\n\t Este programa hace uso de tipos de datos nuevos (struct)");
  printf("\n\t que puede definir el programador segun necesite. ");
  printf("\n\t Define un complejo con parte real e imaginaria. ");
  printf("\n\t Lee cada parte y la calcula suma y la resta de los números.");
  printf("\n\t*** INGRESE EL PRIMER NUMERO COMPLEJO ***\n");
  a = leer_complejo();
  printf("\n\t*** INGRESE EL SEGUNDO NUMERO COMPLEJO ***\n");
  b = leer_complejo();
  s = suma(a,b);
  r = resta(a,b);
  printf("\n\t*** RESULTADOS DE LA SUMA Y LA RESTA ***\n");
  printf ("\n\t La suma es = %f + %f i ", s.re,s.im);
  printf ("\n\t La resta es = %f + %f i \n\n\t", r.re,r.im);
  return (0);
}
// DEFINICION DE LAS FUNCIONES
struct complejo leer_complejo()
{
  struct complejo c;
  printf("\n\t ingrese la parte real = ");
  scanf("%f",&c.re);
  printf("\n\t ingrese la parte imaginaria = ");
  scanf("%f",&c.im);
  return c;
}
struct complejo suma( struct complejo a, struct complejo b)
{
 struct complejo c;
 c.re = a.re + b.re;
 c.im = a.im + b.im;
 return c;
}

struct complejo resta( struct complejo a, struct complejo b)
{
 struct complejo c;
 c.re = a.re - b.re;
 c.im = a.im - b.im;
 return c;
}*/
