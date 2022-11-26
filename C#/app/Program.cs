
using System;
 
namespace Main
{
    class Program
    {
        private class Node
        {
            public int data;
            public Node next;
 
            public Node(int data) => this.data = data;
        }
        
        // create new nodes with passed argument data
        static Node setNode(int data) => new Node(data);
 
        // function to insert a Node at required position
        static Node insertInMiddle(Node head, int pos, int data)
        {
            var headnode = head;
            if (pos < 1)
                Console.WriteLine("Invalid position");
            
            // if list has only and position = 1, insert the newnode before the headnode
            if (pos == 1)
            {
                var newNode = new Node(data);
                newNode.next = head;
                headnode = newNode;
            }
            // if there are more than 1 nodes
            else
            {
                while (pos-- != 0)
                {
                    if (pos == 1)
                    {
                        Node newNode = setNode(data);
                        newNode.next = head.next;
                        head.next = newNode;
                        break;
                    }
                    head = head.next;
                }
                if (pos != 1)
                    Console.WriteLine("Position out of range");
            }
            return headnode;
        }
 
        // display the list nodes
        static void display(Node node)
        {
            while (node != null)
            {
                Console.WriteLine("Data = "+node.data);
                node = node.next;
            }
            Console.WriteLine();
        }
 
        // Driver code
        static void Main(string[] args)
        {
            // directly inserting the data to make the original list 
            // ================================================
 
            var head = setNode(1);
            head.next = setNode(2);
            head.next.next = setNode(3);
            head.next.next.next = setNode(4);
            // ================================================


            // display the list before inserting in middle
            Console.WriteLine("Data entered in the list are: ");
            display(head);
            
            // *** MAIN PROGRAM REQUIRED TO INSERT DATA IN THE MIDDLE OF THE LIST ***
            int data, pos;
            // get dta and position from user
            Console.Write("Input data to insert in the middle of the list: ");
            data = Convert.ToInt32(Console.ReadLine());
            Console.Write(" Input the position to insert new node: ");
            pos = Convert.ToInt32(Console.ReadLine());
            
            Console.WriteLine("\nInsertion completed successfully.");
            
            // call the insertInMiddle method and insert the user data
            head = insertInMiddle(head, pos, data);
            // display the list after inserting
            Console.WriteLine("The new list are:");
            display(head);
        }
    }
}