#include <stdio.h>
#include <stdbool.h>

bool isPrime(int x){
  int factor = 2;
  while(factor*factor <= x){
    if(x%factor==0){return false;}
    factor++;
  }
  return true;
}

int numOfPrimes,checked = 0;

void main(){
  while (numOfPrimes <= 10001){
    checked +=1;
    if(isPrime(checked)){numOfPrimes++;}
  }
  printf("%d", checked);
}
