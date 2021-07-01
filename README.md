<h1 align="justify"> Interfacing three different sensors with Raspberry Pi through different protocols, presenting the sensor data, and integrating an AI model on a dashboard. </h1>
The project used Raspberry Pi as a central control unit coupled with three different sensors that communicate different communication protocols and display all sensor data on a dashboard. To also integrate an AI model on the dashboard. 
<br>
<br>
<p align="center">
  <img width="500" height="340" src="https://github.com/fikrimusa/CDLE-Mini-Project/raw/master/Picture/Project_description.png">
</p>

## Walkthrough of steps to install and run the project


### Prerequisites
The project has been developed and tested on Raspbian operating system.
<br>
### Hardware requirements
1.  Raspberry Pi 4 Model B 8GB.
2.  Ultrasonic sensor (US100).
3.  Digital intensity sensor (BH1750FVI).
4.  Temperature sensor (TMP36).
5.  RPi Approved Phidisk Class10 U1 MicroSD-64GB.
6.  MCP3008 - 8-Channel 10-Bit ADC With SPI Interface.
7.  Logitech USB camera C270 model.
8.  USB microSD Card Reader and Writer.
9.  Raspberry Pi 4 Power Switch Supply Cable USB C.
10. Soldering tools (Soldering Iron, Solder Wire, Desoldering Pump, Soldering Iron Stand, Cleaning Sponge, Tweezers, Wire Stripper/Cutter).
11. Multimeter.
### Software requirements.
1.  Raspbian operating system.
2.  Node-RED.
***
## Raspbian operating system
The installation of Raspberry Pi operating system can be done by manually or automatically. Recommended to install automatically because it saves a lot of time.

1. Installation for Raspberry Pi operating system (Manually)
<br> - Format SD card
<br> - Open file explorer, click format sd card
<br> - File system = FAT32 (Default).

2. Install OS Raspberry Pi (Raspbian)
<br> - Install BalenaEtcher.
<br> - Open BalenaEtcher, Select Image (Installed OS zip file), select sd card and flash.

3. Setup in Raspberry Pi - Download Raspbian (Recommended).

4. Update Raspberry Pi
- Open terminal type
```linux 
sudo apt-get update
```
- Then,
```linux 
sudo apt-get upgrade
```
- Reboot.
```linux 
sudo reboot
```
<br/>
5. Installation for Raspberry Pi operating system (Automatically)
<br> - Install Raspberry Pi Imager
<br> - Format SD card
<br> - Choose operating system and install
***

## Node-RED
Running on Raspberry Pi. Installing and Upgrading Node-RED.

1.  Running the following command will download and run the script. If you want to review the contents of the script first, you can view it here.
```linux
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
```

2.  This script will:
+ remove the pre-packaged version of Node-RED and Node.js. if they are present.
+ install the current Node.js LTS release using the NodeSource. If it detects Node.js is already installed from NodeSource, it will ensure it is at least Node 8, but otherwise leave it alone
+ install the latest version of Node-RED using npm
+ optionally install a collection of useful Pi-specific nodes
+ setup Node-RED to run as a service and provide a set of commands to work with the service

3.  The install script for the Pi also sets it up to run as a service. This means it can run in the background and be enabled to automatically start on boot.

4.  The following commands are provided to work with the service:

+ node-red-start (this starts the Node-RED service and displays its log output. Pressing Ctrl-C or closing the window does not stop the service; it keeps running in the background)

+ node-red-stop (this stops the Node-RED service)

+ node-red-restart (this stops and restarts the Node-RED service)

+ node-red-log (this displays the log output of the service)

5.  You can also start the Node-RED service on the Raspbian Desktop by selecting the Menu -> Programming -> Node-RED menu option.
***

## AI Model
In this mini project, an object detection model has been used in order to demonstrate the AI model on the dashboard. Object detection model that aims to localize and identify multiple objects in a single image. It uses a cocossd dataset where it contains hundreds of thousands of images with millions of already labeled objects for training. The Common Objects in Context (COCO) dataset is one of the most popular open source object recognition databases used to train deep learning programs.

  The model is capable of detecting 80 classes of objects. (SSD stands for Single Shot MultiBox Detection). The green bounding box used for indicates an object for example person, tie, bottle etc. At the top left corner, shows the type of object and confidence level of the object. It uses html code to display “Object Detection using COCOSSD” word.




## Dashboard
### Real Time Sensor Data
The real-time sensors data dashboard presents three different sensor readings and also a line chart for each sensor readings. Temperature reading use gauge indicator, light level use level indicator and distance reading use text and all of these reading are real-time. 

The line chart displayed the sensor reading against the time. Skymind logo also shows at the top of the dashboard and real-time clock and date that are up-to-date time by time.

<p align="center">
  <img width="500" height="340" src="https://github.com/fikrimusa/CDLE-Mini-Project/raw/master/Picture/Step-by-step (1).png">
</p>

### Real Time Object Detection
In the object detection dashboard, it is actually from p5.js. It works exactly like p5.js since the codes are similar. It uses an iframe in order to display the object detection webpage and run the object detection model.

<p align="center">
  <img width="500" height="340" src="https://github.com/fikrimusa/CDLE-Mini-Project/raw/master/Picture/Step-by-step (5).png">
</p>
