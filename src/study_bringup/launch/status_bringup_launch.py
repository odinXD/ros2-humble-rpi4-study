from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_practice',
            executable='status_publisher',
            output='screen',
        ),
        Node(
            package='py_practice',
            executable='status_subscriber',
            output='screen',
        ),
    ])