#include <stdio.h>
#include <stdlib.h>
int a;

int main(int argc, char *argv[]){
  unsigned int arg = (unsigned int) atoi(argv[1]);
  srand(arg);
  printf("[");
  for(int i=0; i < 37; i++){
    a = rand() & 0xff;
    printf("%d,",a);
  }
  a = rand() & 0xff;
  printf("%d]\n", a);
}