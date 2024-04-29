#include <stdlib.h>

/* Definition for singly-linked list */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: Pointer to the head of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list) {
    listint_t *slow = list, *fast = list;

    while (slow && fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;

        /* If slow and fast pointers meet, there is a cycle */
        if (slow == fast)
            return 1;
    }

    /* No cycle found */
    return 0;
}
