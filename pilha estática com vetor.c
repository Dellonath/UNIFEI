#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#define MAX 10

typedef struct{
    int item[MAX];
    int topo;
}pilha;

void pilhainicia(pilha *p){
    p->topo=-1;
}

int pilhavazia(pilha *p){
    if(p->topo==-1){
        return 1;
    }else{
        return 0;
    }
}

int pilhacheia(pilha *p){
    if(p->topo==MAX-1){
        return 1;
    }else{
        return 0;
    }
}

void pilhainsere(pilha *p, int x){
    if(pilhacheia(p)==1){
        printf("\nERROR: Pilha cheia\n");
    }else{
        p->topo++;
        p->item[p->topo]=x;
    }
}

int pilharemove(pilha *p){
    int aux;
    if(pilhavazia(p)==1){
        printf("\nERROR: Pilha vazia\n");
    }else{
        aux=p->item[p->topo];
        p->topo--;
        return aux;
    }
}  

void pilhamostrar(pilha *p){
    int i;
    printf("\n");
    for(i=1;i<=p->topo;i++){
    printf("%d ", p->item[i]);
    }
    printf("\n");
}
    
int main(){
    pilha *p=(pilha *) malloc(sizeof(pilha));
    int opcao=0, x, aux;
    printf("Pilha Iniciada!\n");
    while(opcao!=6){
        printf("\nDigite uma das opções:\n1-Verificar se a Pilha está vazia\n");
        printf("2-Verificar se a Pilha está cheia\n3-Inserir na Pilha\n4-Remover da Pilha\n5-Mostrar Pilha\n6-Sair\nOpção: ");    
        scanf("%d", &opcao);
        switch(opcao){
            case 1:
            if(pilhavazia(p)==1){
                printf("\nPilha Vazia!\n");
            }else{
                printf("\nPilha não está vazia!\n");
            }
            break;
            
            case 2:
            if(pilhacheia(p)==1){
                printf("\nPilha Cheia!\n\n");
            }else{
                printf("\nPilha não está cheia!\n");
            }
            break;
            
            case 3:
            printf("\nDigite o valor a ser inserido: ");
            scanf("%d", &x);
            printf("\n\n");
            pilhainsere(p, x);
            break;
            
            case 4:
            aux=pilharemove(p);
            break;
            
            case 5:
            pilhamostrar(p);
            break;
            
            case 6:
            opcao=6;
            printf("\nPrograma Encerrado!\n\n");
            break;
            
            scanf("%d", &opcao);
        }
    } 
}