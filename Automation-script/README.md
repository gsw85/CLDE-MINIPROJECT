# Node-RED
Import this json file to Node-RED in order to load the flow for this mini-project.
<br>
## Automation Script
The timestamp is injected as long as 10 seconds to the exec node, meaning that it will keep running the exec node every 10 seconds interval. In the exec node, command “python3 /home/pi/Mini-Project-CDLE/Code/Sensor_Data.py” is used in order to get the output from the sensors.

<p align="center">
  <img width="500" height="340" src="https://github.com/fikrimusa/CDLE-Mini-Project/raw/master/Picture/Node-RED (1).png">
</p>


The UI-builder node is used to execute an AI model on the dashboard. Copy code sketch.js and index.html from p5.js in properties and save it. Template node is used for skymind logo and real-time clock and date using javascript.


<p align="center">
  <img width="500" height="340" src="https://github.com/fikrimusa/CDLE-Mini-Project/raw/master/Picture/Node-RED (2).png">
</p>
