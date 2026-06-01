# 04. ROS 2 Actions

## 학습 목표

Raspberry Pi 4B에서 `/turtlesim` action server를 실행하고, action 목록, 타입, 연결 상태, 인터페이스를 확인한다.

CLI에서 회전 goal을 보내고 feedback과 최종 result를 검증한다.

## 핵심 개념

Action은 완료까지 시간이 걸리는 작업을 요청할 때 사용하는 통신 방식이다.

Service와 마찬가지로 client가 server에 요청을 보낸다. 다만 action은 작업 목표인 goal을 보내고, 처리 중 feedback을 계속 받을 수 있으며, 마지막에 result를 받는다. 필요하면 진행 중인 작업을 취소할 수도 있다.

이번 실습에서는 `/turtlesim` node가 제공하는 `/turtle1/rotate_absolute` action을 사용했다.

- Goal: 목표 방향 `theta`
- Result: 시작 위치를 기준으로 회전한 각도 `delta`
- Feedback: 남은 회전 각도 `remaining`

## 사용한 명령어

### SSH 환경에서 turtlesim headless 실행

```bash
source /opt/ros/humble/setup.bash
QT_QPA_PLATFORM=offscreen ros2 run turtlesim turtlesim_node
```

### Action 확인과 goal 전송

```bash
source /opt/ros/humble/setup.bash
ros2 action list
ros2 action list -t
ros2 action info /turtle1/rotate_absolute
ros2 interface show turtlesim/action/RotateAbsolute
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.57}" --feedback
```

## 실행 결과 요약

`/turtlesim` node가 `/turtle1/rotate_absolute` action server를 제공하는 것을 확인했다.

```text
/turtle1/rotate_absolute [turtlesim/action/RotateAbsolute]
```

Action 연결 상태:

```text
Action: /turtle1/rotate_absolute
Action clients: 0
Action servers: 1
    /turtlesim
```

별도의 action client node를 실행하지 않았으므로 조회 시점의 client 수는 0이었다.

Action 인터페이스 구조:

```text
float32 theta
---
float32 delta
---
float32 remaining
```

CLI에서 `theta=1.57` goal을 전송하자 goal이 승인됐다.

```text
Goal accepted with ID: 305a1e44f5e84793bff9a6e25a8dfd58
```

처리 중에는 남은 회전 각도인 `remaining` feedback이 지속적으로 출력됐다.

```text
Feedback:
    remaining: 1.5700000524520874

Feedback:
    remaining: 1.5540000200271606

Feedback:
    remaining: 0.018000006675720215
```

마지막으로 회전 결과와 성공 상태를 확인했다.

```text
Result:
    delta: -1.5520000457763672

Goal finished with status: SUCCEEDED
```

server 터미널에서도 완료 로그가 출력됐다.

```text
[turtlesim]: Rotation goal completed successfully
```

## 에러 및 해결

SSH 환경이므로 앞선 Parameters 실습과 동일하게 `QT_QPA_PLATFORM=offscreen`을 지정했다.

화면에서 거북이의 회전을 직접 확인하지는 못했지만, feedback 감소와 최종 result, server 완료 로그를 통해 action이 정상적으로 처리됐음을 검증했다.

## 정리

Action은 작업 완료까지 시간이 필요한 요청에 적합하다.

이번 실습에서는 `/turtle1/rotate_absolute` action에 회전 goal을 보내고, 남은 회전량 feedback이 점차 감소하는 과정과 최종 성공 result를 확인했다.

## 발표/설명용 요약

이번 실습에서는 ROS 2 action을 학습했다. Raspberry Pi에서 `/turtlesim` action server에 회전 goal을 전달하고, 작업 중 남은 회전량 feedback과 최종 성공 result를 확인했다. 이를 통해 action이 긴 작업의 진행 상태와 결과를 함께 다루는 통신 방식임을 이해했다.
