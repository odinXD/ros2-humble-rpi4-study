# 2026-06-01 Services 실습 일지

## 실습 환경

- Device: Raspberry Pi 4B
- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `~/ros2_ws`

## 실습 목적

`demo_nodes_cpp`의 `add_two_ints_server`를 실행하고, ROS 2 service의 목록, 타입, 인터페이스 구조를 확인한다. 이후 실제 요청을 보내고 server의 처리 결과를 검증한다.

## 1. Service server 실행

첫 번째 터미널에서 다음 명령을 실행했다.

```bash
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp add_two_ints_server
```

이 명령을 실행하면 server는 요청이 들어올 때까지 대기한다.

## 2. Service 목록 확인

다른 터미널에서 ROS 2 환경을 불러오고 service 목록을 확인했다.

```bash
source /opt/ros/humble/setup.bash
ros2 service list
```

결과:

```text
/add_two_ints
/add_two_ints_server/describe_parameters
/add_two_ints_server/get_parameter_types
/add_two_ints_server/get_parameters
/add_two_ints_server/list_parameters
/add_two_ints_server/set_parameters
/add_two_ints_server/set_parameters_atomically
```

`/add_two_ints`는 이번 실습에서 사용할 service이다.

`/add_two_ints_server/...` 형태의 service들은 node의 parameter를 조회하거나 변경하기 위한 기본 service이다.

## 3. Service 타입 확인

service 이름과 타입을 함께 확인했다.

```bash
ros2 service list -t
```

주요 결과:

```text
/add_two_ints [example_interfaces/srv/AddTwoInts]
```

특정 service의 타입만 따로 조회했다.

```bash
ros2 service type /add_two_ints
```

결과:

```text
example_interfaces/srv/AddTwoInts
```

## 4. Service 인터페이스 확인

```bash
ros2 interface show example_interfaces/srv/AddTwoInts
```

결과:

```text
int64 a
int64 b
---
int64 sum
```

`---`를 기준으로 위쪽은 요청, 아래쪽은 응답이다.

client는 `a`, `b`를 보내고 server는 `sum`을 반환한다.

## 5. Service 요청 보내기

```bash
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 7, b: 5}"
```

client 터미널 결과:

```text
requester: making request: example_interfaces.srv.AddTwoInts_Request(a=7, b=5)

response:
example_interfaces.srv.AddTwoInts_Response(sum=12)
```

server 터미널 결과:

```text
[add_two_ints_server]: Incoming request
a: 7 b: 5
```

## 확인한 내용

- Service는 client가 요청하고 server가 응답하는 통신 방식이다.
- `/add_two_ints`의 타입은 `example_interfaces/srv/AddTwoInts`이다.
- 요청 데이터는 `int64 a`, `int64 b`이다.
- 응답 데이터는 `int64 sum`이다.
- Raspberry Pi에서 `a=7`, `b=5`를 요청하여 `sum=12` 응답을 확인했다.
- ROS 2 node는 parameter를 다루기 위한 기본 service도 함께 제공할 수 있다.

## 다음 실습

Parameters CLI 실습을 진행한다.

공식 튜토리얼에서 사용하는 `turtlesim` 패키지가 설치되어 있는지 먼저 확인한다.

```bash
ros2 pkg executables turtlesim
```
