#include <stdio.h>
#include <stdbool.h>
#include <string.h>

void main(){
  int sa = 999;
  char s[10], scopy[10];
  bool found = false;
  while(!found){
    for(int diff = 1; diff >= 0; diff--){
      int b = sa + diff;
      for(int a = sa; a <=999; a++){
        b--;
        sprintf(s, "%d", a*b);
        strcpy(scopy,s);
        strrev(scopy);
        if(strcmp(scopy,s) == 0){
          found = true;
          printf("%d",a*b);
          break;
        }
      }
    }
    sa--;
  }
}
