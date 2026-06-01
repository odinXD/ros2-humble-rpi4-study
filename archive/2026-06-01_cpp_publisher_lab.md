# 2026-06-01 C++ Publisher 실습 일지

## 실습 환경

- Device: Raspberry Pi 4B
- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `~/ros2_ws`

## 실습 목적

`cpp_practice` package의 `hello_node`를 실제 ROS 2 publisher node로 확장한다.

`rclcpp`, `std_msgs` 의존성을 추가하고 Raspberry Pi에서 빌드, 실행, topic 발행 결과를 검증한다.

## 1. Package 의존성 추가

`package.xml`에 다음 의존성을 추가했다.

```xml
<depend>rclcpp</depend>
<depend>std_msgs</depend>
```

## 2. CMake 설정 추가

`CMakeLists.txt`에 실행 파일 의존성을 연결했다.

```cmake
add_executable(hello_node src/hello_node.cpp)
ament_target_dependencies(hello_node rclcpp std_msgs)
```

## 3. Publisher Source 작성

초기 문자열 출력 코드를 `rclcpp::Node` 기반 publisher로 변경했다.

주요 구조:

```cpp
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
};
```

## 4. 첫 빌드 실패

```bash
cd ~/ros2_ws
./scripts/build.sh
```

결과:

```text
Starting >>> cpp_practice
--- stderr: cpp_practice
CMake Error at /opt/ros/humble/share/ament_cmake_target_dependencies/cmake/ament_target_dependencies.cmake:77 (message):
  ament_target_dependencies() the passed package name 'rclcpp' was not found
  before
Call Stack (most recent call first):
  CMakeLists.txt:15 (ament_target_dependencies)

Failed   <<< cpp_practice [0.85s, exited with code 2]

Summary: 0 packages finished [2.10s]
  1 package failed: cpp_practice
  1 package had stderr output: cpp_practice
```

## 5. 오류 원인 확인

처음 작성한 `CMakeLists.txt`에서는 아래 두 줄이 `if(BUILD_TESTING)` 내부에 있었다.

```cmake
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
```

하지만 `ament_target_dependencies(hello_node rclcpp std_msgs)`는 이 블록보다 먼저 실행된다.

CMake가 실행 파일의 의존성을 연결하는 시점에 `rclcpp`, `std_msgs` package가 아직 선언되지 않아 빌드가 실패했다.

## 6. CMake 오류 해결

의존성 선언을 `ament_target_dependencies()`보다 앞쪽으로 옮겼다.

```cmake
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(hello_node src/hello_node.cpp)
ament_target_dependencies(hello_node rclcpp std_msgs)
```

## 7. 수정 후 Raspberry Pi 빌드

```bash
./scripts/build.sh
```

결과:

```text
Starting >>> cpp_practice
Finished <<< cpp_practice [24.9s]

Summary: 1 package finished [26.1s]
Build completed.
```

## 8. Publisher 실행

```bash
source install/setup.bash
ros2 run cpp_practice hello_node
```

결과 일부:

```text
[hello_publisher]: Publishing: 'Hello from cpp_practice: 0'
[hello_publisher]: Publishing: 'Hello from cpp_practice: 1'
[hello_publisher]: Publishing: 'Hello from cpp_practice: 2'
```

## 9. ROS Graph 확인

다른 터미널에서 실행 중인 node를 확인했다.

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 node list
```

결과:

```text
/hello_publisher
```

Node의 상세 정보를 확인했다.

```bash
ros2 node info /hello_publisher
```

주요 결과:

```text
/hello_publisher
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /practice_chatter: std_msgs/msg/String
    /rosout: rcl_interfaces/msg/Log
```

## 10. Topic 목록과 실제 메시지 확인

```bash
ros2 topic list -t
```

결과:

```text
/parameter_events [rcl_interfaces/msg/ParameterEvent]
/practice_chatter [std_msgs/msg/String]
/rosout [rcl_interfaces/msg/Log]
```

```bash
ros2 topic echo /practice_chatter
```

결과 일부:

```text
data: 'Hello from cpp_practice: 51'
---
data: 'Hello from cpp_practice: 52'
---
data: 'Hello from cpp_practice: 53'
---
```

## 11. Topic 상태 확인

```bash
ros2 topic info /practice_chatter
```

결과:

```text
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 0
```

`ros2 topic echo`를 종료한 뒤 조회했으므로 subscriber 수는 0이었다.

## 12. 발행 주기 확인

```bash
ros2 topic hz /practice_chatter
```

결과 일부:

```text
average rate: 1.000
        min: 1.000s max: 1.000s std dev: 0.00024s window: 16
```

## 확인한 내용

- `rclcpp::Node`를 상속하여 C++ ROS 2 node를 만들 수 있다.
- `create_publisher<std_msgs::msg::String>()`으로 문자열 topic publisher를 생성할 수 있다.
- `create_wall_timer(1s, ...)`를 사용해 약 1 Hz 주기로 메시지를 발행할 수 있다.
- `package.xml`과 `CMakeLists.txt`에 package 의존성을 모두 추가해야 한다.
- CMake의 `find_package()`는 해당 의존성을 사용하는 설정보다 먼저 실행되어야 한다.
- Raspberry Pi에서 `/hello_publisher`와 `/practice_chatter` 동작을 실제로 검증했다.

## 다음 실습

`/practice_chatter`를 구독하는 C++ subscriber node를 작성한다.
