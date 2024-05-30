# Control_myCobot_6DOF_Robot_Arm
This project presents the keyboard buttons control of a 6-degree-of-freedom MYCobot robotic arm, showcasing its advanced intelligent route planning capabilities. The project aim involves showcasing the arm’s autonomous control through specific poses triggered by dedicated keyboard buttons. Operationalizing these commands, the robotic arm seamlessly executes movements, autonomously navigating to reach the predetermined poses. Each button corresponds to a unique pose, prompting immediate movement upon activation. Furthermore, leveraging RVIZ2 facilitates the integration of the myCobot GUI interface, streamlining the configuration of individual poses programmed through these buttons.


# Components needed 
1. MyCobot robotic arm
2. Desktop computer, Keyboard, HDMI cable.

# Specifications of Mycobot Robot Arm
6 DOF  <br>
280 Working Radius（mm）<br>
250 Payload（g）<br>
860 Weight（g）<br>
± 0.5 Positioning Accuracy（mm）<br>
500 Working Lifespan（h）	<br>
12V5A Power Input	DC <br>
USB	USB 3.0*2USB 2.0*2<br>
Main control type	Raspberry pi<br>
Master control CPU	Broadcom BCM2711，64Bit 1.5GHz four-core<br>
Master control GPU	500 MHz VideoCore VI<br>
Master control Memory	2GB<br>

# Installation and Setup
The myCobot is connected to the power supply which turns on the robot arm. HDMI, Mouse, and keyboard cables connect to the robot arm which enables the robot setup process to be seamless. A built-in Ubuntu 18.04 Mate Linux imager is installed into the robot raspberry pi which serves as the desktop operating system for the myCobot 280pi robot arm. Setup, updates and all ROS2 packages installation is perform. The installing time for setting up the robot is approximately 8 hours long.

**Installing git**
1. sudo apt install git
   **confirming the git version installed**
2. git --version
   **use for installing pip**
3. sudo apt install python-pip

**Next, create the workspace and install the myCobot package**<br>
**Created a folder**<br>
mkdir -p ˜/colcon_ws/src<br>
**Enter the folder**
cd ˜/colcon_ws/src<br>
**use git clone, to get the myCobot**
package which will be edit to the code implemented in this project<br>
git clone https://github.com/elephantrobotics/mycobot_ros2.git<br>
**move back to workspace**<br>
cd ..<br>
**Build the project workspace**<br>
colcon build --symlink-install<br>

**source the project work environment**<br>
source install/setup.bash<br>

**Install the pymcobot**
pip install pymycobot <br>


# Extract each Joint Angles 
Following the preliminary stage, prior to programming the launch file for interfacing with the robot, a graphical user interface (GUI) for getting the robot arm joints angles is employed. This GUI facilitates the extraction of essential joint angles crucial for implementing intelligent route planning within the robot arm system. Activation of the myCobot joint GUI involves utilizing a ROS2 terminal and a specific snippet code embedded within a launch file. Through this interface, three distinct poses, namely the home, pick, and place poses, are meticulously configured, contributing to the comprehensive setup of the robotic arm’s operational parameters.

The initial pose corresponds to the robot’s home position, where all joint angles are uniformly set to zero. In this configuration, the robot arm’s links align vertically, forming the pose (0,0,0,0,0,0). Following this, the pick pose is established, characterized by joint angles (0, 30, 60, 80, 0, 45). Lastly, the place pose is defined, featuring joint angles (0,-45, -45, 60, 0, 45).
**Command line use to launch GUI**
ros2 run mycobot_280pisimple_gui.launch.py



