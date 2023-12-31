#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t

/**
 * check_cycle - Check if a singly linked list has a cycle
 * @list: Pointer to the head of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;
	
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
int custom_main(void)
{
	listint_t *head, *node1, *node2, *node3;
	
	head = malloc(sizeof(listint_t));
	node1 = malloc(sizeof(listint_t));
	node2 = malloc(sizeof(listint_t));
	node3 = malloc(sizeof(listint_t));
	
	head->n = 1;
	head->next = node1;
	node1->n = 2;
	node1->next = node2;
	node2->n = 3;
	node2->next = node3;
	node3->n = 4;
	node3->next = head;
	
	if (check_cycle(head))
	{
		printf("Cycle found in the linked list.\n");
	}
	else
	{
		printf("No cycle found in the linked list.\n");
	}
	
	free(node3);
	free(node2);
	free(node1);
	free(head);
	return (0);
}
