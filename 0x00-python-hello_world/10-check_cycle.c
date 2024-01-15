#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list. */
typedef struct listint_t {
    int data;
    struct listint_t *next;
} listint_t;

/* Function to check if a singly linked list has a cycle. */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;
	if (list == NULL || list->next == NULL)
	{
		return 0;
	}
	tortoise = list;
	hare = list->next;
	while (hare != NULL && hare->next != NULL)
	{
		if (tortoise == hare)
		{
			return 1;
		}
		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	return 0;
}

