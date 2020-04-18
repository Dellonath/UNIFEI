#include <stdio.h>
#include <stdlib.h>

/*
This algorithm orders an int vector with n elements drawn using Bubble Sort
*/

void bubble_sort(int v[], int n, int i, int j){
    
    if(j != n){
        if(v[i] > v[j]){
            int aux;
            aux = v[i];
            v[i] = v[j];
            v[j] = aux;
            bubble_sort(v, n, 0, 1);
        }else{
            bubble_sort(v, n, i + 1, j + 1);
        }
    }else{
        return ;
    }
}

int main(){
    int *v, valor, n;
    printf("Write the size of vector: ");
    scanf("%d", &n);
    
    v = (int *) malloc(n * sizeof(int));
    
    for(int i = 0;i < n; i++){
        v[i] = rand() % 100;
    }
    
    for(int i = 0;i < n; i++){
        printf("%d ", v[i]);
    }
    
    bubble_sort(v, n, 0, 1);
    printf("\n");
    for(int i = 0;i < n; i++){
        printf("%d ", v[i]);
    }
    return 0;
}
