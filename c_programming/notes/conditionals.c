// JS 6th Conidtionals notes
#include <stdio.h>
#include <string.h>

int main(void){
    int grade;
    printf("What is your grade:" );
    scanf("%d", &grade);

    if(grade > 90 ){
        printf("You have an A!\n");
    }else if(grade >=80){
        printf("You have a B!\n");
    }else{
        printf("You have are failing ohr naur");

    }
  






    return 0;
}



//What puts something inside of the “if” statement?
//a conditions

//How are conditions written in C?
//conditions are written within conditional statements like if, else if, and else. These conditions determine the flow of execution in a program.

//How do we write elif conditions in C?
//else if

//When do else conditions run?
//when all the statements prior are false.

//What are the 3 logical operators in C?
// && and
// || or
// ! inverts