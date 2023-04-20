#include <stdio.h>
#include <stdlib.h>
#include<string.h>
#define N 255



int main()
{
    char textEnClaire[N], cle[27], texCrypt[N];
      int i, j, index;

      printf("Enter le text en claire : \n");
      gets(textEnClaire);

      printf("Entrer une cle de a a z : \n");
      for(i=0; i < 26; i++)
      {
            printf("%c-", i + 97);//la premiere lettre de la cle represente a ainsi de siute jusqua z
            cle[i] = getch();//on recupere la clef lettre par lettre
            printf("%c , ", cle[i]);//on affache a chaque intantanement la lettre donnee
      }

      for(i = 0; i < strlen(textEnClaire); i++)//cryptage
      {
           /*switch(textEnClaire[i])
           {
               case ' ':texCrypt[i]=' ';
               break;
               case '.':texCrypt[i]='.';
               break;
               case '!':texCrypt[i]='!';
               break;
               case '?':texCrypt[i]='?';
               break;
               case '_':texCrypt[i]='_';
               break;
               case '-':texCrypt[i]='-';
               break;
               default:{
                            index=textEnClaire[i]-97;/*je prend la valeur de la lettre dans la quel j'enleve de la lettre a
                            pour obtenir l'index de la lettre correspondante dans permutation(cle)*/
          	texCrypt[i]=cle[index];//la lettre i du text en claire est crupter par son image par la permutation

                        //}
                //break;
           //}

          	index=textEnClaire[i]-97;/*je prend la valeur de la lettre dans la quel j'enleve de la lettre a
                            pour obtenir l'index de la lettre correspondante dans permutation(cle)*/
        	texCrypt[i]=cle[index];

      }

      printf("Le Text crypte est: \n\n");
      for(i=0;i<strlen(textEnClaire);i++)
      {
            printf("%c",texCrypt[i]);
      }

      return 0;

}
