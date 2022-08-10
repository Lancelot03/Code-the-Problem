# the middle element of a singly linked list without iterating the list more than once


Node* getMiddle(Node *head)
{
     struct Node *slow = head;
     struct Node *fast = head;
 
     if (head)
     {
         while (fast != NULL && fast->next != NULL)
         {
             fast = fast->next->next;
             slow = slow->next;
         }
     }
     return slow;
}
