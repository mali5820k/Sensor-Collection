#include <stdio.h>
#include <stdlib.h>

#include "json.h"
#include "gps.h"
#include "gscope.h"
#include "humidity.h"
#include "camctrl.h"
#include "temperature.h"

enum error_codes { COMPLETEPANIC, /* Restart program */
                          DHT11,         /* Rerun init function of dht-11 */
                          CAMSERVO1,     /* Rerun init function of servo 1 */
                          CAMSERVO2,     /* Rerun init function of servo 2 */
                          BERRYSENSOR    /* Rerun init function of Berry sensor(s) */
};

// Functions to restart each sensor
// Return a 0 if successful, and a 1 when not.
int init_DHT_11();
int init_Berry_gps();
int init_Berry_gscope();
int init_Berry_temperature();
int init_cam_ctrl();

// These two inits are special and can exit the system if
// any of the above inits causes an error.
void init_all_sensors();
void init_json();

// Functions to set parameters for every sensor's data
// Return a 0 if successful, and a 1 when not.
int set_humidity();
int set_temperature();
int set_gps_position();
int set_gscope();
int set_image_path();