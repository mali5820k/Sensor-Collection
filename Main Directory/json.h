#ifndef sc_json_h
#define sc_json_h
#include "json-c/json.h"
#include "json-c/json_object.h"

/* Wrapper functions for calling json_object.h functions to make json objects */
/* Check json_object.h and test1.c for more details */
int readData(char *name, void *value);
int writeData(char *name, void *value);
int writeError(char *errName, char* msg);
int readError(char *errName);

#endif
