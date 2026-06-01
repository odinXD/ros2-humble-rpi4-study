#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class HelloSubscriber : public rclcpp::Node
{
public:
  HelloSubscriber()
  : Node("hello_subscriber")
  {
    subscription_ = create_subscription<std_msgs::msg::String>(
      "practice_chatter", 10,
      [this](const std_msgs::msg::String & message) {
        RCLCPP_INFO(get_logger(), "I heard: '%s'", message.data.c_str());
      });
  }

private:
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<HelloSubscriber>());
  rclcpp::shutdown();
  return 0;
}
