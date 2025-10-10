// JS 6th Old enough

#include <stdio.h>
#include <string.h>

int main(void){
    int age;
    printf("How old are you:\n");
    scanf("%d", &age);

    if(age >=18){
        printf("You are old enough to vote");
    }else if(age == 16){
        printf("You are old enough to drive");
    }else if(age ==15){
        printf("You are old enough to get your permit.");
    }else if(age >= 5){
        printf("You can go to school");
    }else{
        printf("You arent old enough for anything here!!\n");
    }
    





    return 0;
}