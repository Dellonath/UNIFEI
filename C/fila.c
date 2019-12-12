#include <stdio.h>
#include <stdlib.h>

struct aluno{
    int matricula;
    char nome[30];
    float n1, n2, n3;
};

typedef struct Fila{
    int inicio, fim, qtd;
    struct aluno dados[100];
}fila;

fila *criafila(){
    fila *fi=(fila*) malloc(sizeof(struct Fila));
    if(fi!=NULL){
        fi->inicio=0;
        fi->fim=0;
        fi->qtd=0;
    }
    return fi;
}

void liberafila(fila *fi){
    free(fi);
}

int tamanhofila(fila *fi){
    if(fi==NULL){
        return -1;
    }
    return fi->qtd;
}

int filacheia(fila *fi){
    if(fi==NULL){
        return -1;
    }
    if(fi->qtd==100){
        return 1;
    }else{
        return 0;
    }
}

int filavazia(fila *fi){
    if(fi==NULL){
        return -1;
    }
    if(fi->qtd==0){
        return 1;
    }else{
        return 0;
    }
}

int inserefila(fila *fi, struct aluno al){
    if(fi==NULL){
        return 0;
    }
    if(filacheia(fi)){
        return 0;
    }
    fi->dados[fi->fim]=al;
    fi->fim=(fi->fim+1)%100;
    fi->qtd++;
    return 1;
}

int removefila(fila *fi){
    if(fi==NULL || filavazia(fi)){
        return 0;
    }
    fi->inicio=(fi->inicio+1)%100;
    fi->qtd--;
    return 1;
}

int consultafila(fila *fi, struct aluno *al){
    if(fi==NULL || filavazia(fi)){
        return 0;
    }
    *al=fi->dados[fi->inicio];
    return 1;
}

int main(){
    fila *fi=criafila();













}
