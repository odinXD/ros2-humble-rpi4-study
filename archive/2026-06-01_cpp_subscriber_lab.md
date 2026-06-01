# 2026-06-01 C++ Subscriber 실습 일지

## 실습 환경

- Device: Raspberry Pi 4B
- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `~/ros2_ws`

## 실습 목적

`cpp_practice` package에 `/practice_chatter` topic을 구독하는 C++ subscriber를 추가한다.

Raspberry Pi에서 publisher와 subscriber를 함께 실행하고 메시지 전달 상태를 확인한다.

## 1. Subscriber Source 추가

`src/cpp_practice/src/listener_node.cpp`를 작성했다.

주요 구조:

```cpp
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
};
```

## 2. CMake 설정 추가

`CMakeLists.txt`에 `listener_node` 빌드와 설치 설정을 추가했다.

```cmake
add_executable(listener_node src/listener_node.cpp)
ament_target_dependencies(listener_node rclcpp std_msgs)

install(TARGETS
  hello_node
  listener_node
  DESTINATION lib/${PROJECT_NAME})
```

## 3. Raspberry Pi에서 빌드

```bash
cd ~/ros2_ws
./scripts/build.sh
```

결과:

```text
Starting >>> cpp_practice
Finished <<< cpp_practice [0.61s]

Summary: 1 package finished [1.83s]
Build completed.
```

## 4. Publisher 실행

첫 번째 터미널:

```bash
source ~/ros2_ws/install/setup.bash
ros2 run cpp_practice hello_node
```

결과 일부:

```text
[hello_publisher]: Publishing: 'Hello from cpp_practice: 21'
[hello_publisher]: Publishing: 'Hello from cpp_practice: 22'
[hello_publisher]: Publishing: 'Hello from cpp_practice: 23'
```

## 5. Subscriber 실행

두 번째 터미널:

```bash
source ~/ros2_ws/install/setup.bash
ros2 run cpp_practice listener_node
```

결과 일부:

```text
[hello_subscriber]: I heard: 'Hello from cpp_practice: 23'
[hello_subscriber]: I heard: 'Hello from cpp_practice: 24'
[hello_subscriber]: I heard: 'Hello from cpp_practice: 25'
```

Subscriber를 나중에 실행했기 때문에 현재 흐르는 메시지부터 수신했다.

## 6. Node 목록 확인

세 번째 터미널:

```bash
source ~/ros2_ws/install/setup.bash
ros2 node list
```

결과:

```text
/hello_publisher
/hello_subscriber
```

## 7. Subscriber 정보 확인

```bash
ros2 node info /hello_subscriber
```

주요 결과:

```text
/hello_subscriber
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /practice_chatter: std_msgs/msg/String
```

## 8. Topic 연결 상태 확인

```bash
ros2 topic info /practice_chatter
```

결과:

```text
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 1
```

## 9. Git 동기화

Pi에서 source 변경을 확인했다.

```bash
git status --short
```

결과:

```text
 M src/cpp_practice/CMakeLists.txt
?? src/cpp_practice/src/listener_node.cpp
```

빌드와 실행 검증 후 source를 commit, push했다.

```text
20fc61f feat: add C++ subscriber node
```

Windows 저장소에서도 pull 후 fast-forward 동기화를 확인했다.

## 확인한 내용

- `create_subscription()`으로 C++ subscriber를 만들 수 있다.
- 새 메시지가 들어오면 callback이 실행된다.
- Publisher와 subscriber는 `/practice_chatter` topic을 통해 연결된다.
- Subscriber를 나중에 시작하면 실행 이후에 흐르는 메시지부터 수신한다.
- Raspberry Pi에서 직접 작성한 C++ node 사이의 통신을 검증했다.

## 다음 실습

`ament_python` 기반 Python package를 만들고 publisher와 subscriber를 작성한다.
