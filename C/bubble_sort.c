/*
This algorithm orders a vector(int) with n elements drawn using Bubble Sort by 
recurrence with a variation: at each exchange the algorithm restarts
*/

#include <stdio.h>
#include <stdlib.h>

void bubble_sort(int v[], int n, int i){
    
    if(i + 1 != n){
        if(v[i] > v[i + 1]){ // verify and swap the elements
            int aux;
            aux = v[i];
            v[i] = v[i + 1];
            v[i + 1] = aux;
            bubble_sort(v, n, 0); // returns to position 0
        }else{
            bubble_sort(v, n, i + 1); // forward
        }
    }
}

void main(){
    int *v, n;
    printf("Write the size of vector: ");
    scanf("%d", &n);
    
    v = (int *) malloc(n * sizeof(int)); // allocates a vector with n elements
    
    for(int i = 0;i < n; i++){
        v[i] = rand() % 100; // function rand() return a random int number
    }
    
    for(int i = 0;i < n; i++){
        printf("%d ", v[i]); // print the vector before the bubble sort
    }
    
    bubble_sort(v, n, 0);
    
    printf("\n");
    for(int i = 0;i < n; i++){
        printf("%d ", v[i]); // print the vector after the bubble sort
    }
}

