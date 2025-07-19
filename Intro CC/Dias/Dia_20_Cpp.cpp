#include <iostream>
using namespace std;
/*
enum Dias  {lunes,martes,miercoles,jueves,viernes,sabado,domingo};
int main()
{
    enum Dias Hoy;
    setlocale(LC_CTYPE,"Spanish"); //Para imprimir la "ñ" y letras tildadas.
    Hoy = martes;
    switch(Hoy)
    {
        case lunes: cout <<"\n\n\t Mañana es martes \n\n";
                    break;
        case martes: cout <<"\n\n\t Mañana es miercoles \n\n";
                    break;
        case miercoles: cout <<"\n\n\t Mañana es jueves \n\n";
                    break;
        case jueves: cout <<"\n\n\t Mañana es viernes \n\n";
                    break;
        case viernes: cout <<"\n\n\t Mañana es sabado \n\n";
                    break;
        case sabado :cout <<"\n\n\t Mañana es domingo \n\n";
                    break;
        default:     cout <<"\n\n\t Mañana es lunes \n\n";
    }
    return (0);
}*/
/*
//En este código se compara un string A ingresado por el usuario
//con los string correspondientes a días de la semana.
// Luego el string A se convierte a un strig tipo Dias.
enum  Dia  {lunes,martes,miercoles,jueves,viernes,sabado,domingo};
Dia convertidor ( string A)
{
   if (A.compare("lunes")== 0)
       return lunes;
   else if (A.compare("martes")==0)
       return martes;
   else if (A.compare("miercoles")==0)
       return miercoles;
   else if (A.compare("jueves")==0)
       return jueves;
   else if (A.compare("viernes")==0)
       return viernes;
   else if (A.compare("sabado")==0)
       return sabado;
   else if (A.compare("domingo")==0)
       return domingo;
}

int main()
{
    setlocale(LC_CTYPE,"Spanish"); //Para imprimir la "ñ" y letras tildadas.
    enum Dia Hoy;
    string d, actividad;
    cout <<"\n\t Que día es hoy ?\n\t";
    cin >> d;
    Hoy = convertidor(d);
    if (Hoy !=sabado && Hoy!=domingo )
        actividad = "trabajo";
    else
        actividad = "descanso";
        cout <<"\n\t Hoy " << d << " es un día de " <<actividad;
    return (0);
}*/

/*#include <string> //Permite manejar strings
// DECLARACION DE LA ESTRUCTURA Estudiante
 struct Estudiante
 {
  string Nombre;
  string Apellido;
  int Edad;
  string Carrera;
  int Semestre;
};

int main()
{
    struct Estudiante A;//A es un objeto de tipo Estudiante
    cout <<"\n\t Nombre del estudiante = ";
    cin >> A.Nombre;
    cout <<"\n\t Apellido del estudiante = ";
    cin >> A.Apellido;
    cout <<"\n\t Edad del estudiante = ";
    cin >> A.Edad;
    cout <<"\n\t Carrera del estudiante = ";
    cin >> A.Carrera;
    cout <<"\n\t Semestre del estudiante = ";
    cin >> A.Semestre;
    cout << "\n\n ****** INFORMACION DEL ESTUDIANTE*****"<< endl;
    cout << "\n\n\t NOMBRE : "  << A.Nombre <<" " << A.Apellido << endl;
    cout << "\n\n\t EDAD : "    << A.Edad <<endl;
    cout << "\n\n\t CARRERA : " << A.Carrera <<endl;
    cout << "\n\n\t SEMESTRE : "<< A.Semestre <<endl;

    return 0;
}*/

/*
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
  cout << "\n\t Este programa hace uso de tipos de datos nuevos (struct)"
        << "\n\t que puede definir el programador segun necesite. "
       << "\n\t Define un complejo con parte real e imaginaria. "
       << "\n\t Lee cada parte y la calcula suma y la resta de los números."
       << endl << endl;
  cout << "\n\t*** INGRESE EL PRIMER NUMERO COMPLEJO ***\n";
  a = leer_complejo();
  cout << "\n\t*** INGRESE EL SEGUNDO NUMERO COMPLEJO ***\n";
  b = leer_complejo();
  s = suma(a,b);
  r = resta(a,b);
  cout << "\n\t*** RESULTADOS DE LA SUMA Y LA RESTA ***\n"
       << "\n\t La suma es = "<< s.re <<" + "<<s.im<<"i "
       << "\n\t La resta es = "<<r.re<<" + "<<r.im<<"i \n\n\t";
  return (0);
}
// DEFINICION DE LAS FUNCIONES
struct complejo leer_complejo()
{
  struct complejo c;
  cout << "\n\t ingrese la parte real = ";
  cin >> c.re;
  cout << "\n\t ingrese la parte imaginaria = ";
  cin >> c.im;
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

/*#include<iostream>
#include <stdio.h>
#include <math.h>
using namespace std;
// DECLARACION DEL PROTOTIPO DE LA ESTRUCTURA COMPLEJO
 struct complejo{
  float re;
  float im;
};
// DECLARACION DE LOS PROTOTIPOS DE LAS FUNCIONES
struct complejo leer_complejo();
struct complejo suma(struct complejo, struct complejo);
struct complejo resta(struct complejo,  struct complejo);
struct complejo multiplicacion(struct complejo, struct complejo);
struct complejo division(struct complejo,  struct complejo);
// INICIO DEL PROGRAMA PRINCIPAL
int main()
{
  struct complejo a,b,s,r,m,d;
  cout << "\n\t Este programa hace uso de tipos de datos nuevos (struct)"
        << "\n\t que puede definir el programador segun necesite. "
       << "\n\t Define un complejo con parte real e imaginaria. "
       << "\n\t Lee cada parte y la calcula suma y la resta de los números."
       << endl << endl;
  cout << "\n\t*** INGRESE EL PRIMER NUMERO COMPLEJO ***\n";
  a = leer_complejo();
  cout << "\n\t*** INGRESE EL SEGUNDO NUMERO COMPLEJO ***\n";
  b = leer_complejo();
  s = suma(a,b);
  r = resta(a,b);
  m = multiplicacion(a,b);
  d = division(a,b);
  cout << "\n\t*** RESULTADOS DE LA SUMA Y LA RESTA ***\n";
  printf ("\n\t La suma es = %f + %f i ", s.re,s.im);
  printf ("\n\t La resta es = %f + %f i \n\n\t", r.re,r.im);
  printf ("\n\t La multiplicación es = %f + %f i \n\n\t", m.re,m.im);
  printf ("\n\t La división es = %f + %f i \n\n\t", d.re,d.im);
  return (0);
}
// DEFINICION DE LAS FUNCIONES
struct complejo leer_complejo()
{
  struct complejo c;
  cout << "\n\t ingrese la parte real = ";
  scanf("%f",&c.re);
  cout << "\n\t ingrese la parte imaginaria = ";
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
}

struct complejo multiplicacion( struct complejo a, struct complejo b)
{
 struct complejo c;
 c.re = (a.re*b.re)-(a.im*b.im);
 c.im = (a.re*b.im)+(a.im*b.re);
 return c;
}

struct complejo division( struct complejo a, struct complejo b)
{
 struct complejo c;
 c.re = ((a.re*b.re)+(a.im*b.im))/(pow(b.re,2)+pow(b.im,2));
 c.im = ((a.re*b.im)+(a.im*b.re))/(pow(b.re,2)+pow(b.im,2));
 return c;
}*/

