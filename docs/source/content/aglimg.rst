.. toctree::
   :glob:

Starting with AGL Image - Quick Start (for Rover 0.1.0)
########################################################

Downloading the Image
==============================================================

Download the 0.1.0 Image from `this link <https://owncloud.idial.institute/s/rZ1ULqVhX9CHjrl?path=%2F>`_.

Download Etcher from `this link <https://etcher.io/>`_ and flash the image to the SD card.

Configuration Steps (One Time Only per Rover)
==============================================================

To demonstrate the rover, you'll need Rover Telemetry UI.

First install node.js by following `http://nodesource.com/blog/installing-node-js-tutorial-ubuntu/ <http://nodesource.com/blog/installing-node-js-tutorial-ubuntu/>`_ for Ubuntu 16.04.

On your local machine, to download Rover Telemetry UI:

.. code-block:: javascript
   :linenos:
   
   git clone https://github.com/app4mc-rover/rover-telemetry-ui.git
   
On your local machine, to download dependencies (If you don't have node.js installed, first install node.js):

.. code-block:: javascript
   :linenos:
   
   cd rover-telemetry-ui
   sudo npm install net connect serve-static http socket.io express path mqtt


	   


Running Steps
==============================================================


On your local machine, to run the Rover Telemetry UI server:

.. code-block:: javascript
   :linenos:   
   
	   cd scripts/
	   sudo node start_rovertelemetryui.js

Now, configure rover.conf on your local machine and copy it to the rover:

	.. code-block:: bash
	   :linenos:
	   cd ~
	   wget 'https://raw.githubusercontent.com/app4mc-rover/rover-app/0.1.1/samples/rover.conf.sample'
	   mv rover.conf.sample rover.conf
	   nano rover.conf

	.. code-block:: ini
	   :linenos:
	   
	   # Configuration file for roverapp. 
	   # Place in /etc/rover.conf
	   ROVER_IDENTITY_C=1
	   MQTT_BROKER_C=127.0.0.1
	   MQTT_BROKER_PORT_C=1883
	   ROVER_MQTT_QOS_C=0
	   MQTT_USERNAME_C=sensor1@DEFAULT_TENANT
	   MQTT_PASSWORD_C=hono-secret
	   USE_GROOVE_SENSOR_C=0
	   USE_REDIRECTED_TOPICS_C=0
	   HONO_HTTP_HOST_C=idial.institute
	   HONO_HTTP_PORT_C=8080
	   HONO_HTTP_TENANT_NAME_C=DEFAULT_TENANT
	   HONO_HTTP_DEVICE_ID_C=4711
	   HONO_HTTP_REGISTER_PORT_C=28080
	   HONO_HTTP_USERNAME_C=sensor1
	   HONO_HTTP_PASSWORD_C=hono-secret

The configuration file should look like the one above. It is space sensitive so be sure not to introduce any unnecessary whitespaces or blank characters to the format. You should configure ``MQTT_BROKER_C`` with the exact hostname of the MQTT broker that you will use. If you don't have one, you can install one to your local machine by using the following:

	.. code-block:: bash
	   :linenos:
	   
	   sudo apt-get install mosquitto

If you have chosen to use this mosquitto broker, you should configure ``MQTT_BROKER_C`` with your IP address. On a Linux machine you can find out your IP address with:

	.. code-block:: bash
	   :linenos:
	   
	   ifconfig

For testing only, you don't have change the ``MQTT_BROKER_PORT_C``, ``MQTT_USERNAME_C``, ``MQTT_PASSWORD_C`` values.

If you are using a Groove sensor, change ``USE_GROOVE_SENSOR_C`` to 1, default is 0.

If you are planning to redirect messages from Eclipse Hono, change ``USE_REDIRECTED_TOPICS_C`` to 1, default is 0.

Now, copy the configured rover.conf to the rover. For this you'll need to boot your rover with the recently flashed SD card.

Copy the configuration file from your PC (fill in the <rover-ip-address>):

	.. code-block:: bash
	   :linenos:
	   
	   sudo apt-get install rsync
	   rsync -r rover.conf root@<rover-ip-address>:/etc/rover.conf


(If you didn't already) SSH into your rover by using (fill in the <rover-ip-address> ):

If you dont know the rover's IP address you can either use Nmap on Linux (i.e. sudo nmap -sn 192.168.1.0/24), or Advanced IP Scanner on Windows.

	.. code-block:: bash
	   :linenos:
	   
	   ssh root@<rover-ip-address>

Once SSHed, kill the existing roverapp:

	.. code-block:: bash
	   :linenos:
	   
	   killall roverapp

Start the new roverapp, type:

	.. code-block:: bash
	   :linenos:
	   
	   /projects/rover-app/build/bin/roverapp

   
Go to your web browser and find the Rover Telemetry UI at ``http://<your host address>:5055/rovertelemetryui.html``.


Killing Roverapp
==============================================================

Press Ctrl + C a few times



