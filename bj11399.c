#include <stdio.h>

int main(void){
    int n;
    scanf("%d", &n);
    int times[n];

    for(int i = 0; i < n; i++){
        scanf("%d", &times[i]);
    }
    for(int i = 0; i < n; i++){
        printf("%d", times[i]);
    }

    return 0;
}