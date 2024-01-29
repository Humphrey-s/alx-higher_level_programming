#include "dog.h"
#include <stdio.h>
/**
 * init_dog - initializes a variable of type dog
 * @d: structure
 * @name: name of dog
 * @age: age of dog
 * @owner: owner of dog
 * Return: (Success)
 */
void init_dog(struct dog *d, char *name, float age, char *owner)
{
	 d->name = name;
	d->age = age;
	d->owner = owner;
}
