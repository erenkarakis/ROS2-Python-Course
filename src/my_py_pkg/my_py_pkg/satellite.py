#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class SatelliteNode(Node):

    def __init__(self):
        super().__init__("satellite")

        self.subscriber_ = self.create_subscription(String, "state_publisher", self.callback_satellite, 10)

        self.get_logger().info("Satellite has been started.")

    def callback_satellite(self, msg):
        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = SatelliteNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()