Software:
- InMoov: https://github.com/MyRobotLab/InMoov
- InMoov2: https://github.com/MyRobotLab/InMoov2
- see: Setup Software in docs
- java8 & python: https://www.java.com/en/download/manual.jsp https://www.python.org/downloads/

Docs:
- https://myrobotlab.org/service/InMoov
- https://inmoov.fr/how-to-start-myrobotlab/?doing_wp_cron=1780418428.8862380981445312500000
	> looking at Older Versions rn
	- missing file: https://github.com/MyRobotLab/myrobotlab/releases/tag/1.0.2693  
		> FOUND in https://github.com/konynour/MRL-DEV
- https://inmoov.fr/
- https://github.com/MyRobotLab/myrobotlab/blob/develop/README.md#starting-myrobotlab
	- https://inmoov.fr/inmoov2-in-nixie/

look at:
https://github.com/konynour/MRL-DEV
https://myrobotlab.org/tutorials

Drivers:
- Xbox Kinect: ?

Steps To Use:
- plug in power supply
- connect USB to laptop
- open START_INMOOV.bat   |  open C:/mrl/myrobotlab-x.x.xxxx/myrobotlab.bat
- ...

Discord for help:...
https://discord.gg/AfScp5x8r5

Driver Issue Solved:
- turned off setting in windows security -> device security -> core isolation, memory integrity

todo:
- solve java issue(s)
* detect Arduino !!!!

- look at hardware setup
- view existing issues & docs (if possible)

- current issues:
	- Arduino not detected when testing on IM2 (driver issue? hardware issue?)
	- IM1 doesn't open without combining both IM1 folders into the mrl one... AND moving the jar file into that mrl folder HOWEVER this is an issue bc I only have the jar from the 1.1.x release & not the stable 1.0.2xxx