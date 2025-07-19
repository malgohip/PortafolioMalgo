#include<iostream>
#include<math.h>
using namespace std;

/*int main()
{
	int i = 0;
	float numero = 1.0;
	while (  numero != 0)
  {
		cout << "\n\t   "<< i << "  " << numero;
		numero/=2.0;
		i++;
  }
	cout<<" \n\n\t La maquina hace cero el número  = 2^ (-"<< i <<") = " << numero*2 <<endl;
  return 0;
}*/

/*int main()
{
	int i = 0;
	float numero = 1.0;
	float x = 1+ numero;
	while ( x != 1)
  {
		cout << "\n\t   "<< i << "  " << numero;
		numero/=2.0;
		x = 1 + numero;
		i++;
  }
	cout<<" \n\n\t Epsilon de la maquina = 2^ (-"<< i-1 <<") = " << numero*2 <<endl;
	cout <<"\n\n\t Note que aun cuando 2^(-24) es distinto de cero, ";
	cout <<" se tiene que 1 + 2^(-24) = 1 \n\n\t con la aritmetica de la maquina \n\n";
    return 0;
}*/

//NOTA. El archivo Estudiantes.txt debe haber sido previamente creado, sino
// se hace de esta manera, el código reportará un error.
#include <fstream>  //permite usar ofstream

int main()
{
    ofstream F("Estudiantes.txt", ios::in); //ofstream Permite crear el objeto F
                                             // para administrar el archivo Estudiantes.txt
                                             //ios::out Abre un archivo para ingresar datos.
    if (!F)
    {
        cout <<"El archivo no puede abrirse";
        exit(1);
    }
    cout << "Ingrese separado por un espacio\n"
         << "ID, Nombre, Apellido, las notas de los parciales P1, P2 y P3 luego de ENTER\n"
         << "Para terminarctrl+z (EOF) y dar ENTER  \n ?";
    int ID;
    char Nombre[10];
    char Apellido[10];
    float P1,P2,P3;
    while (cin >> ID >> Nombre >> Apellido >> P1 >> P2 >> P3)
    {
        F << ID << " " << Nombre << " " << Apellido<< " "
          << P1 << " " << P2 <<" " << P3 << "\n";
        cout << " ? ";
    }
    cout << "\n\n ARCHIVO GENERADO CORRECTAMENTE ... \n";
    return(0);
}
