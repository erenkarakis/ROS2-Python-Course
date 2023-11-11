#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from my_custom_interfaces.msg import DeviceStatus

class DeviceStatusPublisherNode(Node):

    def __init__(self):
        super().__init__("device_status_publisher")

        self.status_publisher_ = self.create_publisher(DeviceStatus, "device_status", 10)
        self.timer_ = self.create_timer(1.0, self.publish_device_status)
        self.get_logger().info("Device status publiher has been started.")

    def publish_device_status(self):
        msg = DeviceStatus()
        msg.motor_speed = 75
        msg.is_sensor_on = True
        msg.status_message = "All systems active"
        self.status_publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = DeviceStatusPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()