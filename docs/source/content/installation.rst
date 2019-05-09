.. toctree::
   :glob:

.. _roverappinstallation:

Installation Instructions
##########################


***************
Raspbian Image
***************

This tutorial will teach your how to set up a Rover-specific Raspbian image from scratch and the basic workflow to run the Roverapp applications.

Requirements
==============

The following are the build-time dependencies required for the Roverapp:

* build-essential
* cmake
* git-core
* python-pip Python package installer
* Python 2.7
* gcc

The following are the run-time dependencies used for the Roverapp:

* Raspbian or similar distro that uses the Raspberry Pi metadata (meta-raspberrypi)
* Access Point setup (with IP 192.168.168.1)
* Python 2.7
* psutil Python module
* wiringPi library
* raspicam-0.1.2 or raspicam-0.1.3 library
* OpenCV 3.2.0 library
* Json-Cpp library
* bluetooth-dev, bluez, pi-bluetooth libraries
* bcm2835 library
* (modified) Adafruit_GFX and Adafruit_SSD1306 libraries
* paho.mqtt.c libraries


Preparing the Raspbian Image
====================================

First, you need to download a fresh Raspbian Stretch image (desktop and recommended software) from `here <https://www.raspberrypi.org/downloads/raspbian/>`_.
Then you have to write the image to your SD card, for example via `Etcher <https://www.balena.io/etcher/>`_.
Once you wrote successfully your Raspbian image on your SD card, insert it into the Raspberry Pi.

Configuring I2C, SSH and SPI
-----------------------------

After your fresh installation you will need to configure the Raspberry Pi in order to run rover-app applications.

.. note::

   Do NOT update your Raspbian image as this will take a lot of time.

Enable I2C
^^^^^^^^^^^
* Open a terminal window
* Run sudo raspi-config
* Use the down arrow to select 5 Interfacing Options
* Arrow down to P2 i2c
* Select yes when it asks you to enable SSH
* Use the right arrow to select the <Finish> button.
* Select yes when it asks to reboot.

If everything went well, the Pi should respond with `/dev/i2c-1` when you run `ls /dev/*i2c*`

Enable SSH
^^^^^^^^^^^
* Open a terminal window
* Run raspi-config
* Use the down arrow to select 5 Interfacing Options
* Arrow down to P2 ssh
* Select yes when it asks you to enable SSH
* Use the right arrow to select the <Finish> button.
* Select yes when it asks to reboot.

If everything went well, you should be able to connect to the RPI3 through ssh from other computer.

Enable SPI
^^^^^^^^^^^
* Open a terminal window
* Run raspi-config
* Use the down arrow to select 5 Interfacing Options
* Arrow down to P4 spi
* Select yes when it asks you to enable SPI
* Use the right arrow to select the <Finish> button
* Reboot your RPI3


Manual Installation Instructions
=================================

.. note::

   We are working on providing a Docker image to automate the installation process

Installing Roverapp dependencies
---------------------------------

Install CMake
^^^^^^^^^^^^^^

.. code-block:: bash
    :linenos:

    $ sudo apt-get install cmake


Install wiring pi
^^^^^^^^^^^^^^^^^^

.. code-block:: bash
    :linenos:

      $ cd ~/  && \
         git clone git://git.drogon.net/wiringPi && \
         cd wiringPi/ &&  \
         git pull origin && \
         ./build

More installation information for wiringPi are available `here <http://wiringpi.com/download-and-install/>`_.


Install jsoncpp
^^^^^^^^^^^^^^^^

.. code-block:: bash
    :linenos:

    $ sudo apt-get -y install libjsoncpp-dev && \
       sudo ln -s /usr/include/jsoncpp/json/ /usr/include/json

Install Openssl
^^^^^^^^^^^^^^^^

.. code-block:: bash
    :linenos:

    $ sudo apt-get -y install libssl-dev


Install paho.mqtt.c
^^^^^^^^^^^^^^^^^^^^^

To install paho.mqtt.c libraries for MQTT-based cloud communication, execute the following commands:

.. code-block:: bash
    :linenos:

    $ cd ~/ && \
       git clone https://github.com/eclipse/paho.mqtt.c.git && \
       cd paho.mqtt.c/ && \
       make && \
       sudo make install

If this makes problems, just try the following:

.. code-block:: bash
    :linenos:

    $ pip install paho-mqtt

Install i2c tools
^^^^^^^^^^^^^^^^^^

.. code-block:: bash
    :linenos:

   $ sudo apt-get install -y libi2c-dev i2c-tools lm-sensors


Install psutil
^^^^^^^^^^^^^^^

psutil is a performance tool library that is written in Python and that is able to provide information about GNU/Linux-based systems.

.. code-block:: bash
    :linenos:

    $ sudo pip install psutil

Install bluetooth
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash
    :linenos:

    $ sudo apt-get install -y bluez \
       libbluetooth-dev

Install raspicam
^^^^^^^^^^^^^^^^^^

.. code-block:: bash
  :linenos:

  $ cd ~/ && \
     git clone https://github.com/6by9/raspicam-0.1.3.git && \
     cd raspicam-0.1.3 && \
     mkdir -p build && \
     cd build && \
     cmake .. &&\
     make &&\
     sudo make install

.. note::

       As an alternative you can use the following git repository: `raspicam 0.1.2 <https://github.com/cedricve/raspicam.git>`_.

.. warning::

       If compilation using ``make`` command fails, one should make sure ``libmmal.so`` and ``libmmal_core.so`` is located in ``/opt/vc/lib``.
       To install these libraries, one can do a Raspberry Pi firmware update: ``sudo rpi-update``.

Install OpenCV
^^^^^^^^^^^^^^^

This installation follows the steps described `here <https://www.pyimagesearch.com/2015/10/26/how-to-install-opencv-3-on-raspbian-jessie/>`_

Dependencies

.. code-block:: bash
   :linenos:

   $ sudo apt-get install -y libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
    $ sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
    $ sudo apt-get install -y libxvidcore-dev libx264-dev
    $ sudo apt-get install -y libgtk2.0-dev
    $ sudo apt-get install libatlas-base-dev gfortran

Getting OpenCV

.. code-block:: bash
   :linenos:

    $ cd ~
     $ wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.4.1.zip
     $ unzip opencv.zip

Getting opencv contrib

.. code-block:: bash
   :linenos:

     $ wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.4.1.zip
      $ unzip opencv_contrib.zip

Compiling OpenCV

.. code-block:: bash
   :linenos:

    $ cd ~/opencv-3.4.1/
      $ mkdir build
      $ cd build
      $ cmake -D CMAKE_BUILD_TYPE=RELEASE \
	    -D CMAKE_INSTALL_PREFIX=/usr/local \
	    -D INSTALL_C_EXAMPLES=ON \
	    -D INSTALL_PYTHON_EXAMPLES=ON \
	    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.4.1/modules \
	    -D BUILD_EXAMPLES=ON ..

Check if you have any errors.
Otherwise we can compile OpenCV.
This step will take some hours from 2 up to 5-6, depending on the size of your SD card and the speed.

.. code-block:: bash
   :linenos:

   $ make -j4

Once you are done, let's install OpenCV:

.. code-block:: bash
   :linenos:

    $ sudo make install
     $ sudo ldconfig


Installing Roverapp
--------------------

After the prerequisite are fulfilled, the Roverapp can be installed.
Roverapp's installation process is simplified by using ``CMake`` tool, a semi-automated Makefile generator for GCC compiler.
Therefore, the Roverapp contains a `CMakeLists.txt <https://github.com/app4mc-rover/rover-app/blob/master/CMakeLists.txt>`_  file.

.. note::

      When adding and linking new libraries, objects, source files, or headers, the CMake file must be tailored accordingly.

Compiling
^^^^^^^^^^

.. code-block:: bash
    :linenos:

    $ cd ~
     $ git clone https://github.com/phil-hei/rover-app.git
     $ cd rover-app/
     $ ./make_roverapp.sh

Configuring Cloud connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to connect to the Hono or any other MQTT-supporting message gateway, the Rover needs to be configured with the according details such as Broker address and credentials.
A template configuration file, called `rover.conf.sample`, is given in the directory `samples`.

.. code-block:: bash
    :linenos:

    $ cd samples/

Modify that file with the required values, namely the following attributes:

.. code-block:: bash
    :linenos:

    # Configuration file for roverapp.
     ROVER_IDENTITY_C=INSERT
     MQTT_BROKER_C=INSERT
     MQTT_BROKER_PORT_C=1883
     ROVER_MQTT_QOS_C=0
     MQTT_USERNAME_C=INSERT
     MQTT_PASSWORD_C=INSERT
     USE_GROOVE_SENSOR_C=0
     USE_REDIRECTED_TOPICS_C=1

Then you need to copy the file to right location:

.. code-block:: bash
   :linenos:

   $ sudo cp rover.conf.sample /etc/rover.conf


Running Roverapp
===========================

The Roverapp is located in the `build/bin` directory along with other scripts for testing Rover's functionalities.
When started, the Roverapp connects to the Cloud and continously sends telemetry data as well as listen for incoming command messages.

.. code-block:: bash
   :linenos:

   $ cd build/bin
    $ sudo ./roverapp


.. note::

   If the installation process complains about not being able to find ``FindOpenCV.cmake`` or ``OpenCVConfig.cmake``, or any ``.cmake`` file.
   For that matter, the file must be searched and exported to the environment with commands as following:

.. code-block:: bash

      sudo find / -name *OpenCVConfig.cmake*
      cd build
      sudo OpenCV_DIR=<path/to/OpenCVConfig.cmake> cmake ..
      make
      sudo make install


Same goes with ``raspicam``:

.. code-block:: bash

      sudo find / -name *raspicamConfig.cmake*
      cd build
      sudo OpenCV_DIR=<path/to/raspicamConfig.cmake> cmake ..
      make
      sudo make install



.. _roverwebinstallation:

*************************************************
Roverweb Installation
*************************************************


Requirements
=============

The following are the build-time dependencies required for the roverweb:

* git-core

The following are the run-time used for the roverweb:

* Raspbian or similar distro that uses the Raspberry Pi metadata (meta-raspberrypi)
* Access Point setup (with IP 192.168.168.1)
* node.js with version 8.x or higher
* node.js modules: net, connect, server-static, http, socket.io, express, path, mqtt
* mjpg-streamer-experimental
* curl

Manual Installation Instructions
================================

Installing Roverweb dependencies
--------------------------------

Installing curl
^^^^^^^^^^^^^^^^

.. code-block:: bash
   :linenos:

   sudo apt-get install curl


Installing node.js and its required modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To serve web-pages and handle communications, node.js is an important dependency for Roverweb.
The following commands can be used to download and install node.js:

.. code-block:: bash
   :linenos:

   $ sudo apt-get update
    $ curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
    $ sudo apt install nodejs

Check if node.js is successfully installed:

.. code-block:: bash
   :linenos:

   $ node -v

There are additional node.js modules which are required for roverweb.
Those modules must be installed by running the following:

.. code-block:: bash
   :linenos:

   $ sudo npm install net connect serve-static http socket.io express path mqtt

.. warning::

  In case of problems while running roverweb, do this step after navigation to project directory.


Installing mjpg-streamer-experimental
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One particular mjpg-streamer version provides streaming with Raspberry Pi.
In order to install the module, execute the following commands:

.. code-block:: bash
   :linenos:

   $ sudo apt-get install cmake libjpeg8-dev
    $ git clone https://github.com/jacksonliam/mjpg-streamer.git
    $ cd mjpg-streamer-experimental
    $ mkdir build
    $ cd build
    $ cmake ..
    $ make
    $ sudo make install


Installing Roverweb
---------------------

Downloading (Fetching) Roverweb
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash
   :linenos:

  $ git clone https://github.com/app4mc-rover/rover-web.git

After roverweb is installed, there is no need to install it to any static location.
You can continue by running the server: :ref:`roverweb Getting started <roverwebstart>`
