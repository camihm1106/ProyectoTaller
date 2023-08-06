#include <iostream>

using namespace std;

int main()
{
    string nombre;
    int edad;
    string direccion;

    cout << "Ingrese su nombre: ";
    getline(cin,nombre);

    cout << "\nIngrese su edad: ";
    cin >> edad;
    cin.ignore();

    cout << "\nIngrese su direccion: ";
    getline(cin,direccion);

    cout<<"\nSu nombre: "<<nombre;
    cout<<"\nSu edad: "<<edad;
    cout<<"\nSu direccion: "<<direccion;

    return 0;
}