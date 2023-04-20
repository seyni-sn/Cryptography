#include "fichier.h"
#include <stdio.h>
#include <stdlib.h>
#define ENTREE "entree.txt"
#define SORTIE "sortie.txt"
//#define SORTIEDEC "sortiedec.txt"
int main(void)
{
    int crypt, decrypt, k;
    k = 3;
    int clef =0;

    FILE *f_in, *f_out; int c;
    if ((f_in = fopen(ENTREE,"r")) == NULL)
      {
         fprintf(stderr, "\nErreur: Impossible de lire le fichier %s\n",ENTREE);
         return(EXIT_FAILURE);
       }
    if((f_out = fopen(SORTIE,"w")) == NULL)
      {
         fprintf(stderr, "\nErreur: Impossible d'ecrire dans le fichier %s\n", SORTIE);
         return (EXIT_FAILURE);
       }
  while ((c = fgetc(f_in)) != EOF)
    {

      //affichChacr(c);
      crypt = cesarCrypt(c,k);
      //printf("Voici le caractaire crypte\n");
      //affichChacr(crypt);
      //decrypt = cesarDecrypt(crypt, k);
      //printf("Voici le caractaire decrypte\n");
      //affichChacr(decrypt);
      fputc(crypt, f_out);
    }
  fclose(f_in); fclose(f_out);
  //return(EXIT_SUCCESS);
  printf("Decodage du text");
  clef = determineClef(SORTIEDEC);
  printf("La clef %d\n",clef );
  }
