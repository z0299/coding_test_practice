#include <stdio.h>

int num;
void go();

int main(){
    printf("%d", num);
    go();
    printf("%d", num);
    return 0;
}

void go(void){
    num = 16448000;
}