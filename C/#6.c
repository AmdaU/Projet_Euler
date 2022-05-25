#include <stdio.h>

int sumsq,sqsum =0;

void main(){
  for(int i; i <=100; i++){
    sumsq += i*i;
    sqsum += i;
  }
  printf("%d\n", sqsum*sqsum - sumsq);
}
