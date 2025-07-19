//5. Dados un par de números enteros n y m con n < m, diseñe un código que permita determinar cuales números de
//todos los posibles productos $i\times j$ con $n<i<m$ y $n<j<m$, son divisibles por 3 y 7.

# include <iostream>

using namespace std;

int main(){
    int n,m;
    char respuesta;
    do{
        cout << "Te recuerdo que n debe ser menor a m\n";
        cout << "\nDime el numero n = \n";
        cin >> n;
        cout << "\nDime el numero m = \n";
        cin >> m;
        if (n < m){
            cout << "Perro con leche";
            respuesta = 'n';
            cout << endl;
        }
        else{
            cout << "\nERROR: recuerda que n debe ser menor a m"
                 << "\n\t Desea volver a intentar? si(s) no (n) ?\n";
            cin >> respuesta;
            cout << endl;
        }
    }while (respuesta = 's');
    cout << "Gracias por correr mi codigo :D";
    return(0);
}
