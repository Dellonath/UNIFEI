#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef signed char singledigit;

void sum(int a, singledigit *A, int b, singledigit *B, int c, singledigit *C){
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
}

void subtract(int a, singledigit *A, int b, singledigit *B, int c, singledigit *C){
  singledigit carry = 0;

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

void shift(int sh, int n, signed char *A){   
    for(int i = 0; i < n-sh; i++) A[i] = A[i+sh];
    for(int i = n - sh; i < n; i++) A[i] = 0; 
}

void shift_r(int sh, int n, singledigit *A, int m, singledigit *B){
  int aux = n - sh; 
  for(int i = n - aux - 1, k = m - 1 ; i >= 0; i--, k--) B[k] = A[i];
}

void rest(int sh, int n, int m, singledigit *A, singledigit *B){
  for(int i = n - 1, k = m - 1; k >= 0; i--, k--) B[k] = A[i];
}

void copy(int n, singledigit *A, int m, singledigit *B){
    for(int i = n - 1, k = m - 1; i >= 0; i--, k--) B[k] = A[i];
}

void traditional_mult(int n, singledigit *A, singledigit *B, int m, singledigit *C){
  singledigit * T = calloc(m, sizeof(singledigit));
  for(int i = 1; i <= n; i++){

    single_multi(n, A, B[n-i], m, T);
    shift(i - 1, m, T);
    sum(m, T, m, C, m, C);
    for(int j = 0; j < m; j++) T[j] = 0;
  }
  free(T);
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

void input(int n, singledigit *A){
  char aux;
  for(int i = 0; i < n; i++){
    scanf("%c", &aux);
    A[i] = (int) aux - '0';
  };
  getchar();
}

void karatsuba(int n, singledigit *X, singledigit *Y, int max, singledigit *Z){
  if(n <= 4){
    return traditional_mult(n, X, Y, 2*n, Z);
  } 

  int m = ceil((float) n/2);

  singledigit *P = calloc(m, sizeof(singledigit));
  singledigit *Q = calloc(m, sizeof(singledigit));
  singledigit *R = calloc(m, sizeof(singledigit));
  singledigit *S = calloc(m, sizeof(singledigit));
  singledigit *P_Q = calloc(m+1, sizeof(singledigit)); 
  singledigit *R_S = calloc(m+1, sizeof(singledigit)); 
  singledigit *PR = calloc(2*m, sizeof(singledigit));
  singledigit *PRS = calloc(max, sizeof(singledigit));
  singledigit *QS = calloc(2*m, sizeof(singledigit));
  singledigit *K = calloc(2*(m+1), sizeof(singledigit));
  singledigit *KS = calloc(2*(m+1)+m, sizeof(singledigit));
  singledigit *Kaux = calloc(2*(m+1), sizeof(singledigit));
  singledigit *Zaux = calloc(max, sizeof(singledigit));
  
  if(n%2 == 0){
    shift_r(m, n, X, m, P);     
    shift_r(m, n, Y, m, R);
  }else{
    shift_r(m-1, n, X, m, P);
    shift_r(m-1, n, Y, m, R);
  }

  rest(m, n, m, X, Q);
  rest(m, n, m, Y, S); 

  sum(m, P, m, Q, m+1, P_Q);
  sum(m, R, m, S, m+1, R_S);

  karatsuba(m, P, R, 2*m, PR);
  karatsuba(m, Q, S, 2*m, QS);
  karatsuba(m+1, P_Q, R_S, 2*(m+1), K);

  subtract(2*(m+1), K, 2*m, PR, 2*(m+1), Kaux);
  subtract(2*(m+1), Kaux, 2*m, QS, 2*(m+1), K);

  copy(2*m, PR, max, PRS);
  shift(2*m, max, PRS);

  copy(2*(m+1), K, 2*(m+1)+m, KS);
  shift(m, 2*(m+1)+m, KS);

  sum(max, PRS, 2*(m+1)+m, KS, max, Zaux);
  sum(max, Zaux, 2*m, QS, max, Z);
  free(P);free(Q);free(R);free(S);free(P_Q);
  free(R_S);free(PR);free(PRS);free(QS);free(K);
  free(KS);free(Kaux);free(Zaux);

}

int main(void) {
  int n;
  scanf("%d",&n);

  getchar();

  singledigit *X = calloc(n, sizeof(singledigit));
  singledigit *Y = calloc(n, sizeof(singledigit));
  singledigit *Z = calloc(2*n, sizeof(singledigit));

  input(n, X);
  input(n, Y);
  
  karatsuba(n, X, Y, 2*n, Z);
  print(2*n, Z);

  free(X);free(Y);free(Z);
  return EXIT_SUCCESS;
}
