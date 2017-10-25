### Description
A simple python test framework that uses behave(Gherkin) and page-object model that aims to create a maintainable and reusable test code.
The system under test is a weather forecast app and the tests written carry out some of its basic functionalities.
Additional capability to take screenshots on failed scenarioes is also added.

#### Where do I start?
(Please note the some of the commands are specific to Mac users)

###### Pre-requisites:
- IDE: PyCharm or anything similar
Download PyCharm [here](https://www.jetbrains.com/pycharm/download/#section=mac)
- python 2.7
- selenium standalone server(for selenium grid):
  download the latest version [here](http://docs.seleniumhq.org/download/)

#### This is great! how do I set up this project locally?
- clone or download this project to your local machine
- set up your virtual environment and activate the same
```sh
$ cd weather-forecast-app
$ virtualenv venv
$ source venv/bin/activate
$ sudo pip install -r requirements.txt
```
- In a new terminal start up selenium grid

`java -jar selenium-server-standalone-x.xy.z.jar -role hub`

- Open another terminal and rin the following command to attach nodes to the hub

`java -jar selenium-server-standalone-x.xy.z.jar -role node  -hub http://localhost:4444/grid/register -browser browserName=firefox,maxInstances=5 -browser browserName=chrome -browser browserName=safari`

** Note: Update x.xy.z with the latest jar version that you have downloaded

- Time to test if the grid is set up correctly on the local machine
Open a browser and navigate to this [url](http://localhost:4444/grid/console)

###### With minimum setup you are now good to run the tests:
This will run only the test scenario with the tag @local in firefox browser
``` sh
$ behave --tags=local -D BROWSER=firefox
```


References:

http://selenium-python.readthedocs.io/page-objects.html

https://github.com/SeleniumHQ/selenium/wiki/Grid2
