Docker makes an environment that everyone in the team can easily access to code. 
> I familiarized myself with using Docker container of a ros:foxy image in an easily accessed and monitored Linux environment with ROS2 Foxy distro setup to run my Autonomous RC.

Providing Docker is successfully installed.
> Bash
> docker run -it -v <path_to_repo>/Docker-Talkers/src/:/Docker-Talkers/src/ --name f1tenth_lab1 ros:foxy 					#to set up ros:foxy environment in the repo path
> docker start f1tenth_lab1           	#if previously turned off
> docker exec -it f1tenth /bin/bash
> source /opt/ros/foxy/setup.bash
> cd <workspace>/src
> ros2 pkg create –build-type ament_python lab1_pkg3  	#form a exec package in workspace
 
This folder contains 2 Exec nodes: Talker and Relay. Both subscribe to the “ROS2_Drive” topic. Talker node published incrementals of speed “v” and steering angle “d” sim on timing callback.
Relay node publishes “v” and “d” data x3 on subscriber callback. 
- Dependencies and required configuration were adjusted inside the .xml and .cfg file

```Bash
cd Docker-Talkers
colcon build
source install/setup.bash
rosdep install -i –from-path src –rosdistro foxy -y		 # install dependencies
ros2 launch lab1_pkg3 lab1_launch.py
 
```

By running the launch file, I can open another cmd and observe the nodes change inside a topic.

```Bash
ros2 topic echo ROS2_Drive
```
