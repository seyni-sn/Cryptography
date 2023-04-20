#include <stdio.h>
#include <stdlib.h>
#include<ctype.h>
#include<string.h>
#include<time.h>

#define N 100
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int Gen();
int Enc(int k, int xi);
int Dec(int k, int yi);

int main(int argc, char *argv[]) 
{
	int xi = 0, yi = 0,k = 0, i = 0, rep = 0;
	char TextClr[N], TextCript[N], c = 0;
	printf("Donner le texte en claire:\n");
	gets(TextClr);
	
	k = Gen();
	
	while(i < strlen(TextClr))
		{
			xi = TextClr[i] - 65;
			yi = Enc(xi, k);
			TextCript[i] = yi + 65;				
			i++;
			
		}
		
	printf("Le texte cripte est le siuvant:\n");
	printf("%s\n\n", TextCript);
	
	do
	{
		printf("voulez decripter le message ?\n");
		printf("1:oui!\n");
		printf("2:non!\n");
		scanf("%d", &rep);
	}while(rep != 1 && rep != 2);
	if(rep == 1)
		{
		 	while(i < strlen(TextCript))
				{
					yi = TextCript[i] - 65;
					xi = Dec(yi, k);
					TextClr[i] = xi + 65;				
					i++;	
				}
			printf("Text en cLaire:\n");
			printf("%s\n", TextClr);
		}
	else exit(0);
	return 0;
}


int Gen()
{
	int k = 0;
	int const MAX = 127, MIN = 0;
	srand(time(NULL));
	k = (rand() % (MAX - MIN)) + MIN;
	return k;
}
	 
int Enc(int xi, int k)
{
	return (xi + k) % 127;
}
	
int Dec(int yi, int k)
{
	return (yi - k) % 127;
}
