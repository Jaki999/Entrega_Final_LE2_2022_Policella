#include <iostream>

using namespace std;

#define INV1 1
#define INV2 2
#define INV3 3
#define INV4 4
#define INV5 5
#define DEFAULT 6

int temp1=10;
int temp2=12;
int temp3=34;
int temp4=28;
int temp5=20;
int estado;

void medir1();
void medir2();
void medir3();
void medir4();
void medir5();
void MdE();

void(*func)(void) = medir1;

int main() {
    cout << "elija que numero de invernadero quiere:" << endl;
    cin >> estado;
    MdE();
}

void medir1() {
    cout << "la temperatura (grados celcius) del invernadero 1 es:" << temp1 << endl;
}

void medir2() {
    cout << "la temperatura (grados celcius) del invernadero 2 es:" << temp2 << endl;
}

void medir3() {
    cout << "la temperatura (grados celcius) del invernadero 3 es:" << temp3 << endl;
}

void medir4() {
    cout << "la temperatura (grados celcius) del invernadero 4 es:" << temp4 << endl;
}

void medir5() {
     cout << "la temperatura (grados celcius) del invernadero 5 es:" << temp5 << endl;  
}

void MdE() {
    switch (estado)
    {   
        case DEFAULT:
            break;

        case INV1:
            func();
            break;
        
        case INV2:
            func = &medir2;
            func();
            break; 
        
        case INV3:
            func = &medir3;
            func();
            break;
        
        case INV4:
            func = &medir4;
            func();
            break;
        
        case INV5:
            func = &medir5;
            func();
            break;    
    }
}