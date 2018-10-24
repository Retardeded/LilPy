# Useless-CS-Projects

//author: Piotr Kurek
#include <stdio.h>
#include <math.h>
#include <string.h>

void correctingNames(char name1[],int n, int numberOfSpaces1)
{
	int i = 0;
	i = n-1;
	name1[n] = '|';
	while(i >= 0)
	{
		if(i <= n - numberOfSpaces1)
		{
			name1[i + numberOfSpaces1-1]  = name1[i];
		}
		i--;
	}
	i = 0;
	while(i < numberOfSpaces1-1)
	{
		name1[i] = ' ';
		i++;
	}
	name1[0] = '|';
}
int main(void) {
	
int n = 14;
char name1[n+1];
char name2[n+1];
char usefullString[] = "|  km/h|   m/h|";
int numberOfSpaces1 = 0;
int numberOfSpaces2 = 0;
scanf("%s", name1);
scanf("%s", name2);
int kmPH;
scanf("%d", kmPH);
int i = 0;

numberOfSpaces1 = n-strlen(name1)+1;
numberOfSpaces2 = n-strlen(name2)+1;

printf("%d", numberOfSpaces2);
printf("\n");
correctingNames(name1, n, numberOfSpaces1);
correctingNames(name2, n, numberOfSpaces2);
printf("\n");
printf("---------------");
printf("\n");
printf(name1);
printf("\n");
printf(name2);
printf("---------------");
printf(usefullString);
printf("---------------");

}
