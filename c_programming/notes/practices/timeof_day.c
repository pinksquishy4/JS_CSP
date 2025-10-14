// JS 6th Time of Day
#include <stdio.h>
int main(void){
    int hour;

    printf("What is the hour in military time: ");
    scanf("%d", &hour);
    if (hour >= 0 && hour < 6) {
        printf("Good Night!\n");
    }
    else if (hour >= 6 && hour < 12) {
        printf("Good Morning!\n");
    }
    else if (hour >= 12 && hour < 18) {
        printf("Good Afternoon!\n");
    }
    else if (hour >= 18 && hour <= 23) {
        printf("Good Evening!\n");
    }
    else {
        printf("thats not even a real hour\n");
    }

      return 0;
}