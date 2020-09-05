/*
COM120 - Sistemas Operacionais - LE04 - 05/09/2020 00:55
Douglas Raimundo de Oliveira Silva
2019018540
Exercício 04 sobre fork() e pipe()
*/

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <math.h>

int *square(int *x){ // função para calcular o fatorial e retornar o endereço de memória onde fora calculado
	for(int i = *x-1; i >= 1; i--) *x = (*x)*i;
	return x;
}

int *factorial(int *x){ // função para calcular o quadrado e retornar o endereço de memória onde fora calculado
	*x = pow(*x, 2);
	return x;
}

int main(){
    int p[2], aux1[1], aux2[2], pida = 0, pidb = 0, num, *x = &num; // declaranumdo os ponteiros, o vetor para pipe e os inteiros necessários
    printf("Digite um número: ");
    scanf("%d", &num);

    if((pipe(p)) < 0) return 0; // criando o file descriptor e checando sucesso
    if((pida = fork()) < 0) return 0; // criando o primeiro processo FILHO A e checando sucesso
    if((pidb = fork()) < 0) return 0; // criando o primeiro processo FILHO B e checando sucesso

    if(pida != 0 && pidb != 0){ // Verifica se é o processo pai
        close(p[1]);
        for(int i = 0; i < 2; i++){
       	    read(p[0], aux1, sizeof(int)); // lendo o file descriptor
            aux2[i] = *aux1; // jogando no array res os resultados do quadrado em res[0] e fatorial em res[1]
        }
        close(p[0]);
        printf("%d²+%d! = %d\n", num, num, aux2[0] + aux2[1]); // printando a soma pelo processo pai

    }else{
    	if(pida != 0) write(p[1], square(x), sizeof(int));  // atribuindo função ao filho A
    	if(pidb != 0) write(p[1], factorial(x), sizeof(int));  // atribuindo função ao filho B
    }
}

