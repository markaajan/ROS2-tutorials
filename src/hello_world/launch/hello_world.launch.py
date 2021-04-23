#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
 

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    hello_world = get_package_share_directory('hello_world')
    return LaunchDescription([
        Node(
            package='hello_world',
            executable='hello_world',
            name='hello_world',
            parameters=[os.path.join(hello_world, 'hello_world.yaml')],
            output='screen',      
            emulate_tty=True),   
    ])
