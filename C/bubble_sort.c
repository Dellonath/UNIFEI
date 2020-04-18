#include <stdio.h>
#include <stdlib.h>

/*
This algorithm orders a int vector with n elements drawn using Bubble Sort by recurrence.
*/

void bubble_sort(int v[], int n, int i, int j){
    
    if(j != n){
        if(v[i] > v[j]){ // verify and swap the elements
            int aux;
            aux = v[i];
            v[i] = v[j];
            v[j] = aux;
            bubble_sort(v, n, 0, 1); // returns to position 0
        }else{
            bubble_sort(v, n, i + 1, j + 1); // forward
        } 
    }else{
        return ;
    }
}

void main(){
    int *v, valor, n;
    printf("Write the size of vector: ");
    scanf("%d", &n);
    
    v = (int *) malloc(n * sizeof(int)); // allocates a vector with n elements
    
    for(int i = 0;i < n; i++){
        v[i] = rand() % 100; // function rand() return a random int number
    }
    
    for(int i = 0;i < n; i++){
        printf("%d ", v[i]); // print the vector before the bubble sort
    }
    
    bubble_sort(v, n, 0, 1);
    
    printf("\n");
    for(int i = 0;i < n; i++){
        printf("%d ", v[i]); // print the vector after the bubble sort
    }
}

