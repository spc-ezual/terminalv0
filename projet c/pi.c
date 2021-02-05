#include <stdio.h>
#include <math.h>
double calc_pi(void){
	double pi_val=0;
	int i = 0;
	//printf("%f %f %f %d",fraction,nombreBase,somme,i);
	while(i<1000000000){
		//printf("%.30f \n",pi_val);
		pi_val=pi_val+(4*pow((-1),i))/(2*i+1);
		i++;
	}
	return pi_val;
}

int main(void){
	double pi = calc_pi();
	int i = 1 ;
	printf("%.30f",pi);
	return 0;
}

//3.141592643589368600000000000000
//3.141592653589793