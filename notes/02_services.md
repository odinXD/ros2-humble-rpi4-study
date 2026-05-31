# 02. ROS 2 Services

## 학습 목표

Raspberry Pi 4B에서 `add_two_ints_server` 예제를 실행하고, ROS 2 service의 목록, 타입, 인터페이스를 확인한 뒤 실제 요청과 응답을 검증한다.

## 핵심 개념

Service는 client가 server에 요청을 보내고, server가 처리 결과를 응답하는 통신 방식이다.

Topic이 지속적으로 흐르는 데이터를 전달하는 채널이라면, service는 특정 작업을 한 번 요청하고 결과를 확인할 때 적합하다.

이번 실습에서는 `/add_two_ints` service를 사용했다.

- 요청: 정수 `a`, `b`
- 응답: 두 정수의 합계 `sum`
- Service Type: `example_interfaces/srv/AddTwoInts`

## 사용한 명령어

### Service server 실행

```bash
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp add_two_ints_server
```

### Service 목록과 타입 확인

```bash
ros2 service list
ros2 service list -t
ros2 service type /add_two_ints
ros2 interface show example_interfaces/srv/AddTwoInts
```

### 요청 보내기

```bash
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 7, b: 5}"
```

## 실행 결과 요약

Raspberry Pi 4B에서 `/add_two_ints` service가 정상적으로 등록된 것을 확인했다.

```text
/add_two_ints [example_interfaces/srv/AddTwoInts]
```

service 타입을 조회한 결과:

```text
example_interfaces/srv/AddTwoInts
```

인터페이스 구조를 조회한 결과:

```text
int64 a
int64 b
---
int64 sum
```

`---` 위쪽은 client가 보내는 요청이고, 아래쪽은 server가 돌려주는 응답이다.

`a=7`, `b=5`를 전달하자 합계 `12`가 응답으로 돌아왔다.

```text
requester: making request: example_interfaces.srv.AddTwoInts_Request(a=7, b=5)

response:
example_interfaces.srv.AddTwoInts_Response(sum=12)
```

server 터미널에서도 요청을 받은 것을 확인했다.

```text
[add_two_ints_server]: Incoming request
a: 7 b: 5
```

## 에러 및 해결

이번 실습에서는 별도의 에러가 발생하지 않았다.

## 정리

`/add_two_ints` service server는 요청이 들어오기를 기다린다. client가 두 정수를 담은 요청을 보내면 server가 이를 처리하고 합계를 응답한다.

이번 실습을 통해 topic과 service의 용도 차이를 확인했다. Topic은 지속적인 메시지 전달에 적합하고, service는 한 번의 요청과 응답이 필요한 작업에 적합하다.

## 발표/설명용 요약

이번 실습에서는 ROS 2의 service 통신 방식을 학습했다. Raspberry Pi에서 `/add_two_ints` service server를 실행하고 정수 `7`과 `5`를 요청값으로 전달하여 합계 `12`를 응답으로 받았다. 이를 통해 service가 client의 요청에 대해 server가 결과를 반환하는 통신 방식임을 확인했다.
