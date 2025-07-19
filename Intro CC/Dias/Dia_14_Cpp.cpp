#include <iostream>

/*int main() {
  int a = 2, b = 3;
  std::cout <<"\n\t " << a/b //entero sobre entero es entero 
            <<"\n\t " << b/a //entero sobre entero es entero 
            <<"\n\t " << (float) a/b //la division como float (Da float)
            <<"\n\t " << float (b)/float (a) //se pasan ambas variables a float y se divide (da float)
            <<"\n\t " << float (b/a) //Se hace la division entera y se promueve a tipo float (da punto flotante)
            <<"\n\t " << a/(b*1.0) //se promueve el denominador a float y se hace la division (da float)
            <<"\n\t " << float (a)/b; //se promueve el numerador a float y se hace la division (da float)
            <<Toda operación con una parte float da float
  return(0);
}*/

/*int main(){
  char a;
  short int b;
  int c;
  long int d;
  float e;
  double f;
  std::cout << "\n\t el tamaño de char es: "<< sizeof(a) <<"byte.";
  std::cout << "\n\t el tamaño de short es: "<< sizeof(b) <<"bytes.";
  std::cout << "\n\t el tamaño de int es: "<< sizeof(c) <<"bytes.";
  std::cout << "\n\t el tamaño de long es: "<< sizeof(d) <<"bytes.";
  std::cout << "\n\t el tamaño de float es: "<< sizeof(e) <<"bytes.";
  std::cout << "\n\t el tamaño de double es: "<< sizeof(f) <<"bytes.";
  return(0);
}*/

using namespace std;

/*int main(){
  char a;
  short int b;
  int c;
  long int d;
  float e;
  double f;
  long double g;
  cout << "\n\t el tamaño de char es: "<< sizeof(a) <<"byte.";
  cout << "\n\t el tamaño de short es: "<< sizeof(b) <<"bytes.";
  cout << "\n\t el tamaño de int es: "<< sizeof(c) <<"bytes.";
  cout << "\n\t el tamaño de long es: "<< sizeof(d) <<"bytes.";
  cout << "\n\t el tamaño de float es: "<< sizeof(e) <<"bytes.";
  cout << "\n\t el tamaño de double es: "<< sizeof(f) <<"bytes.";
  cout << "\n\t el tamaño de long double es: "<< sizeof(g) <<"bytes.";
  return(0);
}*/

/*int main(){
  int a = 2147483647;
  cout << "\n\n\t Maximo valor tipo int = " << a;
  a= 2147483648;
  cout << "\n\n\t Inconsistencia al guardar 2147483648 como int e impormirlo"<< a;
  return (0);
}*/

//muenstra el uso de asignaciones de C++
/*int main(){
  int m = 5;
  cout << "m = " << m <<endl;
  m+=5;
  cout << "m += 5, reporta m = " << m <<endl;
  m-=5;
  cout << "m -= 5, reporta m = " << m <<endl;
  m*=5;
  cout << "m *= 5, reporta m = " << m <<endl;
  m/=5;
  cout << "m /= 5, reporta m = " << m <<endl;
  m%=5;
  cout << "m %= 5, reporta m = " << m <<endl;
  m++;
  cout << "m++ reporta m = " << m <<endl;
  m--;
  cout << "m-- reporta m = " << m <<endl;
}*/

/*int main(){
  int a=64, b=12, c, d, e;
  c=a&b;
  d=a|b;
  e=a^b;
  cout << "a&b en binario es =  "<< c<< endl;
  cout << "a|b en binario es =  "<< d<< endl;
  cout << "a^b en binario es =  "<< e<< endl;
}*/