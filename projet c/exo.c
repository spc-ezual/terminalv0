#include <stdio.h>
#include <stdlib.h>
#include <time.h>



int main(int argc,char* argv[])
{
    if (argc!=2){
        printf("Gros nase, faut un unique argument ? \n");
    }else{
        int nbalea ;
        int resultat[6]={0,0,0,0,0,0};
        srand(time(NULL));

        for (int i=0;i<atoi(argv[1]);i++){
            // on fait un nombre entier entre 0 et 5 qui correspond a l'indice du tableau
            nbalea = rand()%6;
            resultat[nbalea]++;
        }
        for (int i = 0;i<=5 ;i++ ){
            printf("Face %d : %d\n",i+1,resultat[i]);
        }
    }
    return 0;
}

