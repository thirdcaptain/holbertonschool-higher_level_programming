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

/*initialize node*/
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;

/*scan for location*/
	cursor = *head;
	while (cursor->next->n < number)
	{
		cursor = cursor->next;
	}
	if (cursor == *head)
	{
		node->next = *head;
		return(node);
	}
	else if (cursor != *head)
	{
		node->next = cursor->next;
		cursor->next = node;
	}
	else
		add_nodeint_end(head, number);

	return (node);
}
