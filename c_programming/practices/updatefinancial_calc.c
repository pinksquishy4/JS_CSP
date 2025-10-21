//JS 6th Update Financial Calculator 

#include <stdio.h>


float getInput(char label[]) {
    float amount;
    printf("What is your monthly %s: ", label);
    scanf("%f", &amount);
    return amount;
}


int calcPercent(float income, float expense) {
    return (expense / income) * 100;
}

int main() {
    float income, rent, utilities, groceries, transport, savings, spending;
    int rentPercent, utilPercent, groceryPercent, transPercent, savePercent;

    income = getInput("income");
    rent = getInput("rent/mortgage");
    utilities = getInput("utilities");
    groceries = getInput("groceries");
    transport = getInput("transportation");

    rentPercent = calcPercent(income, rent);
    utilPercent = calcPercent(income, utilities);
    groceryPercent = calcPercent(income, groceries);
    transPercent = calcPercent(income, transport);

    savings = income * 0.10;
    savePercent = calcPercent(income, savings);
    spending = income - (rent + utilities + groceries + transport + savings);

    printf("\nYour rent is $%.2f and that is %d%% of your income.\n", rent, rentPercent);
    printf("Your utilities are $%.2f and that is %d%% of your income.\n", utilities, utilPercent);
    printf("Your groceries are $%.2f and that is %d%% of your income.\n", groceries, groceryPercent);
    printf("Your transportation is $%.2f and that is %d%% of your income.\n", transport, transPercent);
    printf("You should save $%.2f a month, that is %d%% of your income.\n", savings, savePercent);
    printf("You have $%.2f of spending money each month!\n", spending);

    return 0;
}