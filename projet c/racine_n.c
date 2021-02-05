#include <stdio.h>
float cal_racine(long nb,long n){
	float racine=1;
	long i = 0;
    long inter = 0;
	printf("%d %d",nb,n);
	while(i<100){
		printf("%.30f \n",racine);
        inter = puissan(racine,n-1);
		racine=(1/n)*(racine*(n-1)+(nb/inter));
		i++;
	}
	return racine;
}

long puissan (long nb,long puis){
	long i = 0;
	long rep=1;
	printf("%f ** %f \n",nb,puis);
	while (i<puis){
		//printf("%d",i);
		rep = rep * nb;
		i++;
	}
	return rep;
}
int main(void){
	long racineDe = 0;
    long n =0;
    printf("Nombre : ");
	scanf("%d",&racineDe);
	printf("n : ",racineDe);
	scanf("%d",&n);
    printf("%d %d",racineDe,n);
	long racine= cal_racine(racineDe,n);
	printf("racine de %.2f = %f",racineDe,racine);
	
	return 0;
}