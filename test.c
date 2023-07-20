#include <stdio.h>

int main(){
    int i, flag = 0, num = 20;
    for(i = 2; i <= num; i++){
        flag = 0;
        for(int j = 2; j <= i/2; j++){
            printf("i, j = %d %d\n", i, j);
            if(i % j == 0){
                flag = 1;
                break;
            }
        }
        if(flag == 0) printf("%d ", i);
    }
    return 0;
}