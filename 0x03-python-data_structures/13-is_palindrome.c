#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list node */
struct listint_s {
    int n;
    struct listint_s *next;
};

typedef struct listint_s listint_t;

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 * Return: 1 if it is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *temp;

    if (*head == NULL || (*head)->next == NULL)
    {
        return (1);
    }
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        temp = slow;
        slow = slow->next;
        temp->next = prev;
        prev = temp;
    }
    if (fast != NULL)
    {
        slow = slow->next;
    }
    while (slow != NULL)
    {
        if (slow->n != prev->n)
	{
            return (0);
        }
        slow = slow->next;
        prev = prev->next;
    }

    return (1);
}
