import sys

import rclpy
from rclpy.node import Node
from study_interfaces.srv import AddThreeInts


class AddThreeIntsClient(Node):

    def __init__(self):
        super().__init__('py_add_three_ints_client')
        self.client = self.create_client(
            AddThreeInts,
            'py_add_three_ints',
        )

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Service not available, waiting again...'
            )

    def send_request(self, a, b, c):
        request = AddThreeInts.Request()
        request.a = a
        request.b = b
        request.c = c
        return self.client.call_async(request)


def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) != 4:
        print('Usage: three_ints_client X Y Z')
        return

    node = AddThreeIntsClient()
    future = node.send_request(
        int(sys.argv[1]),
        int(sys.argv[2]),
        int(sys.argv[3]),
    )
    rclpy.spin_until_future_complete(node, future)

    response = future.result()
    node.get_logger().info(f'Sum: {response.sum}')

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()