# 10. Python Subscriber Node 작성

## 학습 목표

`py_practice` package에 Python subscriber node를 추가한다.

Raspberry Pi 4B에서 publisher와 subscriber를 함께 실행하고, `/py_practice_chatter` topic의 메시지가 실제로 전달되는지 확인한다.

## 핵심 개념

Python subscriber는 `create_subscription()`으로 topic을 구독한다.

새 메시지가 도착하면 등록된 callback 함수가 실행된다.

이번 실습에서는 `/py_hello_subscriber` node가 `/py_practice_chatter` topic을 구독하고 문자열 메시지를 로그로 출력하도록 구현했다.

- Publisher Node: `/py_hello_publisher`
- Subscriber Node: `/py_hello_subscriber`
- Topic: `/py_practice_chatter`
- Message Type: `std_msgs/msg/String`

## 변경한 파일

### `py_practice/subscriber_node.py`

```python
self.subscription = self.create_subscription(
    String,
    'py_practice_chatter',
    self.listener_callback,
    10,
)
```

Callback에서는 수신한 문자열을 로그로 출력한다.

```python
def listener_callback(self, message):
    self.get_logger().info(f"I heard: '{message.data}'")
```

### `setup.py`

`ros2 run py_practice subscriber_node` 명령으로 실행할 수 있도록 console script를 등록했다.

```python
'console_scripts': [
    'publisher_node = py_practice.publisher_node:main',
    'subscriber_node = py_practice.subscriber_node:main',
],
```

## 사용한 명령어

### Raspberry Pi에서 빌드

```bash
cd ~/ros2_ws
./scripts/build.sh
source install/setup.bash
```

### Publisher 실행

```bash
ros2 run py_practice publisher_node
```

### Subscriber 실행

```bash
ros2 run py_practice subscriber_node
```

### ROS graph 확인

```bash
source ~/ros2_ws/install/setup.bash
ros2 node list
ros2 node info /py_hello_subscriber
ros2 topic info /py_practice_chatter
```

## 실행 결과 요약

Raspberry Pi에서 C++와 Python package 빌드가 성공했다.

```text
Starting >>> cpp_practice
Starting >>> py_practice
Finished <<< cpp_practice [1.57s]
Finished <<< py_practice [4.99s]

Summary: 2 packages finished [6.24s]
Build completed.
```

Subscriber는 publisher의 메시지를 연속으로 수신했다.

```text
[py_hello_subscriber]: I heard: 'Hello from py_practice: 13'
[py_hello_subscriber]: I heard: 'Hello from py_practice: 14'
[py_hello_subscriber]: I heard: 'Hello from py_practice: 15'
```

ROS graph에서 두 node를 확인했다.

```text
/py_hello_publisher
/py_hello_subscriber
```

`/py_hello_subscriber`가 `/py_practice_chatter`를 구독하는 것도 확인했다.

```text
Subscribers:
  /py_practice_chatter: std_msgs/msg/String
```

Topic 연결 상태:

```text
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 1
```

## 에러 및 해결

이번 실습에서는 별도로 기록할 구조적 오류가 발생하지 않았다.

## 정리

Python에서도 C++과 마찬가지로 publisher와 subscriber는 topic을 통해 연결된다.

이번 실습에서는 직접 작성한 Python publisher와 subscriber를 Raspberry Pi에서 실행하고 `/py_practice_chatter` topic의 문자열 메시지가 정상 전달되는 것을 확인했다.

## 발표/설명용 요약

이번 실습에서는 Python ROS 2 subscriber node를 작성했다. Raspberry Pi에서 `/py_hello_publisher`와 `/py_hello_subscriber`를 실행하고 `/py_practice_chatter` topic의 문자열 메시지가 전달되는 것을 확인했다. 이를 통해 Python에서도 C++과 동일한 pub-sub 구조를 구현할 수 있음을 검증했다.
