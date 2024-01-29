#include "dog.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * print_dog - print and initialize a struct
 * @d: struct
 * Return: (Success)
 */
void print_dog(struct dog *d)
{
	char *ptr1;
	char *ptr2;
	double *ptr3;
	struct dog *ptr0;

	ptr1 = malloc(sizeof(d->name));
	ptr2 = malloc(sizeof(d->owner));
	ptr3 = malloc(sizeof(d->age));
	ptr0 = malloc(sizeof(*d));
	
	if (ptr0 == NULL)
	{
	free(ptr0);
	}
	else
	{
	if (ptr1 == NULL)
	{
	printf("Name: (nil)\n");
	free(ptr1);
	}
	if (ptr2 == NULL)
	{
	printf("owner: (nil)\n");
	free(ptr2);
	}
	if (ptr3 == NULL)
	{
	printf("age: (nil)\n");
	free(ptr3);
	}

	if (ptr1 != NULL)
	{
	printf("Name: %s\n", d->name);
	free(ptr1);
	}
	if (ptr3 != NULL)
	{
	printf("Age: %f\n", d->age);
	free(ptr2);
	}
	if (ptr2 != NULL)
	{
	printf("Owner: %s\n", d->owner);
	free(ptr3);
	}
	}

}
