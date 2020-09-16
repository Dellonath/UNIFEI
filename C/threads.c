/*
COM120 - Sistemas Operacionais - EP03 - 16/09/2020 12:40
Douglas Raimundo de Oliveira Silva
2019018540
Exercício Prático 03
*/

#include <stdio.h> 
#include <stdlib.h> 
#include <pthread.h> 

int min_value, max_value; // variáveis globais
float mean_value = 0.0;

typedef struct parameters{ // struct para enviar dois argumentos (tamanho do vetor e o vetor) para a função no pthread_create()
	int *arg1; // armazena o vetor
	int arg2; // armazena o tamanho do vetor
}args;

void mean(args *A){ 
	for(int i = 0; i < A[0].arg2; i++) mean_value += A->arg1[i]; // somando os valores do vetor
    mean_value /= A[0].arg2; // dividindo pelo tamanho do vetor
}

void max(args *A){
	max_value = A->arg1[0]; // tomando o primeiro valor
	for(int i = 1; i < A[0].arg2; i++){ // percorrendo o vetor
		if(A->arg1[i] > max_value){ // tomando o maior valor
			max_value = A->arg1[i]; // trocando valores
		}
	}
}

void min(args *A){ 
	min_value = A->arg1[0]; // tomando o primeiro valor
	for(int i = 1; i < A[0].arg2; i++){ // percorrendo o vetor
		if(A->arg1[i] < min_value){ // tomando o menor valor
			min_value = A->arg1[i]; // trocando valores
		}
	}
}

int main(int argc, char *argv[]){ // recebendo os parâmetros do terminal
	pthread_t thread_id1, thread_id2, thread_id3; // criando os identificadores das threads
	int A[atoi(argv[1])]; // alocando um vetor do tamanho do parâmetro enviado
	args params[1]; // criando args para argumento

    for(int i = 0; i < atoi(argv[1]); i++) A[i] = rand() % 100; // gerando valores aleatórios de 0 a 100

    params[0].arg1 = A; // armazenando o vetor como argumento
    params[0].arg2 = atoi(argv[1]); // armazenando o tamanho do vetor como argumento

    printf("Vetor: ");
    for(int i = 0; i < atoi(argv[1]); i++) printf("%d ", A[i]); // printando o vetor

    if(pthread_create(&thread_id1, NULL, (void *) mean, params) != 0) return 0; // iniciando thread e checando êxito
    if(pthread_create(&thread_id2, NULL, (void *) max, params) != 0) return 0; // iniciando thread e checando êxito
    if(pthread_create(&thread_id3, NULL, (void *) min, params) != 0) return 0; // iniciando thread e checando êxito

    pthread_join(thread_id1, NULL);
    printf("\n\nThread_Mean Finalizado\n"); // finalizando a thread
    pthread_join(thread_id2, NULL);
    printf("Thread_Max Finalizado\n");// finalizando a thread
    pthread_join(thread_id3, NULL);
    printf("Thread_Min Finalizado\n");// finalizando a thread

    printf("\nMédia: %f \nMáximo: %d \nMínimo: %d\n", mean_value, max_value, min_value); // printando resultados
 
}