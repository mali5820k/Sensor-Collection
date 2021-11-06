cd ~/
git clone git://git.drogon.net/wiringPi
cd wiringPi
git pull origin
sudo ./build
sudo gpio -v
sudo gpio readall
