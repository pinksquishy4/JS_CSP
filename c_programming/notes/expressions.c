// JS 6th Expressions notes
#include <stdio.h>
#include <math.h>

int main(void){
    int year = 2025; //Whole numbers
    float pi = 3.14; //Decimals
    double long_pi = 3.1459265359; // decimals that are 2x as long

    printf("%f\n", 8/3);
    printf("%f\n", 8/3);
    print("2 ^ 4 = %f\n", pow(2, 4));
    return 0;


}





//What is the difference between an integer and a float in C?

//an interger takes whole numbers, and a float takes decimals. Doubles have to be decimals.

//How does C handle integer division compared to float division?
//all division is integer division, unless one of your numbers is a float...it will always return an integer. Even if it is division.

//List the arithmetic operators available in C and their functions.
/* +-- division
- -- subtraction
/ -- divison 
*-- multiplication
%-- modulo (Remainder)
*/

//What is the modulus operator, and how is it used?
//The modulus operator in C is %.
//It gives the remainder after dividing one integer by another.
//result = a % b;
//It only works with integers, not floats.

//Commonly used to check if a number is even or odd:

//How do you round a float to the nearest integer in C?

//Use the round() function from the math.h library.
//#include <stdio.h>
//#include <math.h>

//int main() {
  //  float num = 3.6;
   // float rounded = round(num);
   // printf("%.0f\n", rounded);  // Output: 4
   // return 0;
//What is type casting in C? Provide an example of explicit type casting.
//Where we detirmine what the data type is and you change that datta type by doing explixet casting
//printf("8/3 = %f\n", (float)8/3);
//cast is specifically stating the data type 

//How do compound assignment operators work in C? List three examples.
//Compound assignment operators are shortcuts that combine an arithmetic operation with assignment.
//Instead of writing x = x + 5;, you can write x += 5;.
//x += 5;  // Same as: x = x + 5;
//y -= 3;  // Same as: y = y - 3;
//z *= 2;  // Same as: z = z * 2;

//what is the purpose of the math.h library? Name three functions it provides.
//the math.h library provides math functions in C that go beyond basic arithmetic.
//sqrt(x);   // Square root of x
//pow(x, y); // x raised to the power y (x^y)
//in(x);    // Sine of x (in radians)


//How do you print a float with a specific number of decimal places using printf()?
//Use %.nf in printf() where n is the number of decimal places you want.
//float num = 3.14159;
//printf("%.2f", num);  // Output: 3.14


//%.2f means print the float with 2 decimal places.


//What happens when you mix integer and float operations in C?
//the outcome will always be a float,, just like in python
