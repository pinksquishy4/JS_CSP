// JS 6th random numbers
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(void){
    char letters[] = {'a', 'b', 'c', 'd'};
    for(int i=0; i < 10; i++){
    srand(time(NULL));
    int num = rand() %5; //%20 +1;
    printf("%d\n", num);
    }





    return 0;
}
//modulo by your highest number and add by your lowest it doesnt matter which order