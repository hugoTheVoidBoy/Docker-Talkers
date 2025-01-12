from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    launch = LaunchDescription()

    talker_node = Node(
        package = "lab1_pkg3",
        executable = "talker",
        parameters=[                   # List of parameters to set
            {"speed": 1.0},            # Example parameter: set speed
            {"steering_angle": 0.5}    # Example parameter: set steering angle
        ]
    )

    relay_node = Node(
        package = "lab1_pkg3",
        executable = "relay"
    )

    launch.add_action(talker_node)
    launch.add_action(relay_node)

    return launch