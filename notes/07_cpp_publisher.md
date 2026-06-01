# 07. C++ Publisher Node 작성

## 학습 목표

`cpp_practice` package의 초기 C++ 실행 파일을 실제 ROS 2 publisher node로 확장한다.

Raspberry Pi 4B에서 빌드한 뒤 node, topic, 메시지 타입, 발행 주기를 CLI로 검증한다.

## 핵심 개념

`rclcpp::Node`를 상속하면 C++ 코드로 ROS 2 node를 만들 수 있다.

이번 실습에서는 `/hello_publisher` node가 1초마다 `/practice_chatter` topic에 문자열 메시지를 발행하도록 구현했다.

- Node: `/hello_publisher`
- Topic: `/practice_chatter`
- Message Type: `std_msgs/msg/String`
- Publish Rate: 약 `1 Hz`

## 변경한 파일

### `package.xml`

ROS 2 C++ client library와 문자열 메시지 타입의 의존성을 추가했다.

```xml
<depend>rclcpp</depend>
<depend>std_msgs</depend>
```

### `CMakeLists.txt`

빌드에 필요한 package를 찾고 `hello_node` 실행 파일에 연결했다.

```cmake
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

ament_target_dependencies(hello_node rclcpp std_msgs)
```

### `src/hello_node.cpp`

`HelloPublisher` 클래스를 만들고 1초 주기의 timer callback에서 메시지를 발행하도록 변경했다.

```cpp
publisher_ = create_publisher<std_msgs::msg::String>("practice_chatter", 10);
timer_ = create_wall_timer(1s, [this]() {
  auto message = std_msgs::msg::String();
  message.data = "Hello from cpp_practice: " + std::to_string(count_++);
  RCLCPP_INFO(get_logger(), "Publishing: '%s'", message.data.c_str());
  publisher_->publish(message);
});
```

## 사용한 명령어

### Raspberry Pi에서 빌드와 실행

```bash
cd ~/ros2_ws
./scripts/build.sh
source install/setup.bash
ros2 run cpp_practice hello_node
```

### ROS graph와 Topic 확인

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 node list
ros2 node info /hello_publisher
ros2 topic list -t
ros2 topic echo /practice_chatter
ros2 topic info /practice_chatter
ros2 topic hz /practice_chatter
```

## 실행 결과 요약

Raspberry Pi에서 package 빌드가 성공했다.

```text
Starting >>> cpp_practice
Finished <<< cpp_practice [24.9s]

Summary: 1 package finished [26.1s]
Build completed.
```

Publisher node는 1초마다 메시지를 발행했다.

```text
[hello_publisher]: Publishing: 'Hello from cpp_practice: 0'
[hello_publisher]: Publishing: 'Hello from cpp_practice: 1'
[hello_publisher]: Publishing: 'Hello from cpp_practice: 2'
```

ROS graph에서 `/hello_publisher` node를 확인했다.

```text
/hello_publisher
```

`/hello_publisher`가 `/practice_chatter`를 publish하는 것도 확인했다.

```text
Publishers:
  /practice_chatter: std_msgs/msg/String
```

실제 topic 메시지:

```text
data: 'Hello from cpp_practice: 51'
---
data: 'Hello from cpp_practice: 52'
---
```

Topic 상태:

```text
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 0
```

발행 주기:

```text
average rate: 1.000
```

## 에러 및 해결

### `ament_target_dependencies()`에서 `rclcpp`를 찾지 못함

처음에는 다음 오류로 빌드가 실패했다.

```text
ament_target_dependencies() the passed package name 'rclcpp' was not found before
```

원인은 `find_package(rclcpp REQUIRED)`와 `find_package(std_msgs REQUIRED)`를 `if(BUILD_TESTING)` 내부에 추가한 것이었다.

`ament_target_dependencies(hello_node rclcpp std_msgs)`가 실행되기 전에 package를 찾아야 하므로 두 줄을 상단 의존성 선언 위치로 옮겼다.

```cmake
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(hello_node src/hello_node.cpp)
ament_target_dependencies(hello_node rclcpp std_msgs)
```

수정 후 Raspberry Pi 빌드에 성공했다.

## 정리

초기 `hello_node`는 문자열을 출력하고 종료하는 일반 C++ 실행 파일이었다.

이번 실습에서 `rclcpp` 기반 node로 확장하고, timer callback을 사용해 `/practice_chatter` topic에 문자열을 약 1 Hz로 발행했다.

## 발표/설명용 요약

이번 실습에서는 첫 C++ ROS 2 publisher node를 작성했다. Raspberry Pi에서 `/hello_publisher`를 실행하고 `/practice_chatter` topic에 문자열 메시지가 약 1 Hz로 발행되는 것을 확인했다. 빌드 과정에서 CMake 의존성 선언 위치 오류도 해결하며 package 설정과 source code의 연결 방식을 익혔다.
