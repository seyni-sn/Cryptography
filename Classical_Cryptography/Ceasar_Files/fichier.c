#include "fichier.h"
//#define SORTIEDEC "sortiedec.txt"

void affichAscii() {
  int i;
  for(i=0;i<255;i++)
    {
      printf("%c",i );
    }
}

char lireChar()
  {
    char a;
    printf("Entrer un caractaire:\n");
    //scanf("%c",&a);
    a=getchar();
    return a;
  }

  void  affichChacr(char a)
    {
      printf("%c\n",a );
    }

int cryptChar(int x,int k)
    	{
    		return (x+k)%26;
    	}

/*void cryptChaine(int k)
  {
    int i;
    char TextClr[N]={0},TextCript[N]={0};
    int crypt = 0;
    printf("Donner le texte en claire:\n");
    gets(TextClr);
    //scanf("%s\n", TextClr);
    for(i=0; i<strlen(TextClr); i++)
      {
        crypt = cesarCrypt(TextClr[i],k);
        TextCript[i] = crypt;
      }
    puts(TextCript);
  }*/

int decryptChar(int y,int k)
      	{
      		return (y-k+26)%26;
      	}

int cesarCrypt(int c, int k)
  {
    int x, y, crypt;
    if(isupper(c)!=0)
      {
        x = c-65;
        y = cryptChar(x,k);
        crypt=y+65;
      }
    else if(islower(c)!=0)
      {
        x = c-97;
        y = cryptChar(x,k);
        crypt = y+97;
      }
    else crypt = c;

    return crypt;
  }

int cesarDecrypt(int c, int k)
  {
    int x, y, crypt;
    if(isupper(c)!=0)
      {
        y = c-65;
        x = decryptChar(y,k);
        crypt=x+65;
      }
    else if(islower(c)!=0)
      {
        y = c-97;
        x = decryptChar(y,k);
        crypt = x+97;
      }
    else crypt = c;

    return crypt;
  }


  int determineClef(char* s)
  {
    int crypt, decrypt, k;
    k =0;
    int rep = 0;

    while(!rep)//A revoire boucle infinie
    {
      FILE *f_in, *f_out; int c;
      if ((f_in = fopen(SORTIE,"r")) == NULL)
        {
           fprintf(stderr, "\nErreur: Impossible de lire le fichier %s\n",ENTREE);
           return(EXIT_FAILURE);
         }
      if((f_out = fopen(s,"w")) == NULL)
        {
           fprintf(stderr, "\nErreur: Impossible d'ecrire dans le fichier %s\n", SORTIE);
           return (EXIT_FAILURE);
         }
      while ((c = fgetc(f_in)) != EOF)
        {

          //affichChacr(c);
          //crypt = cesarCrypt(c,k);
          //printf("Voici le caractaire crypte\n");
          //affichChacr(crypt);
          decrypt = cesarDecrypt(c, k);
          //printf("Voici le caractaire decrypte\n");
          //affichChacr(decrypt);
          fputc(decrypt, f_out);
          printf("%c\n",decrypt );
        }
      fclose(f_in); fclose(f_out);
      //fprintf(stdout, "%s\n",s);
      return(EXIT_SUCCESS);
      while(rep != 0 && rep !=1 )
        {
          printf("Repondre par oui ou non!\n");
          printf("Taper 1-> OUI \n ou 0->NON\n");
          scanf("%d\n", &rep );
        }

      k++;
    }

    return k-1;

  }
