# Functions to restart each sensor
# Return a 0 if successful, and a 1 when not.
def init_DHT_11():
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
    pass
def init_json():
    pass

# Functions to set parameters for every sensor's data
# Return a 0 if successful, and a 1 when not.
def set_humidity():
    pass
def set_temperature():
    pass
def set_gps_position():
    pass
def set_gscope():
    pass
def set_image_path():
    pass