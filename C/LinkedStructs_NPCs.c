#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int cantidadNPCs;

struct NPCs {
    int id;
    struct NPCs *next;
} npc;

typedef struct NPCs* puntero;
puntero p_npc = &npc;

void agregarNPC (void);

int main() {
    printf ("\n Cuantos NPCs desea ingresar? ");
    scanf ("%d", &cantidadNPCs);  
    agregarNPC();
}

void agregarNPC (void) {
    srand(time(NULL));
    for(int i = 0; i<cantidadNPCs; i++){
        int prn = rand();
        
        p_npc->next = malloc(sizeof(puntero));
        p_npc->id = prn;
        
        printf("\n El npc %d tiene el siguiente ID: %d",i , p_npc->id);
    }
}
