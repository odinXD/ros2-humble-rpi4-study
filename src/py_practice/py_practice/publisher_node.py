import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloPublisher(Node):

    def __init__(self):
        super().__init__('py_hello_publisher')
        self.publisher_ = self.create_publisher(String, 'py_practice_chatter', 10)
        self.count = 0
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        message = String()
        message.data = f'Hello from py_practice: {self.count}'
        self.get_logger().info(f"Publishing: '{message.data}'")
        self.publisher_.publish(message)
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = HelloPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()