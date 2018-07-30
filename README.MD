# Old Radio 

This repo contains the source code used to configure my 1941 radio.  This radio as been 
setup so that it is now supports chromecast and bluetooth.  Retro Electronics redone so 
that it is now up-to-date.    

## Getting Started

Your will need a raspberry pi zero. The radio was a 1941 rca radio and has been updated
to chromecast and bluetooth.  All buttons are configured to control a modern amp and speaker
box that i built.  The amp is found on Amazon [here](https://www.amazon.com/gp/product/B074FR4B7H/ref=oh_aui_detailpage_o05_s01?ie=UTF8&psc=1).  

### Installing

Steps to get the code working on your pi:

1. Clone this repo 
```
git clone https://github.com/gschaetz/oldradio.git
```
2. cd into the repo
```
cd ./oldradio/
```
3. Use the most recent version of Raspbian for your pi
4. sftp into your raspberry pi
```
ssh pi@(your ip)
```
3. Create a directory for developement and logs
```
mkdir development
cd ./development
mkdir logs
```
4. Open a second bash shell 
5. sftp in to the pi
```
sftp pi@(your ip)
```
5. Change remote directory to development/
```
cd development/
```
6. Copy oldradio.py to remote
```
put oldradio.py
put launcher.sh
```
7. Use shell for ssh and add crontab.  Add the following to the crontab
```
sudo crontab -e
Add the following line:
@reboot sleep 10 && sudo -u pi bash /home/pi/development/launcher.sh > /home/pi/development/logs/cronlog 2>&1
```
8. Reboot pi
```
sudo shutdown
```
9. Restart pi

## Authors

* **Gary Schaetz** - *Builder of fun stuff* 