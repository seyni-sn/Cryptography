#include <stdio.h>
#include <stdlib.h>
#define ENTREE "entree.txt"
#define SORTIE "sortie.txt"
#define SORTIEDEC "sortiedec.txt"
#include<ctype.h>
#include <string.h>
#define N 100
//#define char[255] chaine;

void affichAscii();
char lireChar();
void affichChacr(char);
int cryptChar(int, int);
int decryptChar(int, int);
int cesarCrypt(int, int);
//void cryptChaine(int k);
//cryptFichier()
int determineClef(char*);
