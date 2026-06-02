import rclpy
from rclpy.node import Node
from study_interfaces.srv import AddThreeInts


class AddThreeIntsServer(Node):

    def __init__(self):
        super().__init__('py_add_three_ints_server')
        self.service = self.create_service(
            AddThreeInts,
            'py_add_three_ints',
            self.add_callback,
        )
        self.get_logger().info('Ready to add three ints.')

    def add_callback(self, request, response):
        response.sum = request.a + request.b + request.c
        self.get_logger().info(
            f'Request: {request.a} + {request.b} + '
            f'{request.c} = {response.sum}'
        )
        return response


def main(args=None):
    rclpy.init(args=args)
    node = AddThreeIntsServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()