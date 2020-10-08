#include <stdlib.h>
#include <stdio.h>

void swap(int A[], int i, int j){ // trocas os valores das posições i e j de A
	int aux = A[i];
	A[i] = A[j];
	A[j] = aux;
}

int partition(int A[], int l, int r){ // algoritmo de partição do quicksort
	int i = l + 1, pivot = A[l]; // seleciona como pivot o numero na posição l do vetor
	for(int j = l + 1; j <= r; j++){
		if(A[j] <= pivot){ // joga todos os valores menores que o pivot para a esquerda
			swap(A, j, i);
			i++; // proximo termo
		}
	}
	swap(A, l, i - 1); 
	return i - 1; // retorna a posição o i-ésimo menor termpo
}

int selectionR(int A[], int l, int r, int i){ 
	if(l == r) return A[l]; 
	int k = rand() % (r - l + 1) + l; // seleciona um pivot aleatório em [i, r]
	/*
	suponha um vetor de 100 posições e iremos buscar na segunda parte deste vetor, então teríamos 50 posições 
	representado por (r - l + 1), a unidade a mais serve para englobar a última posição do vetor. 
	Soma-se então l para tomarmos os valores entre 50 e 100 (segunda parte do vetor)
	*/
	swap(A, l, k); // troca o valor da posição selecionada como vetor na primeira posição

	int p = partition(A, l, r); // inicia a partição como ocorre no quicksort
	int j = p - l + 1; // j para ajustar a posição i procurada

	if(j == i) return A[p];
	if(j > i) return selectionR(A, l, p - 1, i); // seleciona a primeira parte do vetor buscando pelo i-ésimo menor
	if(j < i) return selectionR(A, p + 1, r, i - j); // seleciona a segunda parte buscando pelo (i - j)-ésimo menor
	return 1;
}

int main(int argc, char* argv[]){
  int n;
  int *A;
  int i;
  
  scanf("%d", &n); getchar();
  i = n/2;
  if(n%2==1)i = i+1;

  A = (int*) malloc(n*sizeof(int));
  srand(48+n); 
  
  for(int j = 0; j < n; j++) A[j] = rand();

  printf("%d\n", selectionR(A, 0, n - 1, i));
  
 
  return 0;
}
