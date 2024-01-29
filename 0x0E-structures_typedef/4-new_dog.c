#include "dog.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * new_dog - defines a new dog
 * @name: name of dog
 * @age: age of dog
 * @owner: owner of dog
 * Return: (Success)
 */
dog_t *new_dog(char *name, float age, char *owner)
{
	dog_t *p;

	p = malloc(sizeof(dog_t));

	if (p == NULL)
	{
	free(p);
	return (NULL);
	}
	else
	{
	p->name = name;
	p->age = age;
	p->owner = owner;
	return (p);
	}
}
