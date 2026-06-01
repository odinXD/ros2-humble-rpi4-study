# 08. C++ Subscriber Node 작성

## 학습 목표

`cpp_practice` package에 C++ subscriber node를 추가한다.

Raspberry Pi 4B에서 publisher와 subscriber를 함께 실행하고, `/practice_chatter` topic의 메시지가 실제로 전달되는지 확인한다.

## 핵심 개념

Subscriber는 topic을 구독하고 새 메시지가 도착했을 때 callback을 실행한다.

이번 실습에서는 `/hello_subscriber` node가 `/practice_chatter` topic을 구독하고 문자열 메시지를 로그로 출력하도록 구현했다.

- Publisher Node: `/hello_publisher`
- Subscriber Node: `/hello_subscriber`
- Topic: `/practice_chatter`
- Message Type: `std_msgs/msg/String`

## 변경한 파일

### `src/listener_node.cpp`

`HelloSubscriber` 클래스를 만들고 문자열 메시지를 구독했다.

```cpp
subscription_ = create_subscription<std_msgs::msg::String>(
  "practice_chatter", 10,
  [this](const std_msgs::msg::String & message) {
    RCLCPP_INFO(get_logger(), "I heard: '%s'", message.data.c_str());
  });
```

### `CMakeLists.txt`

`listener_node` 실행 파일을 빌드하고 설치하도록 설정했다.

```cmake
add_executable(listener_node src/listener_node.cpp)
ament_target_dependencies(listener_node rclcpp std_msgs)

install(TARGETS
  hello_node
  listener_node
  DESTINATION lib/${PROJECT_NAME})
```

## 사용한 명령어

### Raspberry Pi에서 빌드

```bash
cd ~/ros2_ws
./scripts/build.sh
```

### Publisher 실행

```bash
source ~/ros2_ws/install/setup.bash
ros2 run cpp_practice hello_node
```

### Subscriber 실행

```bash
source ~/ros2_ws/install/setup.bash
ros2 run cpp_practice listener_node
```

### ROS graph 확인

```bash
source ~/ros2_ws/install/setup.bash
ros2 node list
ros2 node info /hello_subscriber
ros2 topic info /practice_chatter
```

## 실행 결과 요약

Raspberry Pi에서 package 빌드가 성공했다.

```text
Starting >>> cpp_practice
Finished <<< cpp_practice [0.61s]

Summary: 1 package finished [1.83s]
Build completed.
```

Subscriber는 publisher의 메시지를 연속으로 수신했다.

```text
[hello_subscriber]: I heard: 'Hello from cpp_practice: 23'
[hello_subscriber]: I heard: 'Hello from cpp_practice: 24'
[hello_subscriber]: I heard: 'Hello from cpp_practice: 25'
```

ROS graph에서 두 node를 확인했다.

```text
/hello_publisher
/hello_subscriber
```

`/hello_subscriber`가 `/practice_chatter`를 구독하는 것도 확인했다.

```text
Subscribers:
  /practice_chatter: std_msgs/msg/String
```

Topic 연결 상태:

```text
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 1
```

## 에러 및 해결

이번 실습에서는 별도의 에러가 발생하지 않았다.

## 정리

Publisher와 subscriber는 서로 직접 연결되는 것이 아니라 topic을 통해 메시지를 주고받는다.

이번 실습에서는 직접 작성한 C++ publisher와 subscriber를 Raspberry Pi에서 실행하고 `/practice_chatter` topic의 문자열 메시지가 정상 전달되는 것을 확인했다.

## 발표/설명용 요약

이번 실습에서는 C++ ROS 2 subscriber node를 작성했다. Raspberry Pi에서 `/hello_publisher`와 `/hello_subscriber`를 실행하고 `/practice_chatter` topic의 문자열 메시지가 전달되는 것을 확인했다. 이를 통해 직접 작성한 C++ node 사이의 pub-sub 통신 흐름을 검증했다.
