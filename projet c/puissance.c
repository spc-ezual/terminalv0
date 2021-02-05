#include <stdio.h>

long long puissance (short  nb,short puis){
	short i = 0;
	long long rep=1;
	//printf("%f ** %f \n",nb,puis);
	while (i<puis){
		//printf("%d",i);
		rep = rep * nb;
		i++;
	}
	return rep;
}
int main(void){
	short nomb=0;
	short puis=0;
	long long resultat;
	printf("nb : ");
	scanf("%d",&nomb);
	printf("puissance : ");
	scanf("%d",&puis);
	printf("%d ** %d \n",nomb,puis);
	resultat= puissance(nomb,puis);
	printf("%d",resultat);
	
	return 0;
}
// probleme :
//	le nombre nommé "nomb" devien egal à 0 à la suite del'attribution de la valeur à la puissance.