// Este programa muestra el uso de los apuntadores en C++

# include <iostream>

using namespace std;

/*int main()
{
   int a = 10;
   int *aPtr, *bPtr;
   aPtr = &a;
   bPtr = NULL;//el apuntador no apunta a ninguna variable
   cout <<"\n El contenido de la variable a es: " << a;
   cout <<"\n El contenido de la variable apuntada por aPtr es: " << *aPtr;
   cout <<"\n la direccion de a es : " << &a
    <<"\n o tambien " << aPtr;
   cout <<"\n La direccion de aPtr es: " << &aPtr;
   cout <<"\n El contenido de aPtr es :"  << aPtr;
   cout <<"\n El contenido de bPtr es :"  << bPtr;
   cout <<"\n El contenido de la variable a es:" << *(&a) <<endl;
}*/

/*int main()
{
  int a,b,mayor, menor;
  cout << "\n\t Este programa compara dos numeros distintos dados por el usuario y los clasifica " << endl;
  cout << "\n\t Digite el primer numero : ";
  cin >> a;
  cout << "\n\t Digite el segundo numero : ";
  cin >> b;
  if (a > b )
  {
    mayor = a;
    menor = b;
  }
  if (b > a)
  {
    mayor = b;
    menor = a;
  }
  cout << "\n\t El numero mayor es " << mayor << " y el numero menor es " << menor
       << endl;
 return(0);
}*/

/*int main()
{
  int a,b;
  cout << "\n\t Este programa compara dos numeros dados por el usuario y los clasifica " << endl;
  cout << "\n\t Digite el primer numero : ";
  cin >> a;
  cout << "\n\t Digite el segundo numero : ";
  cin >> b;
  if (a == b )
  {
    cout << "\n\t Los números dados son iguales y su valor es: " << a << endl;
  }
  else
  {
    if (a > b)
    {
      cout << "\n\t El numero mayor es : " << a
           << " y el menor es : " << b << endl;
    }
    else
    {
      cout << "\n\t El numero mayor es : " << b
           << " y el menor es : " << a << endl;
    }
  }
 return(0);
}*/

/*int main()
{
  int Nota;
  cout << "Ingrese una nota numerica entera de 0 a 100 =  ";
  cin  >> Nota;
  if (Nota >= 90 && Nota <= 100)
      cout << "\n\t Nota Alfabetica = A ";
  else if (Nota >= 80 && Nota < 90)
      cout << "\n\t Nota Alfabetica = B ";
  else if (Nota >= 70 && Nota < 80)
      cout << "\n\t Nota Alfabetica = C ";
  else if (Nota >= 60 && Nota < 70)
      cout << "\n\t Nota Alfabetica = D ";
  else if ( Nota < 60)
      cout << "\n\t Nota Alfabetica = F ";
  return(0);
}*/

/*int main()
{
  cout << "*********************************************************" << endl;
  cout << "******     CODIGO  ASCII PARA LOS SÍMBOLOS       ********" << endl;
  cout << "*********************************************************" << endl;
  for (int i=-128; i <= 127 ; i++)
    cout << "\t " << i << " \t "<< (char) i << endl ;
  return(0);
}*/