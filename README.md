Software:

* InMoov2: https://github.com/MyRobotLab/InMoov2
* see: Setup Software in docs
* java8 \& python: https://www.java.com/en/download/manual.jsp https://www.python.org/downloads/

Docs:
https://inmoov.fr/inmoov2-in-nixie/    \*\*\*

* https://inmoov.fr/how-to-start-myrobotlab/?doing\_wp\_cron=1780418428.8862380981445312500000
* https://inmoov.fr/
* https://github.com/MyRobotLab/myrobotlab/blob/develop/README.md#starting-myrobotlab

look at:
https://github.com/konynour/MRL-DEV
https://myrobotlab.org/tutorials

Drivers:

* Xbox Kinect: ?

Steps To Use:

* plug in power supply
* connect USB to laptop
* open C:/mrl/myrobotlab-x.x.xxxx/myrobotlab.bat
* select fingerprint
* select gears
-> controllers right \& left work

  * COM5 \& COM4 arduino have the .ino file to control
  * make sure using PORT COM4 for right controller \& COM5 for left (type it into each controller)

Initial Setup:

* https://inmoov.fr/inmoov2-in-nixie/

Getting all components to move:

* set right controller COM4
* set left controller COM5
* select each individual component \& attempt to move it,

  * if it cannot, adjust limits
  * if it still cannot, detach from current side \& switch to the other
  * don't alter pins at the moment
  * some way to save these in the future???
  * only two that don't work rn are top \& low stom

Discord for help:...
https://discord.gg/AfScp5x8r5

Driver Issue Solved:

* turned off setting in windows security -> device security -> core isolation, memory integrity

Listening/ Voice Recognition:

* turn on ear
* set up a wake up word
* speak near the microphone
* check log
* eventually, will want to create responses to specific recognized speech

Chat:

* Chat works via Nixie, attempt LLM communication \& microphone use soon
* LLMs require API key

Scripts:

* https://myrobotlab.org/service/Python
* make sure EVERY component is turned on and ready!!!
* execute a script from the python section

  * make sure you save your edits

todo:
-> look at possible or premade scripts from the internet to use, test them

* current issues:
none :3

