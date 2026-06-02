import rclpy
from rclpy.node import Node
from study_interfaces.msg import StudyStatus


class StudyStatusSubscriber(Node):

    def __init__(self):
        super().__init__('study_status_subscriber')
        self.subscription = self.create_subscription(
            StudyStatus,
            'study_status',
            self.listener_callback,
            10,
        )

    def listener_callback(self, message):
        self.get_logger().info(
            f'I heard: learner={message.learner}, '
            f'topic={message.topic}, '
            f'progress={message.progress}, '
            f'completed={message.completed}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = StudyStatusSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()