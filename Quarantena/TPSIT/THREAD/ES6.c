#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<unistd.h>

//risorse comuni
int biglietti_disponibili = 10;
pthread_mutex_t c = PTHREAD_MUTEX_INITIALIZER; 

void *cassa(void *argv){
    int biglietti;
    pthread_mutex_lock(&c);    
    biglietti = 1 + rand() %10;
    printf("Nome:  %u,  voglio acquistare %d biglietti.\n" , pthread_self(), biglietti);
    if(biglietti_disponibili == 0){
        printf("Biglietti acquistati 0\n");
    }else if(biglietti > 0 && biglietti<= biglietti_disponibili){
        printf("Biglietti acquistati %d\n", biglietti);
        biglietti_disponibili -= biglietti;
    }else if(biglietti > 0 && biglietti > biglietti_disponibili){
        printf("Biglietti acquistati %d\n" , biglietti_disponibili);
        biglietti_disponibili = 0;
    }
    printf("%d biglietti rimasti.\n" , biglietti_disponibili);
    pthread_mutex_unlock(&c); //FINE SEZIONE CRITICA

    pthread_exit(NULL);
}

int main(int argc, char **argv){
    pthread_t clienti[10];
    int i;
    for(i=3; i>0; i--){
        printf("Apertura cassa tra %d...\n" , i);
        sleep(1);
    }

    srand(time(NULL)); //10 clienti
    for(i=0; i<10; i++){
        pthread_create(&clienti[i], NULL, (void*) cassa, NULL);
    }

    for(i=0; i<10; i++){
        pthread_join(clienti[i], NULL); //chiudo
    }

    printf("ACQUISTO FINITO (TERM.)\n");
    return 0;
}