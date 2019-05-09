.. toctree::
   :glob:

Introduction
#########################

**Rover** is an open-source mobile robot that is designed to demonstrate the outcomes of the `Eclipse APP4MC <http://www.eclipse.org/app4mc>`_ and `Eclipse Kuksa <https://www.eclipse.org/kuksa/>`_ research projects.
It features applications and tooling required to address complex research fields such as cloud communication, open-source tooling, or multi-core and cluster computing.
The Rover is equipped with powerful sensors, motors, and display units to interact with the physical world.
Furthermore, Rover uses `Eclipse PolarSys project <http://polarsys.org/polarsys-rover-user-story-application-platform-project-multicore-app4mc>`_ for its chassis and mechanics.

.. image:: ../roverstatic/images/rover11_2017.png
   :width: 60%
   :align: center
   :alt: ../roverstatic/images/rover11_2017.png

.. raw:: html

   <iframe width="700" height="500" src="https://www.youtube.com/embed/-YKgCpiWNCw" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

*************************************************
Motivations and Research
*************************************************

Rover is used as a demonstrator for two main research subjects:

.. image:: ../roverstatic/images/APP4MCLogo.png
   :width: 19%
   :align: center
   :alt: ../roverstatic/images/APP4MCLogo.png

Model-based Multicore Software Development
  * Based on the `Eclipse APP4MC <http://www.eclipse.org/app4mc>`_ platform for engineering embedded multi- and many-core software systems
  * For this purpose, threads are designed run in a schedulable and traceable fashion (with the help of timing library)
  * System traces are taken in Common Trace Format using Linux' perf profiler and custom created scripts
  * APP4MC is used for modeling and deployment outcomes


.. image:: ../roverstatic/images/KUKSA.png
   :width: 25%
   :align: center
   :alt: ../roverstatic/images/KUKSA.png


Cloud-based Communication
  * Based on the `Eclipse KUKSA <https://projects.eclipse.org/proposals/eclipse-kuksa>`_ ecosystem and more precisely on the message gateway `Eclipse Hono <https://www.eclipse.org/hono/>`_
  * Rover uses the `Eclipse Paho <https://www.eclipse.org/paho/>`_ MQTT client to connect to the message gateway of cloud instances in order to send telemetry data and receive driving commands


  .. image:: ../roverstatic/images/rover_infra2_exp.png
     :width: 100%
     :align: center
     :alt: ../roverstatic/images/rover_infra2_exp.png

*************************************************
Infrastructure
*************************************************

The Rover features Cloud communication infrastructure, sensor driving, display unit (such as OLED displays) utilization, bluetooth communication, image processing, and behavior modes (such as Parking, Adaptive Cruise Control, Manual Driving, and Booth Modes).
It also features drivers for sensors such as magnetometers, accelerometers, various ultrasonic sensors, and camera modules.
Furthermore, OLED display, buttons, a buzzer are utilized.

A small yet crucial portion of Rover's infrastructure (especially addressing network infrastructure) is given below.
Rover uses Javascript Object Notation (JSON) as data format for the information that is sent and received between processes.
However, it makes use of the shared memory in order to communicate between threads.

The Rover software, called `roverapp <https://github.com/app4mc-rover/rover-app>`_, is a C/C++ application with a single executable that makes use of its shared memory for data communication.
It is designed as a multi-threaded (POSIX threads or Pthreads) C/C++ implementation that runs on Linux-based embedded single board computers (such as Raspberry Pi) and involves many drivers, custom libraries, external libraries, and many threads (with task functions).

.. image:: ../roverstatic/images/complete_infra.png
   :width: 100%
   :align: center
   :alt: ../roverstatic/images/complete_infra.png

*************************************************
Additional Links
*************************************************

* Overview about the used hardware parts and where to order it: `Rover Hardware <https://wiki.eclipse.org/APP4MC/Rover>`_
