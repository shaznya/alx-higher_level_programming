#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list. */
struct listint {
    int value;
    struct listint *next;
};

typedef struct listint listint_t;

/* Function to check if a singly linked list has a cycle. */
int check_cycle(listint_t *list);

/* Example usage */
int main()
{
	int result;
    listint_t *head = malloc(sizeof(listint_t));
    head->value = 1;
    head->next = malloc(sizeof(listint_t));
    head->next->value = 2;
    head->next->next = malloc(sizeof(listint_t));
    head->next->next->value = 3;
    head->next->next->next = head;

    result = check_cycle(head);

    if (result) {
        printf("The linked list has a cycle.\n");
    } else {
        printf("The linked list does not have a cycle.\n");
    }

    /* Remember to free allocated memory */
    free(head->next->next);
    free(head->next);
    free(head);

    return 0;
}
