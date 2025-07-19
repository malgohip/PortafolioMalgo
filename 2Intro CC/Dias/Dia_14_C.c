# include <stdbool.h>
# include <stdio.h>

/*int main() {
  int Numdolares, Tcambio, Costo;
  printf("Introduzca el numero de dolares a comprar: $");
  scanf("%d", &Numdolares);
  printf("Dime la tasa de cambio para los dolares: $");
  scanf("%d", &Tcambio);
  Costo=Numdolares*Tcambio;
  printf("Costo = $ %d \n ", Costo);
  return(0);
}*/

/*int main (){
  printf("\n\t Caracter: %c %c \n", 'a', 65);
  printf("\n\t Entero y entero largo: %d %ld \n", 1977, 650000);
  printf("\n\t Precedido por espacios: %10d \n", 1977);
  printf("\n\t Precedido por ceros: %010d \n", 1977);
  printf("\n\t En punto flotante: %5.2f %5.2e %5.2E \n", 3.1416, 3.1416, 3.1416);
  printf("\n\t Cadena de caracteres: %s \n", "Esta es una cadena de caracteres o string");
  return(0);
}*/

//logica en C
/*int main(){
  bool p,q,r,s,t,v;
  p= 5 != 3; // p pasa a ser True
  q= 1 != 1; // q pasa a ser False
  r= p && q;
  s= p || q;
  t= !true;
  v= !false;
  printf("r es = %u \n", r);
  printf("s es = %u \n", s);
  printf("t es = %u \n", t);
  printf("v es = %u \n", v);
}*/

int main(){
  int a=64, b=12, c, d, e;
  c=a&b;
  d=a|b;
  e=a^b;
  printf("a&b en binario es = %u \n", c);
  printf("a|b en binario es = %u \n", d);
  printf("a^b en binario es = %u \n", e);
}