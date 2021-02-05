#include <stdio.h>
#include <math.h>

double logNep(double nb){
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

int main(void){
	float nombrePourLeLn = 0;
	printf("Nombre : ");
	scanf("%f",&nombrePourLeLn);
	//printf("nombre : %d",nombrePourLeLn);
	double lognp= logNep(nombrePourLeLn);
	printf("ln(%f)=%.10f",nombrePourLeLn,lognp);
	int i = 1 ;
	while(i>0){
		printf("");
	}
	
	return 0;
}

