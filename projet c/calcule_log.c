#include <stdio.h>
#include <math.h>

double logNep(float nb){
	double fraction = (1-nb)/(nb+1);
	double nombreBase = 1;
	double somme = 0;
	int i = 0;
	//printf("%f %f %f %d",fraction,nombreBase,somme,i);
	while(i<10000){
		somme = somme + ((1/nombreBase)* pow( fraction, nombreBase));
		//printf("%.2000f ",somme);
		nombreBase+=2;
		i++;
	}
	double resultat = somme * (-2);
	return resultat;
}
double loga(int base,float nombre){
	double resultat = logNep(nombre)/logNep(base);
	return resultat;
}
int main(void){
	int base = 0;
	float nombre = 0;

	printf("Format: log base y (x) \n");
	printf("y : ");
	scanf("%d",&base);
	printf("x : ");
	scanf("%f",&nombre);
	double log= loga(base,nombre);
	printf("log%d(%f)=%.10f",base,nombre,log);
	int i =1;
	while(i>0){
		printf("");
	}
	return 0;
}