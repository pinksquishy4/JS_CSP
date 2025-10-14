// JS 6th Mad Libs
#include <stdio.h>
int main(void){
    char name[20];
    char place[20];
    char thing[20];

    printf("Enter a name: ");
    scanf("%s", name);

    printf("Enter a place: ");
    scanf("%s", place);

    printf("Enter a thing (like a noun): ");
    scanf("%s", thing);


    printf("\nSo %s went to the %s to get a %s but it was closed so they cryed and went home.\n", name, place, thing);
    printf("Then %s tried to eat the %s but it tasted like %s and they got sick oh no!.\n", name, thing, place);
    printf("Moral of the story: never trust a %s from a %s unless your name is %s.\n", thing, place, name);





    return 0;
}