#include <stdio.h>
#include <strings.h>
// Below two imports are used for checking if a directory exists for
// the mkdir function.
#include <sys/types.h>
#include <sys/stat.h>
// If we need to have the json files stored in a specific directory, we can use this
// chdir, and mkdir functions.
#include <unistd.h>

#include "json.h"

// a 4MB buffer should be enough to load JSON contents
#define BUFFER 2*1024*1024

struct json_object *parsed_json_file;

char fileName[BUFFER];
char outputFileName[BUFFER];


int setup_json_module(char* _fileName, char* _outputFileName)
{
        int error1, error2 = 0;
        error1 = strcpy(fileName, _fileName);
        error2 = strcpy(outputFileName, _outputFileName);

        if (error1 || error2)
                return 1;

        return 0;
}

void load_json_file()
{
	FILE *file;
        // Open json file and read the data from it:
        file = fopen(fileName, "r");
	char jsonReadBuffer[BUFFER];
        fread(jsonReadBuffer, BUFFER, 1, file);
        fclose(file);

        // Now using the json-c library, we'll parse this file
        // that we read and organize it into the provided struct
        parsed_json_file = json_tokener_parse(jsonReadBuffer);

        // Load the parameters from the json file for each sensor's
        // data type:
        json_object_object_get_ex(parsed_json_file, "humidity", &humidity);
        json_object_object_get_ex(parsed_json_file, "temperature", &temperature);
        json_object_object_get_ex(parsed_json_file, "gps-latitude", &gps_latitude);
        json_object_object_get_ex(parsed_json_file, "gps-longitude", &gps_longitude);
        json_object_object_get_ex(parsed_json_file, "gscope-roll", &gscope_roll);
        json_object_object_get_ex(parsed_json_file, "current-image", &current_image);
        json_object_object_get_ex(parsed_json_file, "error-code", &error_code);
        json_object_object_get_ex(parsed_json_file, "error-message", &error_message);
}

double get_humidity_from_file()
{
        return json_object_get_double(&humidity);
}

double* get_gps_position_from_file()
{
        double position[2] = {json_object_get_double(&gps_latitude), json_object_get_double(&gps_longitude)};
        return position;
}

double* get_gscope_from_file()
{
        double rotValues[3];
        rotValues[0] = json_object_get_double(&gscope_roll);
        rotValues[1] = json_object_get_double(&gscope_pitch);
        rotValues[2] = json_object_get_double(&gscope_yaw);

        return rotValues;
}

double get_temperature_from_file()
{
        return json_object_get_double(&temperature);
}

char* get_image_path_from_file()
{
        char* img_path = json_object_get_string(&current_image);
        return img_path;
}

int write_to_json()
{
        /* Need to know how to check for value's type here */
        /* Check json_object.c for json_object_get_type functions */
        /*
        json_object *nObject;
        nObject = json_object_new_object();
        json_object_object_add(nObject, "abc", json_object_new_int(12));
        */

        // Write all json fields and values to the json file.
        char jsonWriteBuffer[BUFFER];
        strcpy(jsonWriteBuffer, json_object_to_json_string(&humidity));
        strcat(jsonWriteBuffer, json_object_to_json_string(&temperature));
        strcat(jsonWriteBuffer, json_object_to_json_string(&gps_latitude));
        strcat(jsonWriteBuffer, json_object_to_json_string(&gps_longitude));
        strcat(jsonWriteBuffer, json_object_to_json_string(&gscope_roll));
        strcat(jsonWriteBuffer, json_object_to_json_string(&gscope_pitch));
        strcat(jsonWriteBuffer, json_object_to_json_string(&gscope_yaw));
        strcat(jsonWriteBuffer, json_object_to_json_string(&error_code));
        strcat(jsonWriteBuffer, json_object_to_json_string(&error_message));

        FILE *file;
        file = fopen(outputFileName, "w+"); // Overwrite the entire contents of the file
        //char jsonWriteBuffer[BUFFER];
        fwrite(jsonWriteBuffer, BUFFER, 1, file);
        fclose(file);
       
}

int set_error(int error_code, char* msg)
{
        int error1, error2 = 0;
        error1 = json_object_set_int(&error_code, error_code);
        error2 = json_object_set_string(&error_message, msg);

        if (error1 || error2) {
                printf("ERROR: cannot set error to json objects.\n");
                return 1;
        }

        return 0;
}