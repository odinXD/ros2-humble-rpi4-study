# 2026-06-01 Python Package와 Publisher 실습 일지

## 실습 환경

- Device: Raspberry Pi 4B
- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `~/ros2_ws`

## 실습 목적

`ament_python` 기반 `py_practice` package를 생성한다.

Python publisher를 작성하고 Raspberry Pi에서 빌드, 실행, topic 발행 결과를 검증한다.

## 1. Python Package 생성

```bash
cd ~/ros2_ws/src
ros2 pkg create \
  --build-type ament_python \
  --license Apache-2.0 \
  py_practice \
  --dependencies rclpy std_msgs
```

주요 결과:

```text
package name: py_practice
destination directory: /home/doyeong/ros2_ws/src
package format: 3
version: 0.0.0
licenses: ['Apache-2.0']
build type: ament_python
dependencies: ['rclpy', 'std_msgs']
```

## 2. Package 구조 확인

```bash
cd ~/ros2_ws
find src/py_practice -maxdepth 3 -type f | sort
```

결과:

```text
src/py_practice/LICENSE
src/py_practice/package.xml
src/py_practice/py_practice/__init__.py
src/py_practice/resource/py_practice
src/py_practice/setup.cfg
src/py_practice/setup.py
src/py_practice/test/test_copyright.py
src/py_practice/test/test_flake8.py
src/py_practice/test/test_pep257.py
```

## 3. Publisher Source 작성

`src/py_practice/py_practice/publisher_node.py`를 작성했다.

주요 구조:

```python
class HelloPublisher(Node):

    def __init__(self):
        super().__init__('py_hello_publisher')
        self.publisher_ = self.create_publisher(String, 'py_practice_chatter', 10)
        self.count = 0
        self.timer = self.create_timer(1.0, self.timer_callback)
```

## 4. Console Script 등록

`setup.py`에 publisher 실행 명령을 등록했다.

```python
entry_points={
    'console_scripts': [
        'publisher_node = py_practice.publisher_node:main',
    ],
},
```

## 5. Raspberry Pi에서 빌드

```bash
cd ~/ros2_ws
./scripts/build.sh
```

결과:

```text
Starting >>> cpp_practice
Starting >>> py_practice
Finished <<< py_practice [5.99s]
Finished <<< cpp_practice [38.2s]

Summary: 2 packages finished [39.4s]
Build completed.
```

## 6. Python Publisher 실행

```bash
source install/setup.bash
ros2 run py_practice publisher_node
```

결과 일부:

```text
[py_hello_publisher]: Publishing: 'Hello from py_practice: 0'
[py_hello_publisher]: Publishing: 'Hello from py_practice: 1'
[py_hello_publisher]: Publishing: 'Hello from py_practice: 2'
```

## 7. ROS Graph 확인

```bash
source ~/ros2_ws/install/setup.bash
ros2 node list
ros2 node info /py_hello_publisher
```

주요 결과:

```text
/py_hello_publisher
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /py_practice_chatter: std_msgs/msg/String
    /rosout: rcl_interfaces/msg/Log
```

## 8. Topic 목록과 실제 메시지 확인

```bash
ros2 topic list -t
```

결과:

```text
/parameter_events [rcl_interfaces/msg/ParameterEvent]
/py_practice_chatter [std_msgs/msg/String]
/rosout [rcl_interfaces/msg/Log]
```

```bash
ros2 topic echo /py_practice_chatter
```

결과 일부:

```text
data: 'Hello from py_practice: 40'
---
data: 'Hello from py_practice: 41'
---
data: 'Hello from py_practice: 42'
---
```

## 9. Topic 상태와 발행 주기 확인

```bash
ros2 topic info /py_practice_chatter
```

결과:

```text
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 0
```

```bash
ros2 topic hz /py_practice_chatter
```

결과 일부:

```text
average rate: 1.000
        min: 0.998s max: 1.002s std dev: 0.00078s window: 19
```

## 확인한 내용

- Python ROS 2 package는 `ament_python` 빌드 타입을 사용한다.
- `package.xml`에 `rclpy`, `std_msgs` 의존성을 선언한다.
- `setup.py`의 `console_scripts`에 실행 명령과 Python 함수를 연결한다.
- `create_publisher()`와 `create_timer()`로 주기적인 topic 발행을 구현할 수 있다.
- Raspberry Pi에서 `/py_hello_publisher`와 `/py_practice_chatter` 동작을 검증했다.

## 다음 실습

`/py_practice_chatter`를 구독하는 Python subscriber node를 작성한다.
