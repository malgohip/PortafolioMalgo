// PROGRAMA while con condición
// Este programa calcula el factorial de un numero
// Observe que calcula exacto el valor hasta 12!
#include <iostream>
using namespace std;
/*int main ()
{
  int i, n, factorial;
  char respuesta;
  respuesta = 's';
  cout << "\n\t ESTE PROGRAMA CALCULA EL FACTORIAL DE UN NUMERO NATURAL ";

  while (respuesta == 's')
  {
    cout << "\n\n \t Ingrese un número natural: ";
    cin >> n;
    i = n;
    factorial = 1;
    while ( i !=0 )
    {
      factorial = factorial*i;
      i--;
    }
    cout << "\n\t " << n << "! = " << factorial << endl;
    cout << "\n\n\t Desea calcular un nuevo valor: digite si (s), no (n) y luego ENTER?";
    cin >> respuesta;
  }
  cout << "\n\t Gracias por usar nuestro programa \n\n";
 return(0);
}*/

/*int main()
{
    int a,b;
    char eleccion;
    cout << "Ingrese el primer numero = ";
    cin >> a;
    cout << "Ingrese el segundo numero = ";
    cin >> b;
    cout << "\n\t ***Menu de operaciones*** \n "
         << " \n\t Suma (s)  \n "
         << " \n\t Resta (r) \n "
         << " \n\t Multiplicacion (m) \n "
         << " \n\t Division  (d) \n \t ";
    cin >> eleccion;
     switch (eleccion)
     {
        case 's': cout << "\n \t La suma es " << a+b << endl;
                  break;
        case 'r': cout << "\n \t La resta es " << a-b << endl;
                  break;
        case 'm': cout << "\n \t La multiplicacion es " << a*b << endl;
                  break;
        case 'd': cout << "\n \t La division es " << a/b << endl;
                  break;
        default:  cout << "Eleccion invalida" << endl ;
     }
     return(0);
}*/

#define pi 3.141516
/*float area_del_circulo(float );//Prototipo de la función
int main()
{
  float radio;
  char respuesta;
  do{
     cout << "\n \t \a Digite el radio del circulo: \n\t";
     cin >> radio;
     cout << "\n \t \a El area del circulo es: "
	        << area_del_circulo(radio) << endl;
     cout << "\n\t Desea seguir calculando si(s),no(n)?\n\t";
     cin >> respuesta;
   }while(respuesta == 's');
}
float area_del_circulo(float r)
{
  float area;
  area = pi*r*r;
  return area;
}*/

#include <math.h> # Permite usar la funcion sqrt()
/*int primo (int ); //Prototipo de la funcion primo()
int main()
{
	int n,p;
	char respuesta;
	cout << "\n\t Este programa determina si un número es o no primo " << endl;

	do
	{
		cout << "\n\t Ingrese un numero natural ";
		cin >> n;
		p = primo(n);
		if (p == 1)
	 		cout << "\n\t " << n << " es un número primo " << endl;
	 	else
			cout << "\n\t " << n << " no es un número primo. " << endl;
		cout << "\n\t ¿ Desea ingresar mas numeros si(s) no(n) ? " ;
		cin >> respuesta;
		cout << endl;
	}while (respuesta == 's');
}

 int primo(int numero)
 {
      int prim, i;
      float raiz;
      if (numero == 1)
	      prim = 0;
      else
      	if (numero == 2)
   		    prim = 1;
	      else
        {
      	    raiz = sqrt(numero);
		        i = 2;
		       do
		      {
		         if( numero % i == 0)
		             prim = 0;
		         else
			           prim = 1;
			       i++;
		      }while (i <= raiz && prim);
        }
      return prim;
 }*/

/*int main()
{
    int A[7];
    for (int i=0;i<7;i++)
    {
        cout <<"\n\t Ingrese A[ "<<i <<" ] = ";
        cin  >> A[i];
    }
    return (0);
}*/

int main()
{
    float A[3][3];
    for (int i=0 ; i<3 ; i++)
       for (int j=0;j<3;j++)
    {
        cout <<"\n\t Ingrese A[ "<<i <<" ][ "<< j <<"] = ";
        cin  >> A[i][j];
    }
    cout << "\n\t LA MATRIZ INGRESADA ES \n " << endl;
    for (int i=0 ; i<3 ; i++)
    {
       for (int j=0 ; j<3 ; j++)
          cout << " \t " << A[i][j];
       cout << endl;
    }
    return (0);
}
