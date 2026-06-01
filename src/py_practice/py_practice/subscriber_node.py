import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloSubscriber(Node):

    def __init__(self):
        super().__init__('py_hello_subscriber')
        self.subscription = self.create_subscription(
            String,
            'py_practice_chatter',
            self.listener_callback,
            10,
        )

    def listener_callback(self, message):
        self.get_logger().info(f"I heard: '{message.data}'")


def main(args=None):
    rclpy.init(args=args)
    node = HelloSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
