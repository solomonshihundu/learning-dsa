//Program
//Take a number from the user using switch case
//Program prints "First" if num is range of 1 -100
// Prints "Second " if in range of 101 - 200

#include <stdio.h>
int main() {   
    int number;
   
    printf("Please enter a Number: ");  
    
    // reads and stores input
    scanf("%d", &number);


    //
    switch ((number > 0 && number <= 200 ) ? ((number <= 100) ? 0 : 1) : -1) {
    case 0:
        printf("First");
        break;
    case 1:
        printf("Second");
        break;
    default:
        printf("Input Out of Range");
        break;
    }
    
    return 0;
}

//https://www.codeproject.com/Questions/1154415/How-do-I-perform-inequality-comparisons-in-C-using