# Project : WheelchairDAS

# **Driver Assistance System for Wheelchair**
Student Project in 2022 for UG BME Course

## Target
Develop an accurate & effective system while maintaining the cost

## System Overview

![System Overview](https://github.com/Sparkl315/WheelchairDAS/blob/aabb8b16f527155dbd48046f216356d7342fad94/documents/diagrams/wheelchairDAS_overview.png)

### Main Control Unit
 - **Raspberry Pi 4B**
 - Raspberry Pi OS & Robot Operating System (ROS (Noetic))
### Rear & Side Obstacle Detection
 - 6 Ultrasound (HC-SR04) for Side Obstable Detection
 - Stereo Camera for Rear Obstacle Detection
### Auto Input Tuning
 - Arduino connected to Joystick input for interception and Manipulation
 - Able to be turned On or Off with preference
### Graphical User Interface
 - Indicators for obstacle direction & distances
 - Rear Camera View Display

## Technical Details
### Rear & Side Obstacle Detection
**Side Obstacle Detection**

![Block Diagram](https://github.com/Sparkl315/WheelchairDAS/blob/e81ffbe4f7ba9f9f652deeda80ca54335e76def7/documents/diagrams/Obstacle_Detection/Block%20diagram%20arduino%20ultrasound.jpeg)

![Ulrasound Placement](https://github.com/Sparkl315/WheelchairDAS/blob/e81ffbe4f7ba9f9f652deeda80ca54335e76def7/documents/diagrams/Obstacle_Detection/Side_obstacle_detection_placement.jpeg)

![Flowchart](https://github.com/Sparkl315/WheelchairDAS/blob/aabb8b16f527155dbd48046f216356d7342fad94/documents/diagrams/Obstacle_Detection/ultrasound%20detection%20flowchart.png)

**Rear Obstacle Detection**

![Diagram](https://github.com/Sparkl315/WheelchairDAS/blob/bd0619c304849e602a6e2abe0e35d30344739d1e/documents/diagrams/Obstacle_Detection/rear_camera.png)

 - Image View from rear USB camera
 - Depth Sensing using OpenCV

### Auto Input Tuning

![Flowchart](https://github.com/Sparkl315/WheelchairDAS/blob/aabb8b16f527155dbd48046f216356d7342fad94/documents/diagrams/Auto_Input_Tuning/Auto_input_tuning_flowchart.png)

![Circuit Schematic](https://github.com/Sparkl315/WheelchairDAS/blob/aabb8b16f527155dbd48046f216356d7342fad94/documents/schematics/auto_input_tuning_schematic.png)

> **EXPLANATION**
> - Joystick Input (MLX90333)
>   - DC Voltage Output Range 0~5V
>   - Output Channel A : Vertical Direction
>   - Output Channel B : Horizontal Direction
>   - Output 2.5V when idle
> - Arduino Manipulation
>   - Receive Joystick Voltage from Channel A and B (Input become 0~1024 after going through ADC in Analog Input Pins)
>   - Reading from ROS topic of Rear Obstacles
>   - If obstacle are too close, prevent the wheelchair from moving toward that direction by a limiter
>   - PWM Output using Digital pins supporting PWM (0~255)
> - Simulate DC Voltage Output
>   - Convert the duty cycle of Arduino PWM output to DC voltage with RC circuit
> - Pass the manipulated Voltage Signal back to Channel A and Channel B

### Graphical User Interface

![User Interface](https://github.com/Sparkl315/WheelchairDAS/blob/cb31a7e01472bf893220d19c017c465a6ef83dc1/documents/diagrams/WheelchairUI/user_interface.png)

![Flowchart](https://github.com/Sparkl315/WheelchairDAS/blob/aabb8b16f527155dbd48046f216356d7342fad94/documents/diagrams/WheelchairUI/wheelchair_ui_flowchart.png)
