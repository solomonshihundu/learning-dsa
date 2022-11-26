#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#define MAXINPUT 100

int main() 
{   
    char input[MAXINPUT] = "";
    int length,i; 
    int number;

    while(1)
    {  
    
    printf("Please enter a Number: ");  

    scanf ("%s", input);

    //Check if input is break call
    if(!strcmp(input,"break"))
    {
        printf("Exiting Program");
        break;
    }
    else
        //Check if ionput is a number
        length = strlen (input);
        for (i=0;i<length; i++)
            if (!isdigit(input[i]))
            {
                printf ("Entered input is not a number\n");
            }
            //If input is a number convert it to data type double
            const char* str = input;
            int number;
            sscanf(str, "%d", &number);

            // true if num is perfectly divisible by 2
            if(number % 2 == 0)
                printf("%d is an even number\n", number);
            else
                printf("%d is an odd number\n", number);

    
    }
    return 0;

}