#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct Deque{
	char valor;
	struct Deque *proximo;
	struct Deque *anterior;
}deque;

struct Deque *direita;	
struct Deque *esquerda;

deque *iniciadeque(char c){
	deque *d;
	d=(deque *) malloc(sizeof(deque));
	d->proximo=NULL;
	d->anterior=NULL;
	d->valor=c;
    direita=d;
    esquerda=d;
	return d;
}

void inseredireita(char v){
	deque *d, *aux=direita;
	d=(deque *) malloc(sizeof(deque));
	d->valor=v;
	direita->proximo=d;
	direita=d;
	direita->anterior=aux;
	direita->proximo=NULL;
}

void removedireita(){
    deque *aux=direita;
	direita=direita->anterior;
	direita->proximo=NULL;
	free(aux);
}

void insereesquerda(char v){
	deque *d, *aux=esquerda;
	d=(deque *) malloc(sizeof(deque));
	d->valor=v;
	esquerda->anterior=d;
	esquerda=d;
	esquerda->proximo=aux;
	esquerda->anterior=NULL;
}

void removeesquerda(){
    deque *aux=esquerda;
	esquerda=esquerda->proximo;
	esquerda->anterior=NULL;
	free(aux);    
}

void imprimeiniciofim(){
	deque *aux=esquerda;
	while(esquerda!=NULL){
		printf("%c", esquerda->valor);
		esquerda=esquerda->proximo;
	}
	esquerda=aux;	
}

void imprimefiminicio(){
	deque *aux=direita;
	while(direita!=NULL){
		printf("%c", direita->valor);
		direita=direita->anterior;
	}
	direita=aux;	
}
// criar dois vetores e fazer um receber a palavra e outro receber a palavra invertida e ver se são iguais usando strcmp
void palindromo(){
	deque *aux=esquerda, *aux2=direita;
	int i=0, k;
	char *a, *b;
	while(esquerda!=NULL){
	    i++;
	    esquerda=esquerda->proximo;
	}
	esquerda=aux;
	a=(char *) malloc(i*sizeof(char));
	b=(char *) malloc(i*sizeof(char));
	k=i;
	for(i=0;i<k;i++){
	    a[i]=esquerda->valor;
	    esquerda=esquerda->proximo;
	}
	for(i=0;i<k;i++){
	    b[i]=direita->valor;
	    direita=direita->anterior;
	}
	if(strcmp(a, b)==0){
	    printf("A palavra é um Palíndromo!\n");
	}else{
	    printf("A palavra não é um Palíndromo!\n");
	}
	esquerda=aux;
	direita=aux2;
	free(a);
	free(b);
}

int main(){
    deque *deq, *auxiliar;
    char c;
    int i=1, escolha=10;
	
    printf("Com qual letra deseja iniciar o DEQUE? ");
    scanf(" %c", &c);
    deq=iniciadeque(c);
    system("clear");
    while(escolha!=0){
    system("clear");
    printf("SELECIONE UMA DAS OPÇÕES ABAIXO\n1-Adicionar à direita\n2-Adicionar à esquerda\n3-Remover da direita\n4-Remover da esquerda");
    printf("\n5-Imprimir DEQUE da esquerda pra direita\n6-Imprimir DEQUE da direita para esquerda\n7-Verificar se é Palíndromo\n8-Sair\nO que deseja fazer? ");
    scanf("%d", &escolha);
    system("clear");
    switch(escolha){
        case 1:
        printf("Digite a letra que deseja inserir: ");
        scanf(" %c", &c);
        inseredireita(c);
        printf("Realizar outra ação (1-sim 0-não)? ");
        scanf("%d", &escolha);
        system("clear");
        break;
        
        case 2:
        printf("Digite a letra que deseja inserir: ");
        scanf(" %c", &c);
        insereesquerda(c);
        printf("Realizar outra ação (1-sim 0-não)? ");
        scanf("%d", &escolha);
        system("clear");
        break;
        
        case 3:
        if(direita==esquerda){
            printf("Não é possível remover!");
            printf("\nRealizar outra ação (1-sim 0-não)? ");
            scanf("%d", &escolha);
            system("clear");
        }else{
            printf("Removido da esquerda com sucesso!");
            removedireita();
            printf("\nRealizar outra ação (1-sim 0-não)? ");
            scanf("%d", &escolha);
            system("clear");    
        }
        break;
        
        case 4:
        if(direita==esquerda){
            printf("Não é possível remover!");
            printf("\nRealizar outra ação (1-sim 0-não)? ");
            scanf("%d", &escolha);
            system("clear");
        }else{
            printf("Removido da esquerda com sucesso!");
            removeesquerda();
            printf("\nRealizar outra ação (1-sim 0-não)? ");
            scanf("%d", &escolha);
            system("clear");    
        }
        break;
        
        case 5:
        printf("Deque da esquerda pra direita: ");
        imprimeiniciofim();
        printf("\nRealizar outra ação (1-sim 0-não)? ");
        scanf("%d", &escolha);
        system("clear");
        break;
        
        case 6:
        printf("Deque da direita pra esquerda: ");
        imprimefiminicio();
        printf("\nRealizar outra ação (1-sim 0-não)? ");
        scanf("%d", &escolha);
        system("clear");
        break;
        
        case 7:
        palindromo();
        printf("Realizar outra ação (1-sim 0-não)? ");
        scanf("%d", &escolha);
        system("clear");
        break;

	case 8:
	escolha=0;
	break;
        }
    }
    while(esquerda!=NULL){
        auxiliar=esquerda;
        esquerda=esquerda->proximo;
        free(auxiliar);
    }
    printf("Programa finalizado com sucesso!\n");
}
