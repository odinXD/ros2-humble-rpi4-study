# 2026-06-01 Nodes / Topics 실습 일지

## 실습 환경

- Device: Raspberry Pi 4B
- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `~/ros2_ws`

## 실습 목적

`demo_nodes_cpp`의 `talker`와 `listener`를 사용해 node 목록, node 정보, topic 목록, topic 타입, 실제 메시지, 발행 주기, publisher와 subscriber 연결 상태를 확인한다.

## 1. Talker 실행

첫 번째 터미널에서 다음 명령을 실행했다.

```bash
ros2 run demo_nodes_cpp talker
```

`/talker`가 약 1초 간격으로 메시지를 발행하는 것을 확인했다.

```text
[talker]: Publishing: 'Hello World: 1'
[talker]: Publishing: 'Hello World: 2'
[talker]: Publishing: 'Hello World: 3'
```

## 2. 실행 중인 Node 확인

다른 터미널에서 ROS 2 환경을 불러오고 node 목록을 확인했다.

```bash
source /opt/ros/humble/setup.bash
ros2 node list
```

결과:

```text
/talker
```

`/talker`의 상세 정보도 확인했다.

```bash
ros2 node info /talker
```

주요 결과:

```text
/talker
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
  Publishers:
    /chatter: std_msgs/msg/String
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
```

`/talker`가 `/chatter` topic에 `std_msgs/msg/String` 타입의 메시지를 publish한다는 것을 확인했다.

## 3. Topic 목록과 타입 확인

```bash
ros2 topic list
ros2 topic list -t
```

결과:

```text
/chatter
/parameter_events
/rosout
```

```text
/chatter [std_msgs/msg/String]
/parameter_events [rcl_interfaces/msg/ParameterEvent]
/rosout [rcl_interfaces/msg/Log]
```

`-t` 옵션을 사용하면 topic 이름과 메시지 타입을 함께 볼 수 있다.

## 4. Listener 연결 전 `/chatter` 상태 확인

```bash
ros2 topic info /chatter
```

결과:

```text
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 0
```

이 시점에는 `/talker`만 실행 중이므로 publisher는 1개이고 subscriber는 없다.

## 5. 실제 메시지 확인

```bash
ros2 topic echo /chatter
```

결과 일부:

```text
data: 'Hello World: 160'
---
data: 'Hello World: 161'
---
data: 'Hello World: 162'
---
```

`ros2 topic echo`는 지정한 topic을 subscribe하여 현재 흐르는 메시지를 터미널에 보여준다.

## 6. 발행 주기 확인

```bash
ros2 topic hz /chatter
```

결과 일부:

```text
average rate: 1.000
        min: 1.000s max: 1.000s std dev: 0.00017s window: 10
```

`/talker`는 `/chatter`에 약 1 Hz, 즉 1초에 한 번 메시지를 발행한다.

## 7. Listener 연결

다른 터미널에서 listener를 실행했다.

```bash
ros2 run demo_nodes_cpp listener
```

결과 일부:

```text
[listener]: I heard: [Hello World: 27]
[listener]: I heard: [Hello World: 28]
[listener]: I heard: [Hello World: 29]
```

listener를 나중에 실행했기 때문에 실행 이전에 발행된 메시지는 받지 않고 현재 흐르는 메시지부터 수신했다.

## 8. Listener 연결 후 상태 확인

```bash
ros2 node list
```

결과:

```text
/listener
/talker
```

listener의 상세 정보를 확인했다.

```bash
ros2 node info /listener
```

주요 결과:

```text
/listener
  Subscribers:
    /chatter: std_msgs/msg/String
    /parameter_events: rcl_interfaces/msg/ParameterEvent
```

`/chatter` 연결 상태도 다시 확인했다.

```bash
ros2 topic info /chatter
```

결과:

```text
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 1
```

## 확인한 내용

- Node는 ROS 2에서 하나의 역할을 담당하는 실행 단위이다.
- Topic은 node 사이에서 메시지가 흐르는 통신 채널이다.
- `/talker`는 publisher이고 `/listener`는 subscriber이다.
- 두 node는 `/chatter` topic을 통해 `std_msgs/msg/String` 메시지를 주고받는다.
- `/chatter`의 발행 주기는 약 1 Hz이다.
- listener를 나중에 실행하면 실행 이후에 흐르는 메시지부터 수신한다.

## 다음 실습

Services CLI 실습을 진행한다.

```bash
ros2 run demo_nodes_cpp add_two_ints_server
```
