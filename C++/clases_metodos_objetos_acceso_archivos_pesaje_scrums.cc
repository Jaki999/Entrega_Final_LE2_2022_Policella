#include <iostream>
#include <string>
#include <fstream>

using namespace std;

class jugador {
    public:
        string nombre;
        int peso;
}; 

class scrum {
    public:
        jugador jugadores[8];
        int pesaje();     
};
int scrum::pesaje() {
    int suma = 0;
    for (int i=0; i<8; i++) suma += jugadores[i].peso;
    return suma;
}

int main(){
    fstream a_archivo ("Output.txt");
    
    cout << "Primero el equipo A" << endl;
    a_archivo << "Lista del equipo A:" << endl;
    scrum scrumA;
    for (int i=0; i<8; i++) {
        cout << "Ingrese el nombre de su jugador:" << endl;
        cin >> scrumA.jugadores[i].nombre;
        cout << "Ingrese el peso de su jugador en kg:" << endl;
        cin >> scrumA.jugadores[i].peso;
        a_archivo << scrumA.jugadores[i].nombre << " " << scrumA.jugadores[i].peso << "kg" << endl;
    }
    cout << "El peso total del Scrum A es: " << scrumA.pesaje() << "kg" << endl;
    a_archivo << "Total: " << scrumA.pesaje() << "kg" << endl;
    
    cout << "Ahora el equipo B" << endl;
    a_archivo << "Lista del equipo B:" << endl;
    scrum scrumB;
    for (int i=0; i<8; i++) {
        cout << "Ingrese el nombre de su jugador:" << endl;
        cin >> scrumB.jugadores[i].nombre;
        cout << "Ingrese el peso de su jugador en kg:" << endl;
        cin >> scrumB.jugadores[i].peso;
        a_archivo << scrumB.jugadores[i].nombre << " " << scrumB.jugadores[i].peso << "kg" << endl;
    }
    cout << "El peso total del Scrum B es: " << scrumB.pesaje() << "kg" << endl;
    a_archivo << "Total: " << scrumB.pesaje() << "kg" << endl;
}
