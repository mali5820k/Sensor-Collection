#include "json.h"

int readData(char *name, void *value)
{

}

int writeData(char *name, void *value)
{
	/* Need to know how to check for value's type here */
	/* Check json_object.c for json_object_get_type functions */
	json_object *nObject;
	nObject = json_object_new_object();
	json_object_object_add(nObject, "abc", json_object_new_int(12));
}

int writeError(char *errName, char* msg)
{
	
}

int readError(char *errName)
{
	
}