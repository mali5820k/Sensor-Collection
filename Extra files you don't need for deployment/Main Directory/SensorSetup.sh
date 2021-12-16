# Install gpsd daemon
sudo apt install gpsd-clients gpsd -y

echo 'Change the DEVICES="" line to DEVICES"/dev/serial0"'
sleep 2
sudo nano /etc/default/gpsd
