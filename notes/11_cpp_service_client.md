# 11. C++ Service와 Client 작성

## 학습 목표

`ament_cmake` 기반 C++ package에 service server와 client를 작성한다.

Raspberry Pi 4B에서 두 정수를 전달하고 합계를 응답받는 흐름을 검증한다.

## 핵심 개념

Service는 client가 요청을 보내고 server가 결과를 응답하는 통신 방식이다.

이번 실습에서는 기존 CLI 실습에서 사용한 `example_interfaces/srv/AddTwoInts` 타입을 직접 작성한 C++ node에 적용했다.

- Package: `cpp_srvcli`
- Server Node: `/cpp_add_two_ints_server`
- Client Node: `/cpp_add_two_ints_client`
- Service: `/cpp_add_two_ints`
- Service Type: `example_interfaces/srv/AddTwoInts`

## Package 구조

```text
src/cpp_srvcli/
├── CMakeLists.txt
├── package.xml
├── include/cpp_srvcli/
└── src/
    ├── add_two_ints_server.cpp
    └── add_two_ints_client.cpp
```

## 변경한 파일

### `package.xml`

```xml
<depend>rclcpp</depend>
<depend>example_interfaces</depend>
```

### `src/add_two_ints_server.cpp`

Server는 요청의 `a`, `b`를 더한 뒤 응답의 `sum`에 저장한다.

```cpp
response->sum = request->a + request->b;
```

Service 이름은 `cpp_add_two_ints`이다.

```cpp
auto service = node->create_service<example_interfaces::srv::AddTwoInts>(
  "cpp_add_two_ints", &add);
```

### `src/add_two_ints_client.cpp`

Client는 실행 인자로 받은 정수 두 개를 요청에 담는다.

```cpp
request->a = std::atoll(argv[1]);
request->b = std::atoll(argv[2]);
```

Service를 찾은 뒤 비동기 요청을 보내고 응답 완료까지 기다린다.

```cpp
auto result = client->async_send_request(request);
```

### `CMakeLists.txt`

```cmake
add_executable(server src/add_two_ints_server.cpp)
ament_target_dependencies(server rclcpp example_interfaces)

add_executable(client src/add_two_ints_client.cpp)
ament_target_dependencies(client rclcpp example_interfaces)
```

## 사용한 명령어

### Package 생성

```bash
cd ~/ros2_ws/src
ros2 pkg create \
  --build-type ament_cmake \
  --license Apache-2.0 \
  cpp_srvcli \
  --dependencies rclcpp example_interfaces
```

### Raspberry Pi에서 빌드와 Server 실행

```bash
cd ~/ros2_ws
./scripts/build.sh
source install/setup.bash
ros2 run cpp_srvcli server
```

### CLI에서 Service 확인과 호출

```bash
source ~/ros2_ws/install/setup.bash
ros2 service list -t
ros2 service type /cpp_add_two_ints
ros2 service call /cpp_add_two_ints example_interfaces/srv/AddTwoInts "{a: 10, b: 20}"
```

### C++ Client 실행

```bash
source ~/ros2_ws/install/setup.bash
ros2 run cpp_srvcli client 7 8
```

## 실행 결과 요약

Raspberry Pi에서 세 package 빌드가 성공했다.

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

Server가 service 요청을 기다리는 상태로 실행됐다.

```text
[cpp_add_two_ints_server]: Ready to add two ints.
```

CLI로 `10`, `20`을 요청하자 `30`이 응답으로 돌아왔다.

```text
requester: making request: example_interfaces.srv.AddTwoInts_Request(a=10, b=20)

response:
example_interfaces.srv.AddTwoInts_Response(sum=30)
```

C++ client로 `7`, `8`을 요청하자 `15`가 응답으로 돌아왔다.

```text
[cpp_add_two_ints_client]: Sum: 15
```

Server에서도 처리된 요청을 확인했다.

```text
[cpp_add_two_ints_server]: Request: 7 + 8 = 15
```

## 에러 및 해결

이번 실습에서는 별도로 기록할 구조적 오류가 발생하지 않았다.

Client가 server를 발견하기 전까지 다음 로그가 출력될 수 있다.

```text
Service not available, waiting again...
```

ROS 2 discovery가 완료되고 server를 찾으면 요청이 정상적으로 처리된다.

## 정리

Service server는 요청을 받을 때 callback을 실행하고 응답을 채운다.

Client는 service가 준비될 때까지 기다린 뒤 비동기 요청을 보내고 결과를 확인한다.

이번 실습에서는 CLI와 직접 작성한 C++ client 두 방식으로 `/cpp_add_two_ints` service를 검증했다.

## 발표/설명용 요약

이번 실습에서는 C++ ROS 2 service server와 client를 작성했다. Raspberry Pi에서 `/cpp_add_two_ints` service에 두 정수를 전달하고 합계를 응답받았다. CLI 호출과 직접 작성한 client 실행을 모두 확인하며 service 요청 및 응답 구조와 discovery 대기 흐름을 이해했다.
