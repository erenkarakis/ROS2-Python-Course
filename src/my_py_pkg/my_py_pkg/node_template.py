#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class TemplateNode(Node): # TODO: Rename

    def __init__(self):
        super().__init__("template_node") # TODO: Rename


def main(args=None):
    rclpy.init(args=args)
    node = TemplateNode() # TODO: Rename
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()