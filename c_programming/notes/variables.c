// VL 6th Variables Notes
#include <stdio.h>

int main(void){
    int num = 4;
    printf("%d", num);
    float pi = 3.14;
    char grade = 'A'; //will only hold one letter
    char name[]= "Juliette";
    //bool passing = true;

    printf("What is your letter grade: ");
    scanf("%c", &grade);

    printf("%d\n", num);
    printf("%s has a %c grade in the class!\n", name, grade);

    return 0;
}
//What is the main difference between declaring variables in Python and C?
//Python: Variables are dynamically typed, so you don't need to specify a data type when declaring a variable.

//C: Variables are statically typed, so you must specify the data type when declaring a variable.


//In C, what is the purpose of specifying a data type when declaring a variable?
//It tells the person the kind of data the variable will hold (e.g., integer, float)
//and it tells how much memory to allocate for that variable


//List three common data types used in C and their corresponding format specifiers for printf().
//int - %d
//float - %f
//char - %c


//How do you declare and initialize an integer variable named "age" with the value 25 in C?
//int age = 25;


//What is the difference between printf() and scanf() functions in C?
//printf() is used to display output on the screen.
//scanf() is used to read input from the user.


//How do you add comments in C?
// single line comments use //
//double line comments use /* */




//What is the purpose of the #include <stdio.h> line at the beginning of a C program?
// it includes the standard output/input library, which provides functions like printf() and scanf().



//In C, what is the significance of the main() function?
//It is the entry point of the program where the excution starts.


//What is the difference between %d and %f format specifiers in printf()?
//%d is used to print integers (whoel numbers).



//How do you print a newline character in C?
//Use /n in the format string of printf().



//What is the purpose of the & symbol when using scanf() to get user input?
//The & symbol is used to get the adress of the variable where the input will be stored.



//How do you declare a constant in C? Provide an example.
//Use the const keyword before the data type.
//const float PI = 3.14;
