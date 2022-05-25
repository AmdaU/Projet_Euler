#include <stdio.h>

long long int result = 1;

void main(){
  for(int number = 2; number <=20; number++){
    int factor = 2;
    int temp = number;
    int tempres = result;
    while(factor <= temp){
      if(tempres%factor == 0 && temp%factor ==0){
        temp /= factor;
        tempres /= factor;
        factor =1;
      }
      factor ++;
    }
    result = result*temp;
  }
  printf("%d", result);
}
