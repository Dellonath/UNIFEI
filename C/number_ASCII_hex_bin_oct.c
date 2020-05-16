/*
Write a program that accepts a decimal number
signed as an ASCII string and print your
complementary representation of two in binary,
octal and hexadecimal.
*/
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

void binary(int a){
    int r, carry = 1;
    char b[8];
    for(int i = 7; i >= 0; i--){ 
        r = a >> i;
        if(r & 1) {
            b[i] = '0';
        }else{
            b[i] = '1';
        }
    }

    for(int i = 7; i >= 0; i--){
        if(b[i] == '1' && carry == 1){
            b[i] = '0';
            carry = 1;
        }else{
            if(b[i] == '0' && carry == 1){
                b[i] = '1';
                carry = 0;
            }
        }
    }
    printf("%s", b);
}

int main(){
    int size;
    printf("Write how many digits are in the number (with positive or negative signal: ");
    scanf("%d", &size);
    char *a = (char *) malloc(size * sizeof(char)); 
    printf("Digit the number: ");
    scanf("%s", a);
    
    for(int i = 0; i < size; i++){
        printf("\nDECIMAL: %c   ASCII: %d    HEXADECIAL: %x    OCTAL: %o    BINARY (Two's Compl.):  ", a[i], a[i], a[i], a[i]);
        binary(a[i]);
    }
}


/* 
Write how many digits are in the number (with positive or negative signal: 3                                                                             
Digit the number: +12                                                                                                                                    
                                                                                                                                                         
DECIMAL: +   ASCII: 43    HEXADECIMAL: 2b    OCTAL: 53    BINARY (Two's Compl.):  00101100                                                                
DECIMAL: 1   ASCII: 49    HEXADECIMAL: 31    OCTAL: 61    BINARY (Two's Compl.):  01110100                                                                
DECIMAL: 2   ASCII: 50    HEXADECIMAL: 32    OCTAL: 62    BINARY (Two's Compl.):  10110100
*/
