#include "wrapper.h"

// Implement these below functions so error control team can access them.
int init_DHT_11()
{
        return 0;
}

int init_Berry_gps()
{
        return 0;
}

int init_Berry_gscope()
{
        return 0;
}

int init_Berry_temperature()
{
        return 0;
}

int init_cam_ctrl()
{
        return 0;
}

void init_all_sensors()
{
        // Init section for all sensors:
        // each sensor or component should have an init function instead
        // of a main function, simply to setup the GPIO pins that sensor
        // or component needs.
        // 

}

void init_json()
{
        if (setup_json_module()) {
                printf("ERROR: Could not initialize JSON module!\n");
                exit(EXIT_FAILURE);
        }
        load_json_file();
}

int main(int argc, char **argv)
{
        // JSON init
        init_json();

        // Init section for all sensors:
        // each sensor or component should have an init function instead
        // of a main function, simply to setup the GPIO pins that sensor
        // or component needs.
        init_all_sensors();
}
