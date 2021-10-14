
main: camctrl.o gps.o gscope.o humidity.o json.o temperature.o wrapper.o
	gcc camctrl.o gps.o gscope.o humidity.o json.o temperature.o wrapper.o -o main

jsontest: json.o jsonTester.o
	gcc json.o jsonTester.o -ljson-c -o jsontest

camctrl.o: camctrl.h CameraControl.c
	gcc -c CameraControl.c -o camctrl.o

gps.o: gps.h GPS.c
	gcc -c GPS.c  -o gps.o

gscope.o: gscope.h Gyroscope.c
	gcc -c Gyroscope.c -o gscope.o

humidity.o: humidity.h Humidity.c
	gcc -c Humidity.c -o humidity.o

json.o: json.h JSON.c
	gcc -c JSON.c -o json.o

jsonTester.o: json.h jsonTester.c
	gcc -c jsonTester.c -o jsonTester.o

temperature.o: temperature.h Temperature.c
	gcc -c Temperature.c -o temperature.o

wrapper.o: wrapper.h wrapper.c
	gcc -c wrapper.c -o wrapper.o
