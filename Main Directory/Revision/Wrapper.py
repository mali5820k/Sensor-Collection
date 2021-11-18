import Humidity
import CameraControl
import GPS
import Gyroscope
import Temperature

# Sensor Data buffers
dataBuffer = {}


# Functions to restart each sensor
# Return a 0 if successful, and a 1 when not.
def init_DHT_11():
    Humidity.setPin(22)
    pass


def init_Berry_gps():
    pass


def init_Berry_gscope():
    pass


def init_Berry_temperature():
    pass


def init_cam_ctrl():
    pass


# These two inits are special and can exit the system if
# any of the above inits causes an error.
def init_all_sensors():
	init_DHT_11()
	init_Berry_gps()
	init_Berry_gscope()
	init_Berry_temperature()
	init_cam_ctrl()

# May not need this anymore
def init_json():
    pass


# Functions to get parameters for every sensor's data
# Return a -1 if not successful
def get_humidity():
	humidity = Humidity.get_humidity()
	dataBuffer["Humidity"] = humidity


def get_temperature():
    pass


def get_gps_position():
    pass


def get_gscope():
    pass


def set_image_path():
    pass

def capture_image():



def main():
	pass

if __name__ == "__main__":
	main()