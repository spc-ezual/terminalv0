#include <stdio.h>

double cal_racine(double nb){
	double racine=1;
	int i = 0;
	//printf("%f %f %f %d",fraction,nombreBase,somme,i);
	while(i<100){
		printf("%.30f \n",racine);
		racine=0.5*(racine+(nb/racine));
		i++;
	}
	return racine;
}

int main(void){
	float racineDe = 0;
	printf("Nombre : ");
	scanf("%f",&racineDe);
	//printf("nombre : %f",racineDe);
	double racine= cal_racine(racineDe);
	printf("racine de %.2f = %f",racineDe,racine);
	int i = 1 ;
	while(i>0){
		printf("");
	}
	
	return 0;
}

