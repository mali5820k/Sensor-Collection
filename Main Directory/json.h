#ifndef sc_json_h
#define sc_json_h
#include "json-c/json.h"

// Structs for each and every json entry required
struct json_object humidity;
struct json_object temperature;
struct json_object gps_latitude;
struct json_object gps_longitude;
struct json_object gscope_roll;
struct json_object gscope_pitch;
struct json_object gscope_yaw;
struct json_object current_image;
struct json_object error_code;
struct json_object error_message;

// Roll is x, pitch is y, yaw is z, measured in degrees.
// Temperature will be measured in degrees Celsius.
// Latitude and longitude measured in degrees.
// Humidity is a percentage.
double latitude, longitude, temperature, humidity, roll, pitch, yaw;

/* Wrapper functions for calling json_object.h functions to make json objects */
/* Check json_object.h and test1.c for more details */
int setup_json_module();
void load_json_file();
double get_humidity_from_file();
double* get_gps_position_from_file();
double* get_gscope_from_file();
double get_temperature_from_file();
char* get_image_path_from_file();
int write_to_json();
int set_error(int error_code, char* msg);

#endif
