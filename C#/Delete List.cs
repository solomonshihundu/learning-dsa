using System;

namespace DeleteList
{
    public class DeleteList
    {
        
        void DeleteList(List* list) 
        {
            // Check if list is empty
            if (list == NULL)
            {
            return;
            }
            

            // Iterate through list, deallocating each node
            Node* current = list->head;

            while (current != NULL)
            { 
                Node* next = current->next;
                free(current);
                current = next;
            }

            // Set head pointer to NULL
            list->head = NULL;
            return;
        }
    }
}