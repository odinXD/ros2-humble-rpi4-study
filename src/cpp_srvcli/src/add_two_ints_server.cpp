#include <memory>

#include "example_interfaces/srv/add_two_ints.hpp"
#include "rclcpp/rclcpp.hpp"

void add(
  const std::shared_ptr<example_interfaces::srv::AddTwoInts::Request> request,
  std::shared_ptr<example_interfaces::srv::AddTwoInts::Response> response)
{
  response->sum = request->a + request->b;

  RCLCPP_INFO(
    rclcpp::get_logger("cpp_add_two_ints_server"),
    "Request: %ld + %ld = %ld",
    request->a, request->b, response->sum);
}

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);

  auto node = rclcpp::Node::make_shared("cpp_add_two_ints_server");

  auto service = node->create_service<example_interfaces::srv::AddTwoInts>(
    "cpp_add_two_ints", &add);

  RCLCPP_INFO(node->get_logger(), "Ready to add two ints.");

  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
