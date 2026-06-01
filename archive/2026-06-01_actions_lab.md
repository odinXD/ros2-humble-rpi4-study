# 2026-06-01 Actions 실습 일지

## 실습 환경

- Device: Raspberry Pi 4B
- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `~/ros2_ws`
- Access: SSH terminal

## 실습 목적

`/turtlesim` node의 action server를 확인하고, CLI에서 회전 goal을 보낸다.

Action의 goal, feedback, result 흐름을 실제 출력으로 검증한다.

## 1. Offscreen 모드로 turtlesim 실행

첫 번째 터미널에서 다음 명령을 실행했다.

```bash
source /opt/ros/humble/setup.bash
QT_QPA_PLATFORM=offscreen ros2 run turtlesim turtlesim_node
```

결과:

```text
[turtlesim]: Starting turtlesim with node name /turtlesim
[turtlesim]: Spawning turtle [turtle1] at x=[5.544445], y=[5.544445], theta=[0.000000]
```

SSH 환경이므로 GUI 창 없이 node를 실행했다.

## 2. Action 목록 확인

다른 터미널에서 ROS 2 환경을 불러오고 action 목록을 확인했다.

```bash
source /opt/ros/humble/setup.bash
ros2 action list
```

결과:

```text
/turtle1/rotate_absolute
```

## 3. Action 타입 확인

```bash
ros2 action list -t
```

결과:

```text
/turtle1/rotate_absolute [turtlesim/action/RotateAbsolute]
```

## 4. Action 연결 상태 확인

```bash
ros2 action info /turtle1/rotate_absolute
```

결과:

```text
Action: /turtle1/rotate_absolute
Action clients: 0
Action servers: 1
    /turtlesim
```

`/turtlesim` action server가 1개 실행 중이다.

별도의 `turtle_teleop_key` client node는 실행하지 않았으므로 조회 시점의 action client 수는 0이다.

## 5. Action 인터페이스 확인

```bash
ros2 interface show turtlesim/action/RotateAbsolute
```

결과:

```text
# The desired heading in radians
float32 theta
---
# The angular displacement in radians to the starting position
float32 delta
---
# The remaining rotation in radians
float32 remaining
```

Action 인터페이스는 세 부분으로 구성된다.

- Goal: 목표 방향 `theta`
- Result: 회전 결과 `delta`
- Feedback: 남은 회전 각도 `remaining`

## 6. Action goal 전송

```bash
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.57}" --feedback
```

goal이 승인됐다.

```text
Waiting for an action server to become available...
Sending goal:
     theta: 1.57

Goal accepted with ID: 305a1e44f5e84793bff9a6e25a8dfd58
```

## 7. Feedback 확인

`--feedback` 옵션을 지정했으므로 처리 중 남은 회전 각도가 계속 출력됐다.

결과 일부:

```text
Feedback:
    remaining: 1.5700000524520874

Feedback:
    remaining: 1.5540000200271606

Feedback:
    remaining: 1.5380001068115234

...

Feedback:
    remaining: 0.03400003910064697

Feedback:
    remaining: 0.018000006675720215
```

`remaining` 값이 점차 감소하므로 회전 작업이 진행되고 있음을 확인할 수 있다.

## 8. Result 확인

작업이 끝난 뒤 최종 결과가 출력됐다.

```text
Result:
    delta: -1.5520000457763672

Goal finished with status: SUCCEEDED
```

첫 번째 터미널에서도 server 완료 로그가 출력됐다.

```text
[turtlesim]: Rotation goal completed successfully
```

## 확인한 내용

- Action은 시간이 걸리는 작업의 goal, feedback, result를 다룬다.
- `/turtlesim`은 `/turtle1/rotate_absolute` action server를 제공한다.
- Action 타입은 `turtlesim/action/RotateAbsolute`이다.
- CLI에서 `theta=1.57` goal을 보낼 수 있다.
- `remaining` feedback이 지속적으로 감소했다.
- 최종 result는 `delta=-1.5520000457763672`였다.
- Goal은 `SUCCEEDED` 상태로 완료됐다.
- SSH headless 환경에서도 CLI 출력으로 action 동작을 검증할 수 있다.

## 다음 실습

Launching nodes CLI 실습을 진행한다.

SSH 환경이므로 Qt 기반 node를 실행할 때 offscreen 모드를 유지한다.

```bash
QT_QPA_PLATFORM=offscreen ros2 launch turtlesim multisim.launch.py
```
