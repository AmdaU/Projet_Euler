#include <stdio.h>

short candidate = 2;
long long number = 600851475143;

void main(){
  while (candidate*candidate < number){
    if (number % candidate == 0){
      number /= candidate;
      candidate = 1;}
    candidate += 1;}
  printf("%d",number);}
