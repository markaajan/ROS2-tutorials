#!/usr/bin/env python3

import rclpy
from time import sleep


def main():
    rclpy.init()
    counter = 0
    hello_world = rclpy.create_node('hello_world')
    hello_world.declare_parameter('Text',"Hello ROS2 World")
    hello_world.declare_parameter('Freq',60)
    
    while rclpy.ok():
        try:
            rclpy.spin_once(hello_world, timeout_sec=1.0)
        except KeyboardInterrupt:
            pass
        counter = counter + 1
        print(hello_world.get_parameter('Text').value)
        print ("Counter =" + str(counter))
        frequency = 60 / hello_world.get_parameter('Freq').value
        sleep(frequency)

    hello_world.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
