#include <stdio.h>
#include <stdlib.h>

typedef struct Pilha{
	int valor;
	struct Pilha *proximo;
}pilha;

pilha *topo, *topo2;

pilha *iniciapilha(){  //inicia uma nova pilha 
	pilha *p;                           
	p=(pilha *) malloc(sizeof(pilha));  
	topo=p;                             
	topo->proximo=NULL;                    
	return p;
}

void empilhar(pilha *p, int x){    //adiciona uma nova célula à pilha e coloca-a como topo
	pilha *g;
	g=(pilha *) malloc(sizeof(pilha)); 
	g->proximo=topo;   
	g->valor=x;
	topo=g;
}

void desempilhar(pilha *p){  //recebe a pilha e desempilha a última célula
	pilha *aux;
	aux=topo;
	topo=topo->proximo;
	free(aux);
}

void imprime(pilha *p){   //mostra termo a termo da pilha e retorna o *topo ao topo
	pilha *aux;
	aux=topo;
    while(topo->proximo!=NULL){
		printf("%d  ", topo->valor);
		topo=topo->proximo;
        }
    topo=aux;
    }

//a função abaixo está excluindo alguns pares quando seguidos de ímpares

void pilhavazia(pilha *p){   //verifica se a pilha está vazia 
    if(topo->proximo==NULL){
        printf("A pilha está vazia!\n");
    }else{
        printf("A pilha não está vazia!\n");
    }
}

void retiraimpares(pilha *p){  //retira todas as células ímpares da pilha e mantém a ordem
    pilha *aux=topo;
    int *v, qtd=0, k=0, j;
    
    while(topo->proximo!=NULL){
        if(topo->valor%2==0){
            qtd++;
        }
        topo=topo->proximo;
    }
    topo=aux;  //ponteiro retorna topo
    
    v=(int *) malloc(qtd*sizeof(int));  //vetor de inteiros para guardar os pares
    
    while(topo->proximo!=NULL){ //percorrendo a pilha e recolhendo os pares
        if(topo->valor%2==0){
            v[k]=topo->valor;
            k++;
            topo=topo->proximo;
        }else{
            topo=topo->proximo;
        }
    }
    topo=aux;
    
    while(topo->proximo!=NULL){
        desempilhar(p);
    }
    
    for(j=qtd-1;j>=0;j--){  //empilhemos novamente utilizando o vetor v invertido-o, fazemos qtd-1 pois a contagem é regressiva até 0
        empilhar(p, v[j]);
    }
}
    

float mediapares(pilha *p){   //a função retorna a média da pilha, desempilhando-a célula a célula
	pilha *aux;
	float soma=0, i=0;
	while(topo->proximo!=NULL){
		i++;
		soma=soma+topo->valor;
		topo=topo->proximo;
		free(aux);
		aux=topo;
	}
	soma=soma/i;
	return soma;
}

void concatena(pilha *p1, pilha *p2){
	pilha *aux=topo;
	while(topo->proximo!=NULL){
		topo=topo->proximo;
	}
	topo->valor=topo2->valor;
	topo->proximo=topo2->proximo;
	topo=aux;
}

int main(){
	pilha *g, *g2, *aux;
	int i;
	g=iniciapilha();
	
	printf("Empilhando os valores 1, 2, ..., 10\n");
	for(i=1;i<=10;i++){
		empilhar(g, i);
	}
	printf("Pilha: ");
	imprime(g);
	printf("\n");

	printf("Retirando os primos da pilha \n");
	retiraimpares(g);

	printf("Pilha:  ");
	imprime(g);

	printf("\nCalculando média dos pares");
	printf("\n%.2f", mediapares(g));
	
	printf("\nEmpilhando os valores 1, 2, ..., 5 na pilha 1");
	for(i=1;i<6;i++){
	    empilhar(g, i);
	}
	topo2=topo;
	printf("\nEmpilhando os valores 6, 7, ..., 10 na pilha 2\n");
	g2=iniciapilha();
	for(i=6;i<11;i++){
	    empilhar(g2, i);
	}
	concatena(g, g2);
	printf("Pilha 1 e 2 concatenadas\n");
	imprime(g);

	while(topo->proximo!=0){
		aux=topo;
		topo=topo->proximo;
		free(aux);
	}
}
























