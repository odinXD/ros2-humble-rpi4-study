#include <chrono>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

class HelloPublisher : public rclcpp::Node
{
public:
  HelloPublisher()
  : Node("hello_publisher"), count_(0)
  {
    publisher_ = create_publisher<std_msgs::msg::String>("practice_chatter", 10);
    timer_ = create_wall_timer(1s, [this]() {
      auto message = std_msgs::msg::String();
      message.data = "Hello from cpp_practice: " + std::to_string(count_++);
      RCLCPP_INFO(get_logger(), "Publishing: '%s'", message.data.c_str());
      publisher_->publish(message);
    });
  }

private:
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
  size_t count_;
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<HelloPublisher>());
  rclcpp::shutdown();
  return 0;
}