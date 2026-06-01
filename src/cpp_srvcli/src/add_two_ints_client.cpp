#include <chrono>
#include <cstdlib>
#include <memory>

#include "example_interfaces/srv/add_two_ints.hpp"
#include "rclcpp/rclcpp.hpp"

using namespace std::chrono_literals;

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);

  if (argc != 3) {
    RCLCPP_INFO(rclcpp::get_logger("cpp_add_two_ints_client"), "Usage: client X Y");
    return 1;
  }

  auto node = rclcpp::Node::make_shared("cpp_add_two_ints_client");
  auto client =
    node->create_client<example_interfaces::srv::AddTwoInts>("cpp_add_two_ints");

  auto request =
    std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
  request->a = std::atoll(argv[1]);
  request->b = std::atoll(argv[2]);

  while (!client->wait_for_service(1s)) {
    if (!rclcpp::ok()) {
      RCLCPP_ERROR(node->get_logger(), "Interrupted while waiting for the service.");
      return 0;
    }
    RCLCPP_INFO(node->get_logger(), "Service not available, waiting again...");
  }

  auto result = client->async_send_request(request);

  if (rclcpp::spin_until_future_complete(node, result) ==
    rclcpp::FutureReturnCode::SUCCESS)
  {
    RCLCPP_INFO(node->get_logger(), "Sum: %ld", result.get()->sum);
  } else {
    RCLCPP_ERROR(node->get_logger(), "Failed to call service.");
  }

  rclcpp::shutdown();
  return 0;
}