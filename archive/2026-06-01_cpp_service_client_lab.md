# 2026-06-01 C++ Service와 Client 실습 일지

## 실습 환경

- Device: Raspberry Pi 4B
- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `~/ros2_ws`

## 실습 목적

`ament_cmake` 기반 `cpp_srvcli` package를 만들고 `AddTwoInts` 타입의 service server와 client를 작성한다.

Raspberry Pi에서 CLI 요청과 C++ client 요청을 각각 실행한다.

## 1. Package 생성

```bash
cd ~/ros2_ws/src
ros2 pkg create \
  --build-type ament_cmake \
  --license Apache-2.0 \
  cpp_srvcli \
  --dependencies rclcpp example_interfaces
```

주요 결과:

```text
package name: cpp_srvcli
destination directory: /home/doyeong/ros2_ws/src
package format: 3
build type: ament_cmake
dependencies: ['rclcpp', 'example_interfaces']
```

## 2. Server Source 작성

`src/cpp_srvcli/src/add_two_ints_server.cpp`를 작성했다.

```cpp
void add(
  const std::shared_ptr<example_interfaces::srv::AddTwoInts::Request> request,
  std::shared_ptr<example_interfaces::srv::AddTwoInts::Response> response)
{
  response->sum = request->a + request->b;
}
```

## 3. Server 빌드와 실행

```bash
cd ~/ros2_ws
./scripts/build.sh
source install/setup.bash
ros2 run cpp_srvcli server
```

결과:

```text
Summary: 3 packages finished [24.2s]
Build completed.

[cpp_add_two_ints_server]: Ready to add two ints.
```

## 4. CLI에서 Service 확인

```bash
source ~/ros2_ws/install/setup.bash
ros2 service list -t
ros2 service type /cpp_add_two_ints
```

주요 결과:

```text
/cpp_add_two_ints [example_interfaces/srv/AddTwoInts]
example_interfaces/srv/AddTwoInts
```

## 5. CLI에서 Service 호출

```bash
ros2 service call /cpp_add_two_ints example_interfaces/srv/AddTwoInts "{a: 10, b: 20}"
```

결과:

```text
requester: making request: example_interfaces.srv.AddTwoInts_Request(a=10, b=20)

response:
example_interfaces.srv.AddTwoInts_Response(sum=30)
```

Server 로그:

```text
[cpp_add_two_ints_server]: Request: 10 + 20 = 30
```

## 6. Client Source 작성

`src/cpp_srvcli/src/add_two_ints_client.cpp`를 작성했다.

Client는 실행 인자를 정수로 변환하고 service 요청에 담는다.

```cpp
request->a = std::atoll(argv[1]);
request->b = std::atoll(argv[2]);
```

Service가 아직 발견되지 않았다면 잠시 기다린다.

```cpp
while (!client->wait_for_service(1s)) {
  RCLCPP_INFO(node->get_logger(), "Service not available, waiting again...");
}
```

## 7. Client 추가 후 Raspberry Pi 빌드

```bash
cd ~/ros2_ws
./scripts/build.sh
```

결과:

```text
Starting >>> cpp_practice
Starting >>> cpp_srvcli
Starting >>> py_practice
Finished <<< cpp_practice [1.90s]
Finished <<< py_practice [5.81s]
Finished <<< cpp_srvcli [19.7s]

Summary: 3 packages finished [21.0s]
Build completed.
```

## 8. C++ Client 실행

```bash
source install/setup.bash
ros2 run cpp_srvcli client 7 8
```

Client 결과:

```text
[cpp_add_two_ints_client]: Service not available, waiting again...
[cpp_add_two_ints_client]: Service not available, waiting again...
[cpp_add_two_ints_client]: Sum: 15
```

Server 결과:

```text
[cpp_add_two_ints_server]: Request: 7 + 8 = 15
```

## 9. Git 동기화

Pi에서 source 변경을 확인했다.

```text
?? src/cpp_srvcli/
```

빌드와 실행 검증 후 source를 commit, push했다.

```text
561245c feat: add C++ service and client
```

Windows 저장소에서도 pull 후 fast-forward 동기화를 확인했다.

## 확인한 내용

- `create_service()`로 C++ service server를 만들 수 있다.
- Server callback은 요청을 처리하고 응답 객체를 채운다.
- `create_client()`로 C++ service client를 만들 수 있다.
- Client는 service discovery가 완료될 때까지 기다릴 수 있다.
- `async_send_request()`로 요청을 전송하고 응답을 받을 수 있다.
- Raspberry Pi에서 CLI 요청과 C++ client 요청을 모두 검증했다.

## 다음 실습

Python service/client package를 작성한다.
