// JS 6th Financial calculator
#include <stdio.h>
#include <math.h>
int main(void){
 float income, rent, utilities, groceries, transportation;


    printf("What is your monthly income: ");
    scanf("%f", &income);

    printf("What is your monthly rent/mortgage: ");
    scanf("%f", &rent);

    printf("What is your monthly utilities: ");
    scanf("%f", &utilities);

    printf("What is your monthly groceries: ");
    scanf("%f", &groceries);

    printf("What is your monthly transportation: ");
    scanf("%f", &transportation);

    
    float rentPercent = (rent / income) * 100;
    float utilitiesPercent = (utilities / income) * 100;
    float groceriesPercent = (groceries / income) * 100;
    float transportationPercent = (transportation / income) * 100;

    float savings = income * 0.10;
    float spendingMoney = income - (rent + utilities + groceries + transportation + savings);


    printf("\nYour rent is $%.2f and that is %.0f%% of your income.\n", rent, rentPercent);
    printf("Your utilities are $%.2f and that is %.0f%% of your income.\n", utilities, utilitiesPercent);
    printf("Your groceries are $%.2f and that is %.0f%% of your income.\n", groceries, groceriesPercent);
    printf("Your transportation is $%.2f and that is %.0f%% of your income.\n", transportation, transportationPercent);
    printf("You should save $%.2f a month, that is 10%% of your income.\n", savings);
    printf("You have $%.2f of spending money each month!\n", spendingMoney);









    return 0;
}