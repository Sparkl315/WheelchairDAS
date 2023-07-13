# WheelchairDAS

# **Driver Assistance System for Wheelchair**
## Target
Develop an accurate & effective system while maintaining the cost

## System Overview
### Main Control Unit
 - **Raspberry Pi 4B**
 - Raspberry Pi OS & Robot Operating System (ROS (Noetic))
### Rear & Side Obstacle Detection
 - 6 Ultrasound (HC-SR04) for Side Obstable Detection
 - Stereo Camera with Depth Sensing for Rear Obstacle Detection
### Auto Input Tuning
 - Arduino connected to Joystick input for interception and Manipulation
 - Able to be turned On or Off with preference
### Graphical Interface
 - Indicators for obstacle direction & distances
 - Rear Camera View Display

## Technical Details
### Rear & Side Obstacle Detection
**Side Obstacle Detection**
 - (Block Diagram for Ultrasound and RPi Connection) !
 - (Ultrasound Placement Diagram) !
 - Serial Communication via USB port for Data acquisition
 - Data is stored using a topic system in ROS
 - ...

**Rear Obstacle Detection**
 - Image View from rear USB camera
 - Depth Sensing using OpenCV
 - (Diagrams : image RGB view, image Grey view, Dispersity Analysis & Mapping, Depth View, Flowchart of the system) !
 - ...

### Auto Input Tuning
 - (Flowchart for Connection of Joystick, Arduino, Motor Control Unit) !
 - (Circuit Schematic for Joystick and Arduino w/ RC circuit) !
> **EXPLAINATION** (FOR REFERENCE)
> - Joystick Input (MAX-forgot chip number)
>   - DC Voltage Output Range 0~5V
>   - Output Channel A : Horizontal Direction  (Not sure pls check)
>   - Output Channel B : Vertical Direction  (Not sure pls check)
>   - Output 2.5V when idle
> - Arduino Manipulation
>   - Receive Joystick Voltage from Channel A and B (Input become 0~1024 after going through ADC in Analog Input Pins)
>   - Reading from ROS topic of Rear Obstacles
>   - If obstacle are too close, prevent the wheelchair from moving toward that direction by a limiter
>   - PWM Output using Digital pins supporting PWM (0~255)
> - Simulate DC Voltage Output
>   - Convert the duty cycle of Arduino PWM output to DC voltage with RC circuit
>   - (RC circuit Schematic) !
> - Pass the manipulated Voltage Signal back to Channel A and Channel B
     
### Graphical Interface
 - (Screen Capture of the UI with proper description) !
 - Indicators are based on Side & Rear Obstacle Detection

## Result & Discussion
### Limitation on Current Situation
 - The Wheelchair have slight delay on Joystick Input before adding any modification
 - The Wheelchair Battery is unreliable and old

  &rarr; **Safety Risk** 

...

## Further Development
...

