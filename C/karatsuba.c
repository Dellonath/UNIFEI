#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef signed char singledigit;

singledigit *sum(int a, singledigit *A, int b, singledigit *B, int c){
  singledigit *C = calloc(c, sizeof(singledigit));
  singledigit carry = 0;
  for(int i = 1; i <= c; i++){
    singledigit fA = 0;
    singledigit fB = 0;
    if(a >= i) fA = A[a-i];
    if(b >= i) fB = B[b-i];
    int r = fA + fB + carry;
    C[c-i] = r % 10;
    carry = (r - C[c-i])/10;
  }
  return C;
}

singledigit *subtract(int a, singledigit *A, int b, singledigit *B, int c){
  singledigit carry = 0;
  singledigit *C = calloc(c, sizeof(singledigit));
  
  for(int i = 1; i <= c; i++){
    singledigit fA = 0;
    singledigit fB = 0;
    if(a >= i) fA = A[a-i];
    if(b >= i) fB = B[b-i];
    fB = fB + carry;
    if(fB <= fA){
      C[c-i] = fA - fB;
      carry = 0;
    }else{
      C[c-i] = 10 + fA - fB;
      carry = 1;
    }
  }
  
  return C;
}

singledigit *rest(int sh, int n, singledigit *A){
  singledigit *B = calloc(n, sizeof(singledigit));
  for(int i = n-1; i >= n - sh; i--) B[i] = A[i];
  return B;
}

void single_multi(int n, singledigit *A, singledigit B, int m, singledigit *C){
  int carry = 0;
  for(int i = 1; i <= n; i++){
    int r = (A[n-i] * B) + carry;
    C[m-i] = r % 10;
    carry = (r - C[m-i])/10;
  }
  C[m-n-1] = carry;
}

singledigit *shift(int sh, int n, singledigit *A){
  for(int i = 0; i < n-sh; i++) A[i] = A[i+sh];
  for(int i = n - sh; i < n; i++) A[i] = 0;
  return A;
}

singledigit *shift_r(int sh, int n, singledigit *A){
  singledigit *B = calloc(n, sizeof(singledigit));
  for(int i = 0; i < n; i++) B[i] = A[i];
  for(int i = 0; i < sh; i++){
    int aux = B[n - 1];
    for(int i = n-1; i >= 0; i--) B[i]=B[i-1];
    B[0] = aux;
  }
  for(int i = 0; i < sh; i++) B[i] = 0;
  return B;
}


singledigit *traditional_mult(int n, singledigit *A, singledigit *B, int m){
  singledigit *C = calloc(m, sizeof(singledigit));
  singledigit *T = calloc(m, sizeof(singledigit));
  for(int i = 1; i <= n; i++){
    single_multi(n, A, B[n-i], m, T);
    shift(i-1, m, T);
    C = sum(m, T, m, C, m);
    for(int j = 0; j < m; j++) T[j] = 0;
  }
  free(T);
  return C;
}

void print(int n, singledigit *A){
  int i = 0;
  while(A[i] == 0) i++; 
  do{
    printf ("%d", A[i]);
    i++;
  }while(i < n);
  printf("\n");
}

int len(singledigit *A){
  int i = 0;
  while(A[i] != '\0') i++;
  return i;
}

void input(int n, singledigit *A){
  char aux;
  for(int i = 0; i < n; i++){
    scanf("%c", &aux);
    A[i] = atoi(&aux);
  };
  getchar();
}

singledigit *karatsuba(int n, singledigit *X, singledigit *Y, int k){

  if (n <= 5) return traditional_mult(n, X, Y, 2*n);

  singledigit *P = calloc(n, sizeof(singledigit));
  singledigit *Q = calloc(n, sizeof(singledigit));
  singledigit *R = calloc(n, sizeof(singledigit));
  singledigit *S = calloc(n, sizeof(singledigit));
  singledigit *P_Q = calloc(n, sizeof(singledigit));
  singledigit *R_S = calloc(n, sizeof(singledigit));
  singledigit *PR = calloc(2*n, sizeof(singledigit));
  singledigit *QS = calloc(2*n, sizeof(singledigit));
  singledigit *K = calloc(2*n, sizeof(singledigit));
  singledigit *UV = calloc(2*n, sizeof(singledigit));

  int m = ceil((float) n/2);
  P = shift_r(m, n, X);
  Q = rest(m, n, X);
  R = shift_r(m, n, Y);
  S = rest(m, n, Y); 

  P_Q = sum(n, P, n, Q, n);
  R_S = sum(n, R, n, S, n);

  PR = traditional_mult(n, P, R, 2*n);
  QS = traditional_mult(n, Q, S, 2*n); 
  K = traditional_mult(n, P_Q, R_S, 2*n); 
  
  K = subtract(2*n, K, 2*n, PR, 2*n);
  K = subtract(2*n, K, 2*n, QS, 2*n);

  PR = shift(2*m, 2*n, PR);
  K = shift(m, 2*n, K);
  
  //UV = sum(2*n, sum(2*n, shift(2*m, 2*n, PR), 2*n, shift(m, 2*n, subtract(2*n, subtract(2*n, K, 2*n, shift(2*m, 2*n, PR), 2*n), 2*n, QS, 2*n)), 2*n), 2*n, QS, 2*n);
  UV = sum(2*n, PR, 2*n, K, 2*n);
  UV = sum(2*n, UV, 2*n, QS, 2*n);
  return UV;
}



int main(void){
  int n;
  scanf("%d",&n);

  getchar();

  singledigit *X = calloc(n, sizeof(singledigit));
  singledigit *Y = calloc(n, sizeof(singledigit));
  singledigit *Z = calloc(2*n, sizeof(singledigit));
  
  input(n, X);
  input(n, Y);
  
  //Z = traditional_mult(n, X, Y, 2*n); 
  //Z = subtract(n, X, n, Y, n);
  //Z = sum(n, X, n, Y, n); 
  //Z = rest(3, n, X);
  //Z = shift_r(2, n, X);
  //Z = shift(2, n, X);
  Z = karatsuba(n, X, Y, 2*n);
  
  print(2*n, Z);



  printf("\n");

  free(X);free(Y);free(Z);
  return EXIT_SUCCESS;
}

