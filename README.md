# Cabelchecker

Enable I2c and remote GPIO on RPI

intalling software:
`git clone https://github.com/Hammerboy1/Cabelchecker.git`

installing Pyqt5:
`sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools`

Copying files to correct location:
```bash
cp ./*Desktopicon /home/pi/Desktop
cp ./*listen-for-shutdown.py* /home/pi/
cp ./*Cabelcheck.sh* /home/pi/ 
sudo cp ./*Cabelcheck.desktop*  /etc/xdg/autostart
```

`chmod +x /home/pi/Cabelcheck.sh`
