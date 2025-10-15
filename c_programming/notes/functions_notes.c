// JS 6th Functions notes
#include <stdio.h>

void birthday(char* name, int age){
printf("Happy birthday to you\n");
printf("Happy birthday to you\n");
printf("Happy birthday to you\n");
printf("Happy Birthday dear %s\n", name);
printf("Happy birthday to you!\n");
printf("Happy birthfay %s is now %d\n", name, age);   





//int add(int num_one, int num_two){
    //return num_one + nume_two;

//}

}
//char* get_name(void){
    //char *name[50];
    //printf("What is your name?");
    //scanf("%s", name);
    //return name;
    
//} 
int main(void){
birthday("Mykel", 15);
birthday("Lucas", 40);
birthday("Victoria", 19);
birthday("Juliette", 67);
//char* user = get_name();
//birthday(user, 5);
//int addition = add(5,4);
//printf("%d\n", addition);
//printf("%d\n", add(50,37));

return 0;
}



//What a function is
///storage cotainers for actions that we can use over and over again
//you do not write functions inside of other functions.

//Why we use functions
// because they make things easier

//How to write a function in C
//you set a paremeter specifically inside the function

//What are arguments and parameters?
//parameters are the placeholders in the function's recipe, and arguments are the actual ingredients you use when you cook it. 

//How do arguments and parameters work together?
//A parameter is a placeholder for that information, and an argument is the actual piece of information you give.

//How to use parameters and arguments in c
//// Function declaration with parameters
//int add(int num1, int num2); 

// Function definition with parameters
//int add(int num1, int num2) {
    //return num1 + num2;
//}
//What are return statements?
//When a C program runs a function, it's like asking a mini-computer to do a job. The return statement is how that mini-computer gives the result back to the main program. 

//How do return statements change how you define a function in C?
//when you define a function in C, you specify the type of value it will return (like int for intergers), and you use the return statement to send that value back to where the function was called.


//What do return statements do with the information?
//Return statements send the result of a function back to the part of the program that called it.