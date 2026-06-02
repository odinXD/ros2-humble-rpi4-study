import rclpy
from rclpy.node import Node
from study_interfaces.msg import StudyStatus


class StudyStatusPublisher(Node):

    def __init__(self):
        super().__init__('study_status_publisher')
        self.publisher_ = self.create_publisher(StudyStatus, 'study_status', 10)
        self.progress = 0
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        message = StudyStatus()
        message.learner = 'doyeong'
        message.topic = 'custom_interfaces'
        message.progress = self.progress
        message.completed = self.progress >= 100

        self.publisher_.publish(message)
        self.get_logger().info(
            f'Publishing: learner={message.learner}, '
            f'topic={message.topic}, '
            f'progress={message.progress}, '
            f'completed={message.completed}'
        )

        if self.progress < 100:
            self.progress += 20


def main(args=None):
    rclpy.init(args=args)
    node = StudyStatusPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()