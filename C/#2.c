#include <stdio.h>

int a=0, b=1, c=1, sum=0;

void main(){
  for(int i=0; c<4000000;i++){
    a = b;
    b = c;
    c = a+b;
    if(c%2 == 0){sum += c;}
  }
  printf("%d",sum);
}
