#include <stdio.h>

void sayHello(char name[]) {
    printf("Hello %s!\n", name);
}

int main() {

    sayHello("Jackie");
    sayHello("Isabella");
    sayHello("Alexxis");
    sayHello("Wesley");
    sayHello("Juliette");

    return 0;
}