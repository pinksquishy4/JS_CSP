//JS 6th Strings Notes
#include <stdio.h>
#include <string.h>
int main(void){
    char name [] = "Juliette";
    printf("Please tell me your last name: \n");

    char last_name[25];
    char full_name[100];

    scanf("%s", last_name);
    printf("[%s]", name);


    strcat(name, " ");
    printf("[%s]", name);


    strcat(name, last_name);
    printf("[%s]", name);

    strcat(full_name, last_name);
    strcat(full_name, " ");
    

    printf("%zu \n", strlen(full_name));
    printf("%zu\n", sizeof(full_name));
    
    
    
    
    return 0;


}

//What is the difference between a string and a character?
 //char tells us we are dealing with letters, so we need to set it to char. 
 /*Once you set you chraacter limit, you cannot increase it when you are writing it.
 Once youve moved on you cannot add more space. 
 - strings are very specfically lst of characters. every single string you cerate is just a list that looks like this.
 ["x", "a", "v", "i", "e", "r"]*/

//What types of quotation marks do we need for a string?
// we use double quotes because single qoute are used when we only have one letter.

//What library do we need to include to access the string functions in C?
// you do #include <string.h>

//List functions the library allows us to use.
//strcat
//strlength it gives us how large it could be
//size of how much space i have

//How do we concatenate strings in C?
//we add the quotation marks with an empty space is the strcat function.

//How do we get individual characters from a string in C?
//name[2]='j'
//make sure to use single quotes