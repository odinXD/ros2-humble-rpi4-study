# 01. ROS 2 Nodes와 Topics

## 학습 목표

Raspberry Pi 4B에서 ROS 2의 `talker`와 `listener` 예제를 실행하고, node와 topic의 관계를 CLI 명령으로 확인한다.

## 핵심 개념

### Node

Node는 ROS 2에서 하나의 역할을 담당하는 실행 단위이다.

이번 실습에서는 다음 두 node를 사용했다.

- `/talker`: 문자열 메시지를 발행한다.
- `/listener`: 문자열 메시지를 구독한다.

### Topic

Topic은 node 사이에서 메시지가 흐르는 통신 채널이다.

이번 실습에서 `/talker`는 `/chatter` topic에 메시지를 publish했고, `/listener`는 같은 topic을 subscribe했다.

`/chatter`의 메시지 타입은 `std_msgs/msg/String`이다.

## 사용한 명령어

### Talker 실행

```bash
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp talker
```

### Node 확인

```bash
ros2 node list
ros2 node info /talker
```

### Topic 확인

```bash
ros2 topic list
ros2 topic list -t
ros2 topic info /chatter
ros2 topic echo /chatter
ros2 topic hz /chatter
```

### Listener 연결 후 확인

```bash
ros2 run demo_nodes_cpp listener
ros2 node list
ros2 node info /listener
ros2 topic info /chatter
```

## 실행 결과 요약

Raspberry Pi 4B에서 `/talker`를 실행한 뒤 `/chatter` topic에 `Hello World` 메시지가 지속적으로 발행되는 것을 확인했다.

```text
/chatter [std_msgs/msg/String]
Publisher count: 1
Subscription count: 0
```

`ros2 topic echo /chatter`를 실행하자 다음과 같이 실제 메시지를 확인할 수 있었다.

```text
data: 'Hello World: 160'
---
data: 'Hello World: 161'
---
```

`ros2 topic hz /chatter`를 통해 메시지가 약 1초에 한 번 발행되는 것도 확인했다.

```text
average rate: 1.000
```

이후 `/listener`를 연결하자 실행 중인 node와 `/chatter` 연결 상태가 다음과 같이 바뀌었다.

```text
/listener
/talker

Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 1
```

`/listener`가 `/talker`의 메시지를 정상적으로 수신하는 것도 확인했다.

```text
[listener]: I heard: [Hello World: 27]
[listener]: I heard: [Hello World: 28]
```

## 에러 및 해결

이번 실습에서는 별도의 에러가 발생하지 않았다.

## 정리

`/talker`와 `/listener`는 서로 직접 연결되는 것이 아니라 `/chatter` topic을 통해 메시지를 주고받는다.

`/listener`를 나중에 실행했을 때 이전 메시지를 받지 않고 실행 이후의 메시지부터 받은 것을 확인했다. 이번 예제의 topic은 현재 발행되는 데이터를 전달하는 통신 채널로 이해할 수 있다.

## 발표/설명용 요약

이번 실습에서는 ROS 2의 node와 topic 개념을 학습했다. Raspberry Pi에서 `/talker`와 `/listener`를 실행하고, `/chatter` topic을 통해 `std_msgs/msg/String` 타입의 메시지가 약 1 Hz로 전달되는 것을 확인했다. 이를 통해 publisher와 subscriber가 topic을 중심으로 연결된다는 점을 이해했다.
