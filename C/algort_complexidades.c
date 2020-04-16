// Complexidade O(1)
// atribui valor 10 a uma variável
#include <stdio.h>

int main(){
	int x;
	x = 10;
}


// Complexidade O(n)
// cria uma lista e atribui valor de i para cada posição i do vetor
#include <stdio.h>
#include <stdlib.h>

int main(){
	int *vetor, n, i;
	printf("Digite o tamanho do vetor:");
	scanf("%d", &n);

	vetor = (int *) malloc(n*sizeof(int));

	for(i = 0; i < n; i++){ // responsável pela complexidade O(n)
		vetor[i] = i;
	}
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////

// Complexidade O(n²)
// aloca memória para uma matriz bidimensional e atribui valor 0 a cada posição da matriz n x n
#include <stdio.h>
#include <stdlib.h>

int main(){
	int **matriz, n, i, j;

	printf("Digite o número das linhas e colunas: ");
	scanf("%d", &n);


	matriz = (int **) malloc(n * sizeof(int *));
    
    for(i = 0;i < n; i++){
        matriz[i] = (int *) malloc(n * sizeof(int));
    }
    
	for(i = 0; i < n; i++){
		for(j = 0; j < n; j++){ // responsável pela complexidade O(n²)
			matriz[i][j] = (i + 1) * 10 + (j + 1); 
		}
	}
	
	for(i = 0; i < n; i++){
		for(j = 0; j < n; j++){ // apenas para demonstração da matriz bidimensional
			 printf("%d ", matriz[i][j]);
		}
	}
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////

// Complexidade O(n³)
// aloca memória para uma matriz tridimensional e atribui valor 0 a cada posição da matriz n x n x n
#include <stdio.h>
#include <stdlib.h>

int main(){
	int ***matriz, n, i, j, k;

	printf("Digite o número das linhas, colunas e profundidade: ");
	scanf("%d", &n);


	matriz = (int ***) malloc(n * sizeof(int **));
    
    for(i = 0;i < n; i++){
    	matriz[i] = (int **) malloc(n * sizeof(int *));
    	for(j = 0; j < n; j++){
    		matriz[i][j] = (int *) malloc(n * sizeof(int));
    	}
        
    }
    
	for(i = 0; i < n; i++){
		for(j = 0; j < n; j++){ // responsável pela complexidade O(n³)
			for(k = 0; k < n; k++){
			    matriz[i][j][k] = (i + 1) * 100 + (j + 1) * 10 + (k + 1);
			}
		}
	}
	
	for(i = 0; i < n; i++){
		for(j = 0; j < n; j++){ 
			for(k = 0; k < n; k++){
			     printf("%d ", matriz[i][j][k]); // apenas para demonstração da matriz (pode ser ignorado todo esses for aninhados)
			}
		}
	}
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////

// Complexidade O(2^n)
// retorna o n-ésimo termo da Sequência de Fibonacci
#include <stdio.h>
#include <stdlib.h>

int fibonacci(n){
	if(n == 0){
		return 0;
	}else{
		if (n == 1){
			return 1;
		}else{
			if(n > 1){
				return fibonacci(n - 1) + fibonacci(n - 2);
			}
		}
	}
}

int main(){
	int n;

	printf("Digite o número de termos: ");
	scanf("%d", &n);
	for(int i = 0; i < n; i++){
	    printf("%d ", fibonacci(i));
	}
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////

// Complexidade O(log n)
// retorna a posição da chave no vetor utilizando busca binária
#include <stdio.h>
#include <stdlib.h>

int busca_binaria(int v[], int esq, int dir, int chave){ 
    if (dir >= esq){ 
        int mid = esq + (dir - esq) / 2; 
        if (v[mid] == chave){
            return mid; 
        }
        if (v[mid] > chave){
            return busca_binaria(v, esq, mid - 1, chave); 
        }
        return busca_binaria(v, mid + 1, dir, chave); 
    }
    return -1; 
} 
  
int main(){ 
    int *v, chave, resultado, n; 

    printf("Digite o tamanho do vetor: ");
    scanf("%d", &n);
    
    printf("Digite a chave que deseja encontrar: ");
    scanf("%d", &chave);
    
    v = (int *) malloc(n * sizeof(int));
    
    for(int i = 0; i < n; i++){
    	v[i] = i;
    }

    resultado = busca_binaria(v, 0, n - 1, chave); 

    if(resultado == -1){
    	printf("\nNúmero não encontrado.");
    }else{
    	printf("\nNúmero encontrado na posicão %d do vetor.", resultado);
    }
    return 0; 
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////

// Complexidade O(nlog n)
// dado um vetor, ordena os elementos do vetor do menor para maior com MergeSort
#include <stdio.h>
#include <stdlib.h>

void mergesort(int *v, int n);
void sort(int *v, int *c, int i, int f);
void merge(int *v, int *c, int i, int m, int f);

void mergesort(int *v, int n){
  	int *c = malloc(sizeof(int) * n);
  	sort(v, c, 0, n - 1);
  	free(c);
}

void sort(int *v, int *c, int i, int f){
  	if (i >= f){
  		return;
  	} 

  	int m = (i + f) / 2;

  	sort(v, c, i, m);
  	sort(v, c, m + 1, f);

  	if (v[m] <= v[m + 1]){
  		return;
  	} 

  	merge(v, c, i, m, f);
}

void merge(int *v, int *c, int i, int m, int f){
  	int z, iv = i, ic = m + 1;

  	for(z = i; z <= f; z++){
  		c[z] = v[z];
  	} 
 	z = i;
  	while(iv <= m && ic <= f) {

    	if (c[iv] < c[ic]){
    		v[z++] = c[iv++];
    	}else{
    		v[z++] = c[ic++];
    	} 
  	}

  	while(iv <= m){
  		v[z++] = c[iv++];
  	}

  	while(ic <= f){
  		v[z++] = c[ic++];
  	} 
}

int main(){
  int *v, i, n;

  printf("Digite o tamanho do vetor: ");
  scanf("%d", &n);

  v = (int *) malloc(n * sizeof(int));

  for(i = 0; i < n; i++){
  	v[i] = rand() % 49;
  }

  mergesort(v, n);

  for(i = 0; i < n; i++){
  	printf("%d ", v[i]);
  } 
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////

// Complexidade O(n!)
// pega uma string e exibe todas as permutações possíveis
#include <stdio.h> 
#include <string.h> 

void swap(char *x, char *y) 
{ 
    char temp; 
    temp = *x; 
    *x = *y; 
    *y = temp; 
} 

void permute(char *a, int l, int r) 
{ 
   int i; 
   if (l == r) 
     printf("%s\n", a); 
   else
   { 
       for (i = l; i <= r; i++) 
       { 
          swap((a+l), (a+i)); 
          permute(a, l+1, r); 
          swap((a+l), (a+i)); 
       } 
   } 
} 
  
int main() 
{ 
    char str[] = "ABCDE"; 
    int n = strlen(str); 
    permute(str, 0, n-1);
    return 0; 
}
