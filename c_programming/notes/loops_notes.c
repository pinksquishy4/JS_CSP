// JS 6th Loops Notes
#include <stdio.h>

int main(void){
    int nums[] = {4,5, 5, 2, 4, 5, 6, 7, 8, 9, 3};
    char candy[5][20] = {"Skittles", "Butterfinger", "Reese's", "Twix","Kitkat"};

    for(int x = 0; x < 11; x++){
        printf("%d\n", nums[x]);

    }
    for (int i=0; i < 5; i++){
        printf("%s is my favorite Candy!\n", candy[i]);
    }
    for (int num = 1; num < 11; num++){
        printf("%d\n", num);
    }
        int goose = 6;
    int count = 0;
    while(count != goose){
        printf("Duck\n");
        count++;
    }
    printf("Goose!");

    return 0;
}


//What is a loop? 
//num = 0
// while num<10:
    //print(num)
    //num+=1

//What are the two types of loops?
//for and while

//What is iteration
//doing the same thing over and over again

//What are arrays? 
//a collection of data that we clump together

//How do you make lists in C? 
//int ---data type) nums[]---how many times ={ 4, 5, 6 ,7 ,8 ,9};

//How do you make for loops in C? 
//for (int i=0; i < 5; i++)--put the plus plus it means increase by 1



//How do you make while loops in C?
//almost indentical to a while loop in python

/*        int goose = 6;
    int count = 0;
    while(count != goose){
        printf("Duck\n");
        count++;
    }
    printf("Goose!");
*/


