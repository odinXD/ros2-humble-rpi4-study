import sys

import rclpy
from example_interfaces.srv import AddTwoInts
from rclpy.node import Node


class AddTwoIntsClient(Node):

    def __init__(self):
        super().__init__('py_add_two_ints_client')
        self.client = self.create_client(AddTwoInts, 'py_add_two_ints')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')

    def send_request(self, a, b):
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        return self.client.call_async(request)


def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) != 3:
        print('Usage: client X Y')
        return

    node = AddTwoIntsClient()
    future = node.send_request(int(sys.argv[1]), int(sys.argv[2]))
    rclpy.spin_until_future_complete(node, future)

    response = future.result()
    node.get_logger().info(f'Sum: {response.sum}')

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
