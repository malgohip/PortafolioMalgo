//##########    NO EJECUTE EL CODIGO SOBRE ESTE APLICATIVO  ##################
//############################################################################
#include <iostream>
using namespace std;
#define nfil 2 // Definimos una matriz de dos filas y  tres columnas
#define ncol 3

/*int main()
{

  float C[nfil][ncol]={{1,2,-1},{2,5,-2.56}}; //otra manera de ingresar datos.
  cout << "\n \t LA MATRIZ INGRESADA ES \n ";
  for (int i = 0 ; i < nfil ; ++i)
  {
    cout << endl;
    for (int j = 0 ; j < ncol ; ++j)
       cout << " \t "  <<  C[i][j];
  }
  cout << endl;
  return(0);
}*/

/*int main()
{
    int A[] = {1,3,5,7,9,11,13,15};//El compilador asume que el tamaño del arreglo es 4
    cout << "La primera componente de A es = " <<*A << endl;
    cout << "La segunda componente de A es = " <<*(A+1) << endl;
    cout << "La tercera componente de A es = " <<*(A+2) << endl;
    cout << "La cuarta  componente de A es = " <<*(A+3) << endl;
    cout << "La quinta  componente de A es = " <<*(A+4) << endl;
    cout << "La sexta   componente de A es = " <<*(A+5) << endl;
    cout << "La septima componente de A es = " <<*(A+6) << endl;
    cout << "La octava  componente de A es = " <<*(A+7) << endl;
    cout << "\n DIRECCIONES DE MEMORIA DE LAS COMPONENTES\n" <<endl;
    cout << "Direccion de la componente 1 de A es = " << &A[0] << endl;
    cout << "Direccion de la componente 2 de A es = " << &A[1] << endl;
    cout << "Direccion de la componente 3 de A es = " << &A[2] << endl;
    cout << "Direccion de la componente 4 de A es = " << &A[3] << endl;
    cout << "Direccion de la componente 5 de A es = " << &A[4] << endl;
    cout << "Direccion de la componente 6 de A es = " << &A[5] << endl;
    cout << "Direccion de la componente 7 de A es = " << &A[6] << endl;
    cout << "Direccion de la componente 8 de A es = " << &A[7] << endl;
    return(0);
}*/

/*int main()
{
    int A[] = {2,-1,1,5};
    int *P;
    P = A; //Significa que P guarda la primera componente del arreglo
           //No significa que P sea un arreglo.
    cout << "\n\t 1. El tama\~no de P es = " << sizeof(P) << endl;
    cout << "\n\t 2. El tama\~no de A es = " << sizeof(A) << endl;
    cout << "\n\t 3. El contenido de P es = "<< P << endl;
    cout << "\n\t 4. El contenido de A es = "<< A << endl;
    cout << "\n\t 5. La direccion de P es = "<< &P << endl;
    cout << "\n\t 6. La direccion de A es = " << &A << endl;//Note que el contenido de A y su dirección son los mismos.
    cout << "\n\t 7. La direccion de A[0] es = " << &A[0] << endl;
    return (0);
}*/

/*int main()
{
    int A[] = {2,-1,1,5};
    int *P;
    P = A;
    cout << "\n\n ******EL VECTOR INGRESADO ES****** \n\n ";
    for (int i = 0; i < 4; i++)
       cout << "\t" << P[i];//Se imprimen las componentes del arreglo A usando
                            //el apuntador P
    cout << endl;
    return(0);
}*/

/*int main()
{
    float A[2][3] = {{1,2,-1},{2,5,-2.56}};
    cout << "\n\n\t ******EL ARREGLO INGRESADO ES****** \n\n ";
    for (int i = 0; i < 2; i++)
    {    for (int j = 0; j < 3; j++)
           cout << "\t" << A[i][j]<<" ("<<&A[i][j]<<")";//Se imprimen los elementos del arreglo A.
        cout << endl;
    }
    cout << "\n\n ******LAS DIRECIONES DEL ARREGLO INGRESADO SON****** \n\n ";
    for (int i = 0; i < 2; i++)
    {   for (int j = 0; j < 3; j++)
           cout << "\t" << &A[i][j];//Se imprimen  las direcciones de los elementos del arreglo A.
        cout << endl;
    }
    return(0);
}*/

#define nfil 3
#define ncol 3

/*int main()
{

  float A[nfil][ncol]={{1,2,-1},{2,5,-1},{3,2,1}};
  cout << "\n \t \t LA MATRIZ INGRESADA ES \n ";
  for (int i = 0 ; i < nfil ; ++i)
  {
    cout <<endl;
    for (int j = 0 ; j < ncol ; ++j)
       cout << " \t \t"  << *(*(A+i)+j);
  }
  cout << endl;
 // IMPRIMIMOS LAS DIRECCIONES DE MEMORIA DEL PRIMER ELEMENTO DE CADA FILA
 cout << "\n \t LAS DIRECCIONES DE LAS FILAS DE LA MATRIZ INGRESADA SON \n ";
 for (int i = 0 ; i < nfil ; ++i)
     cout << "\n \t \t Dirección Fila "<< i  <<" = " << A[i];
 cout << endl;
 return(0);
}*/

#include <stdlib.h>

/*int main()
{
	int m;
	float *A;
   cout << "\n\t Ingrese el número de componentes del arreglo = ";
   cin >> m;
   A = new float [m];
   if (A==NULL)
   {
   		cout << "\n Memoria insuficiente ";
   		exit(1);
   }
   cout << "\n\n ***** INGRESANDO ARREGLO ***** ";
	for (int i=0; i < m ; ++i)
	{
       cout << "\n A[" << i << "] = ";
       cin >> A[i];
	}
  cout << " \n\n *****  ARREGLO LEIDO ***** " <<endl;
	cout << "\n ";
	for (int i=0; i < m ; ++i)
          cout << A[i] << "\t" ;
    cout << endl;
	delete [] A; //Permite liberar la memoria reservada para A.
	return(0);
}*/

int main()
{
	int m,n;
	float **A;
   cout << "\n\t Ingrese el número de fila = ";
	cin >> m;
	cout << "\n\t Ingrese el número de columnas = ";
	cin >> n;
   A = new float *[m];
   if (A==NULL)
   {
   		cout << "\n Memoria insuficiente ";
   		exit(1);
   }
   for (int i=0; i < m; ++i)
   	 {
   	  	 A[i]= new float [n];
   	  	 if (A[i]==NULL)
   	  	 {
	   		cout << "\n Memoria insuficiente ";
	   		exit(1);
   	  	 }
   	  }

	cout << "\n\n ***** INGRESANDO LA MATRIZ ***** ";
	for (int i=0; i < m ; ++i)
	{   cout << "\n";
	   for (int j=0; j < n ; ++j)
	     {
	     	cout << "\n A["<< i << "][" << j << "] = ";
     		cin >> A[i][j];
	     }
	    cout << "\n";
	}
	cout <<  "\n\n *****  MATRIZ LEIDA ***** " <<endl;
	for (int i=0; i < m ; ++i)
	{  cout << "\n \t";
	   for (int j=0; j < n ; ++j)
	    cout <<   A[i][j] <<"\t" ;
	   cout << "\n";
	}
}
