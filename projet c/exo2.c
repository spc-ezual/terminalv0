#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int* nlance(int nb_lancer){
        int nbalea ;
        calloc(6,sizeof(int));
        int* resultat = (int*) calloc(6,sizeof(int));
        //int resultat[6]={0,0,0,0,0,0};
        srand(time(NULL));
        for (int i=0;i<nb_lancer;i++){
            // on fait un nombre entier entre 0 et 5 qui correspond a l'indice du tableau
            nbalea = rand()%6;
            resultat[nbalea]++;
        }
    
    return resultat;
}

int main(int argc,char* argv[])
{
    if (argc!=2){
        printf("Gros nase, faut un unique argument ? \n");
    }else{
    int* tab_res=nlance(atoi(argv[1]));
    for (int i = 0;i<=5 ;i++ ){
        printf("Face %d : %d\n",i+1,tab_res[i]);
    }
    return 0;
    }
}

