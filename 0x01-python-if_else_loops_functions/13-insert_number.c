#include "lists.h"

/**
 * insert_node - inserts a node and number into a sorted linked list
 * @head: pointer to pointer to first node of listint_t list
 * @number: integer to be included in new node
 *
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *cursor;
	listint_t *end;

/*initialize node*/
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;
	cursor = *head;
	end = *head;
/*cursor at head & end*/
	if (*head == NULL)
		return(add_nodeint_end(head, number));

	while (end->next != NULL)
		end = end->next;

	if (number > end->n)
		return(add_nodeint_end(head, number));

/*cursor not at end*/
	while (cursor->next->n < number)
		cursor = cursor->next;

	if (cursor == *head)
	{
		node->next = *head;
		*head = node;
		return(node);
	}
	else
	{
		node->next = cursor->next;
		cursor->next = node;
	}

	return (node);
}
