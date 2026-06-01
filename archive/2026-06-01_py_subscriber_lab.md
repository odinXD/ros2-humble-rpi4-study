# 2026-06-01 Python Subscriber 실습 일지

## 실습 환경

- Device: Raspberry Pi 4B
- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `~/ros2_ws`

## 실습 목적

`py_practice` package에 `/py_practice_chatter` topic을 구독하는 Python subscriber를 추가한다.

Raspberry Pi에서 Python publisher와 subscriber를 함께 실행하고 메시지 전달 상태를 확인한다.

## 1. Subscriber Source 추가

`src/py_practice/py_practice/subscriber_node.py`를 작성했다.

주요 구조:

```python
class HelloSubscriber(Node):

    def __init__(self):
        super().__init__('py_hello_subscriber')
        self.subscription = self.create_subscription(
            String,
            'py_practice_chatter',
            self.listener_callback,
            10,
        )

    def listener_callback(self, message):
        self.get_logger().info(f"I heard: '{message.data}'")
```

## 2. Console Script 등록

`setup.py`에 subscriber 실행 명령을 등록했다.

```python
'console_scripts': [
    'publisher_node = py_practice.publisher_node:main',
    'subscriber_node = py_practice.subscriber_node:main',
],
```

## 3. Raspberry Pi에서 빌드

```bash
cd ~/ros2_ws
./scripts/build.sh
```

결과:

```text
Starting >>> cpp_practice
Starting >>> py_practice
Finished <<< cpp_practice [1.57s]
Finished <<< py_practice [4.99s]

Summary: 2 packages finished [6.24s]
Build completed.
```

## 4. Python Publisher 실행

첫 번째 터미널:

```bash
source install/setup.bash
ros2 run py_practice publisher_node
```

결과 일부:

```text
[py_hello_publisher]: Publishing: 'Hello from py_practice: 11'
[py_hello_publisher]: Publishing: 'Hello from py_practice: 12'
[py_hello_publisher]: Publishing: 'Hello from py_practice: 13'
```

## 5. Python Subscriber 실행

두 번째 터미널:

```bash
ros2 run py_practice subscriber_node
```

결과 일부:

```text
[py_hello_subscriber]: I heard: 'Hello from py_practice: 13'
[py_hello_subscriber]: I heard: 'Hello from py_practice: 14'
[py_hello_subscriber]: I heard: 'Hello from py_practice: 15'
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
/py_hello_publisher
/py_hello_subscriber
```

## 7. Subscriber 정보 확인

```bash
ros2 node info /py_hello_subscriber
```

주요 결과:

```text
/py_hello_subscriber
  Subscribers:
    /py_practice_chatter: std_msgs/msg/String
```

## 8. Topic 연결 상태 확인

```bash
ros2 topic info /py_practice_chatter
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
 M src/py_practice/setup.py
?? src/py_practice/py_practice/subscriber_node.py
```

빌드와 실행 검증 후 source를 commit, push했다.

```text
505597f feat: add Python subscriber node
```

Windows 저장소에서도 pull 후 fast-forward 동기화를 확인했다.

## 확인한 내용

- Python subscriber는 `create_subscription()`으로 topic을 구독한다.
- 새 메시지가 도착하면 callback 함수가 실행된다.
- `setup.py`의 `console_scripts`에 subscriber 실행 명령을 등록한다.
- Python publisher와 subscriber는 `/py_practice_chatter` topic을 통해 연결된다.
- Raspberry Pi에서 직접 작성한 Python node 사이의 통신을 검증했다.

## 다음 실습

C++ service/client package를 작성한다.
