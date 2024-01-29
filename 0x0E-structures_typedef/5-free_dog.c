#include "dog.h"
#include <stdlib.h>
/**
 * free_dog - free a struct
 * @d: pointer to struct
 * Return: (Success)
 */
void free_dog(dog_t *d)
{
	free(d);
}
