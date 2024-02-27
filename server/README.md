# Smart Traffic Light System

## Project Overview

This document outlines the conceptual design of a smart traffic light system using Raspberry Pi and 4 USB cameras. The system aims to improve traffic flow by dynamically adjusting traffic light timings based on real-time traffic density estimation. It is intended for educational and research purposes only.

### Disclaimer

Deploying a traffic light control system in a real-world environment requires thorough testing, safety measures, and approval from relevant authorities. The provided code example lacks detailed hardware interaction or communication protocols, as these aspects are specific to the chosen traffic light controller.

## Components

### Hardware

- Raspberry Pi units
- USB Cameras (wide-angle recommended)
- Micro SD cards for each Raspberry Pi
- Power supplies for each Raspberry Pi and camera
- Enclosure for each Raspberry Pi (optional)
- Traffic light controller with a compatible communication method (e.g., serial, GPIO)

### Software

- Operating System for Raspberry Pi (e.g., Raspbian)
- Python
- OpenCV library for image processing
- FastAPI for the web API
- ElephantSQL for the database
- Cloud storage and management platform (optional)

## Conceptual Design

### 1. System Architecture

The system comprises four Raspberry Pi units, each connected to a USB camera. The key components and functionalities include:

- Each Raspberry Pi processes video frames from its respective camera.
- OpenCV is used to detect and count vehicles in the frames.
- Traffic density is estimated based on the vehicle count (placeholder function, needs actual implementation).
- Each Raspberry Pi sends congestion data, including lane ID, congestion level, and vehicle count, to a central server or cloud platform (optional).
- The central server/cloud platform combines data from multiple sources, implements logic for dynamically adjusting traffic light timings, and provides APIs for real-time traffic data and visualizations (optional).

### 2. Software Development

#### Raspberry Pi Applications

Develop software on each Raspberry Pi to:

- Capture video frames from the connected camera.
- Utilize OpenCV for vehicle detection and counting.
- Implement a placeholder function to estimate traffic density.
- Send traffic data to a central server or cloud platform (optional).

#### Central Server (Raspberry Pi) with ElephantSQL

- Set up ElephantSQL for the database on the Raspberry Pi.
- Store traffic data in the database for historical analysis.

#### Cloud Platform with FastAPI

- Implement FastAPI on a cloud server for the web application.
- Receive traffic data from the Raspberry Pi units.
- Process the data, potentially combining it from multiple lanes or intersections.
- Implement logic for dynamically adjusting traffic light timings based on the combined data (placeholder function, needs actual implementation and connection to the traffic light controller).
- Provide an API to retrieve real-time traffic data and visualizations (optional).

### 3. Deployment

- Install the Raspberry Pi operating system on each Micro SD card and set up the necessary software.
- Connect the cameras to the Raspberry Pis, mount them in weatherproof enclosures (optional), and establish connections to the traffic light controllers using appropriate communication methods.
- Deploy the central server with ElephantSQL on a Raspberry Pi.
- Deploy the FastAPI server on a cloud platform.
