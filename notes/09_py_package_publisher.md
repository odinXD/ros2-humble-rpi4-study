# 09. Python Package와 Publisher Node 작성

## 학습 목표

Raspberry Pi 4B의 ROS 2 workspace에 `ament_python` 기반 package를 생성한다.

Python publisher node를 작성하고, node와 topic 메시지가 실제로 동작하는지 CLI로 검증한다.

## 핵심 개념

Python ROS 2 package는 `ament_python` 빌드 타입을 사용한다.

C++ package에서 `CMakeLists.txt`로 실행 파일을 등록했다면, Python package에서는 `setup.py`의 `console_scripts`에 실행 명령을 등록한다.

이번 실습에서는 `/py_hello_publisher` node가 1초마다 `/py_practice_chatter` topic에 문자열 메시지를 발행하도록 구현했다.

- Package: `py_practice`
- Node: `/py_hello_publisher`
- Topic: `/py_practice_chatter`
- Message Type: `std_msgs/msg/String`
- Publish Rate: 약 `1 Hz`

## Package 구조

```text
src/py_practice/
├── package.xml
├── resource/py_practice
├── setup.cfg
├── setup.py
├── py_practice/
│   ├── __init__.py
│   └── publisher_node.py
└── test/
```

## 변경한 파일

### `package.xml`

Python ROS 2 client library와 문자열 메시지 타입 의존성을 포함한다.

```xml
<depend>rclpy</depend>
<depend>std_msgs</depend>
```

### `setup.py`

`ros2 run py_practice publisher_node` 명령으로 Python 함수를 실행할 수 있도록 entry point를 등록했다.

```python
entry_points={
    'console_scripts': [
        'publisher_node = py_practice.publisher_node:main',
    ],
},
```

### `py_practice/publisher_node.py`

`rclpy` 기반 publisher node를 작성했다.

```python
self.publisher_ = self.create_publisher(String, 'py_practice_chatter', 10)
self.timer = self.create_timer(1.0, self.timer_callback)
```

Timer callback은 문자열 메시지를 생성하고 발행한다.

```python
message = String()
message.data = f'Hello from py_practice: {self.count}'
self.publisher_.publish(message)
```

## 사용한 명령어

### Package 생성

```bash
cd ~/ros2_ws/src
ros2 pkg create \
  --build-type ament_python \
  --license Apache-2.0 \
  py_practice \
  --dependencies rclpy std_msgs
```

### Raspberry Pi에서 빌드와 실행

```bash
cd ~/ros2_ws
./scripts/build.sh
source install/setup.bash
ros2 run py_practice publisher_node
```

### ROS graph와 Topic 확인

```bash
source ~/ros2_ws/install/setup.bash
ros2 node list
ros2 node info /py_hello_publisher
ros2 topic list -t
ros2 topic echo /py_practice_chatter
ros2 topic info /py_practice_chatter
ros2 topic hz /py_practice_chatter
```

## 실행 결과 요약

Raspberry Pi에서 C++와 Python package 빌드가 모두 성공했다.

```text
Starting >>> cpp_practice
Starting >>> py_practice
Finished <<< py_practice [5.99s]
Finished <<< cpp_practice [38.2s]

Summary: 2 packages finished [39.4s]
Build completed.
```

Python publisher가 메시지를 지속적으로 발행했다.

```text
[py_hello_publisher]: Publishing: 'Hello from py_practice: 0'
[py_hello_publisher]: Publishing: 'Hello from py_practice: 1'
[py_hello_publisher]: Publishing: 'Hello from py_practice: 2'
```

ROS graph에서 publisher node를 확인했다.

```text
/py_hello_publisher
```

Topic과 메시지 타입:

```text
/py_practice_chatter [std_msgs/msg/String]
```

실제 메시지:

```text
data: 'Hello from py_practice: 40'
---
data: 'Hello from py_practice: 41'
---
```

Topic 상태:

```text
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 0
```

발행 주기:

```text
average rate: 1.000
```

## 에러 및 해결

이번 실습에서는 별도로 기록할 구조적 오류가 발생하지 않았다.

## 정리

`ament_python` package는 `setup.py`의 `console_scripts`를 통해 Python 함수를 ROS 2 실행 명령으로 연결한다.

이번 실습에서는 `rclpy` 기반 publisher를 작성하고 `/py_practice_chatter` topic에 문자열 메시지가 약 1 Hz로 발행되는 것을 Raspberry Pi에서 검증했다.

## 발표/설명용 요약

이번 실습에서는 Python ROS 2 package와 publisher node를 작성했다. Raspberry Pi에서 `/py_hello_publisher`를 실행하고 `/py_practice_chatter` topic에 문자열 메시지가 약 1 Hz로 발행되는 것을 확인했다. 이를 통해 C++와 Python package의 실행 파일 등록 방식 차이를 이해했다.
