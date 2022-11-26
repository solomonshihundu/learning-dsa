using System;

namespace number_guess
{
    class Program
    {
        static void Main(string[] args)
        {
            Random random = new Random();
            while(true){
                int randno = random.Next(1,101);
                int count = 1;
                while(true)
                {
                    Console.Write("Enter a number between 1 and 100(0 to quit)");
                    int input = Convert.ToInt32(Console.Readline());
                    if(input == 0)
                        return;
                    else if (input < randno)
                    {
                        Console.WriteLine("Low, try again");
                        ++count;
                        continue;
                    }
                    else if (input > randno)
                    {
                        Console.WriteLine("High, try again");
                        ++count;
                        continue;
                    }
                    else
                    {
                        Console.WriteLine("You guessed it! The number was {0}!",randno);
                        Console.WriteLine("It took you {0} {1}.\n",count,count ==1 ? "try" : "tries");
                        break;

                    }

                }
            }
        }
    }
}