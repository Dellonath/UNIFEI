#include <stdio.h>
#include <stdlib.h>

int count_spaces(char **M, int n){
	int spaces = 0;

	for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            if(M[i][j] == '0') spaces++;

    return spaces;
}

void print_matrix(char **M, int n){
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++)
            printf("%c",M[i][j]);
       	printf("\n");
	}
	printf("\n");
}

int check_move(char **M, int n, int x, int y){
	if(x >= 0 && x < n && y >= 0 && y < n && M[x][y] == '0')
		return 1;
	return 0;
}

int check_trail(int **N, int n, int x, int y){
	for(int i = 0; i < n; i++) if(N[i][0] == x && N[i][1] == y) return 0;
	return 1;
}

int **find_second_letter_position(char **M, int n, char L){

	int k = 0;

	int **letters_pos; 
	letters_pos = (int **) malloc(2 * sizeof(int *));
	for(int i = 0; i < n;i++) letters_pos[i] = (int *) malloc(2 * sizeof(int));

	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++)
            if(M[i][j] == L){
            	letters_pos[k][0] = i;
            	letters_pos[k][1] = j;
            	k++;
            }
	}

	return letters_pos;
}

int resolve(char **M, int n, int x, int y, char L, int q, int **N, int count){

	if(check_move(M, n, x, y)){
		M[x][y] = L;
		printf("x=%d y=%d q=%d\n", x, y, q);
		print_matrix(M, n);
	}

	if(count > 30) return 0;


	if(check_move(M, n, x - 1, y)) 
		resolve(M, n, x - 1, y, L, q + 1, N, count + 1);

	if(check_move(M, n, x, y + 1)) 
		resolve(M, n, x, y + 1, L, q + 1, N, count + 1);

	if(check_move(M, n, x + 1, y)) 
		resolve(M, n, x + 1, y, L, q + 1, N, count + 1);

	if(check_move(M, n, x, y - 1)) 
		resolve(M, n, x, y - 1, L, q + 1, N, count + 1);
	

}

void read_data(char **M, int n){
	
	for(int i = 0; i < n; i++) M[i] = (char *) malloc(n * sizeof(char));
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            scanf(" %c", &M[i][j]);
}

int main(){
	int n, aux;
	scanf("%d",&n);

    char **M;
    int **N;
	M = (char **) malloc(n * sizeof(char *));
	read_data(M, n);

	aux = count_spaces(M, n);
	N = (int **) malloc(n * sizeof(int *));
	for(int i = 0; i < aux; i++) N[i] = (int *) malloc(2 * sizeof(int));
    


    //find_second_letter_position(M, n, 'B');
    resolve(M, n, 0, 0, 'A', 0, N, 0);
    //print_matrix(M, n);

}
