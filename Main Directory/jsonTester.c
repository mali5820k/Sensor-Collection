#include <stdlib.h>
#include <stdio.h>
#include "json.h"

void readTest1();
void writeTest1();

int main(int argc, char **argv)
{
    if (argc != 2) {
        printf("\nUsage: ./executable templateJsonFilePath, outputFileName");
        exit(EXIT_FAILURE);
    }

    // Haven't implemented the imgDirectory path test yet.

    // Initialize 
    setup_json_module(argv[0], argv[1]);

    // Json file read and write tests:
    readTest1();
    writeTest1();
}

void readTest1()
{
    double humidityRead, temperatureRead;
    double *gpsRead, *gscopeRead;
    char *imgPathRead;

    load_json_file();
    humidityRead = get_humidity_from_file();
    temperatureRead = get_temperature_from_file();
    gpsRead = get_gps_position_from_file();
    gscopeRead = get_gscope_from_file();
    imgPathRead = get_image_path_from_file();

    printf("\nHumidity is: %d\n", humidityRead);
    printf("\nTemperature is: %d *C\n", temperatureRead);
    printf("\nGPS position is: %d\n", get_humidity_from_file());
    printf("\nGyroscope rotation is: %d, %d, %d\n", gscopeRead[0], gscopeRead[1], gscopeRead[2]);
    printf("\nImage output path is: %s\n", imgPathRead);
}

void writeTest1()
{
    _temperature = 27.21;
    _humidity = 20;
    _latitude = 40;
    _longitude = 90;
    _roll = 28;
    _pitch = 50;
    _yaw = 100;

    write_to_json();
}