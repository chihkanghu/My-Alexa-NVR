# Alexa, play my NVR recordings

A simply project demostrates how to voice-control a CGI based NVR via MQTT service via both Raspberry Pi and Alexa echo dot.

![alt tag](https://github.com/chihkanghu/My-Alexa-NVR/blob/master/thesystem.png?raw=true)

# The Video
Visit the demo video at 
[My voice-controlled network video recorder](https://www.youtube.com/watch?v=eVELFj-NKZg)

# Getting Started
Prepare the following devices:

* Alexa echo dot
* Raspberry Pi 3
* LILIN NVR404c
* LILIN IP camera
* A network switch for Internet access

![alt tag](https://github.com/chihkanghu/My-Alexa-NVR/blob/master/diagram.png?raw=true)

Connect all these devices to the network switch.

![alt tag](https://github.com/chihkanghu/My-Alexa-NVR/blob/master/diagram.png?raw=true)

# Prerequisites

* Knowledge of Node.js, MQTT, CGI, Python
* Access of your Alexa developer console
* Access of your AWS Lambda function
* LILIN NVR IR over HTTP SDK

# Installing

Raspberry Pi:

sudo pip install paho-mqtt

or 

sudo pip3 install paho-mqtt


# Setup
### Alexa Skills
* Visit your Alexa developer console.
* Click on Alexa Skills Kit button.
* Click on Get Started button.
* Click on Add a New Skill.
* Enter "PlayMyNVR" for the name of Skill Information. 
* Enter "my nvr" for the Invocation Name of Skill Information.
* Click on Interaction Model.
* Copy and paste Intent Schema from my source code.
* Copy and paste Sample Utterances from my source code.
* Click on Configuration.
* Copy and paste AWS Lambda ARN where you will later get from AWS Lambda function.

### AWS Lambda
* Visit your AWS developer console.
* Click on Lambda service.
* Click on Create a Lambda function.
* Select blueprint, hello-world, A starter AWS Lambda function.
* Configure triggers by choosing Alexa Skills Kit.
* Give HelloNVR to the name under Configure triggers.
* Choose existing Role under Select Configure function.
* Click on Next and Create Function buttons.
* Go back to Lambda function and select HelloNVR function.
* Click on Code tab and select Upload a .zip file.
* Upload mynvr.zip file to the Lambda function.
* Copy ARN code on top right of the Lambda function to your Alexa skill.
* Click on Test button and make sure that you see "Execution result: succeeded".
* Go back to Alexa Skills.

Up to this point, you can give it a try and see if your Lambda Node.js can communicate your Alexa skills.  Go back to Alexa developer console and click on Test page.  Enter the utterance, go live, and click Ask button.  In Lambda Response, it shows the correspondent text.  You can click on Listen button.  The text, stop playing, is later spoke by Alexa echo dot.  

### Raspberry Pi
* Install paho-mqtt
* Copy and paste my Python code
* Run the Python code as 

sudo python app.py

### The NVR
* Make sure that the NVR is within the same subnet as your Raspberry Pi.
* Modify gv_ipaddress, gv_username, gv_password accordingly for the NVR in app.py.

After above steps, you can start to talk to your Alexa to operate your NVR by saying:

# Examples

Alexa, ask my NVR go channel 1

Alexa, ask my NVR playback

Alexa, ask my NVR go sixteen view


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Node.js [MQTT.js] (https://www.npmjs.com/package/mqtt)
* [Never too early for a Christmas IoT”] (http://blog.alexellis.io/christmas-iot-tree/) by Alex Ellis 
* MQTT service via YPCloud, [mqtt.cc] (mqtt.cc)
* [paho-mqtt] (https://www.npmjs.com/package/paho-mqtt)
