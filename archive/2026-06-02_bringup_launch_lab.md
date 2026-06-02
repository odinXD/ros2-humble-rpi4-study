# 2026-06-02 Bringup Launch Package 실습 일지

## 실습 환경

- Device: Raspberry Pi 4B
- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `~/ros2_ws`

## 실습 목적

Launch 전용 `study_bringup` package를 만들고 custom message publisher와 subscriber를 한 번에 실행한다.

Raspberry Pi에서 package 빌드, launch 실행, node 목록, topic 연결을 검증한다.

## 1. Bringup Package 생성

```bash
cd ~/ros2_ws/src

ros2 pkg create \
  --build-type ament_python \
  --license Apache-2.0 \
  study_bringup \
  --dependencies launch launch_ros py_practice

cd study_bringup
mkdir launch
```

## 2. Launch File 설치 설정

`src/study_bringup/setup.py`에 launch file 설치 설정을 추가했다.

```python
import os
from glob import glob
```

```python
(os.path.join('share', package_name, 'launch'),
    glob('launch/*_launch.py')),
```

## 3. Launch File 작성

`src/study_bringup/launch/status_bringup_launch.py`를 작성했다.

```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_practice',
            executable='status_publisher',
            output='screen',
        ),
        Node(
            package='py_practice',
            executable='status_subscriber',
            output='screen',
        ),
    ])
```

## 4. Raspberry Pi에서 빌드

```bash
cd ~/ros2_ws
./scripts/build.sh
source install/setup.bash
```

결과:

```text
Starting >>> study_interfaces
Starting >>> cpp_practice
Starting >>> cpp_srvcli
Finished <<< cpp_srvcli [0.95s]
Finished <<< cpp_practice [1.08s]
Finished <<< study_interfaces [2.87s]
Starting >>> py_practice
Starting >>> py_srvcli
Finished <<< py_practice [6.89s]
Starting >>> study_bringup
Finished <<< py_srvcli [6.95s]
Finished <<< study_bringup [5.01s]

Summary: 6 packages finished [16.0s]
Build completed.
```

## 5. Launch 실행

```bash
ros2 launch study_bringup status_bringup_launch.py
```

Launch가 두 프로세스를 시작했다.

```text
[INFO] [status_publisher-1]: process started
[INFO] [status_subscriber-2]: process started
```

`progress`가 증가하면서 publisher와 subscriber가 message를 주고받았다.

```text
[study_status_publisher]: Publishing: learner=doyeong, topic=custom_interfaces, progress=0, completed=False
[study_status_subscriber]: I heard: learner=doyeong, topic=custom_interfaces, progress=0, completed=False
[study_status_publisher]: Publishing: learner=doyeong, topic=custom_interfaces, progress=100, completed=True
[study_status_subscriber]: I heard: learner=doyeong, topic=custom_interfaces, progress=100, completed=True
```

## 6. Node와 Topic 확인

```bash
source ~/ros2_ws/install/setup.bash
ros2 node list
ros2 topic info /study_status
ros2 topic echo /study_status
```

Node 목록:

```text
/study_status_publisher
/study_status_subscriber
```

Topic 연결:

```text
Type: study_interfaces/msg/StudyStatus
Publisher count: 1
Subscription count: 1
```

Topic message:

```text
learner: doyeong
topic: custom_interfaces
progress: 100
completed: true
```

## 확인한 내용

- `study_bringup` package에 launch file을 포함할 수 있다.
- `setup.py`에서 launch file을 install 영역에 포함하도록 설정해야 한다.
- `ros2 launch` 명령 하나로 publisher와 subscriber를 함께 실행할 수 있다.
- `/study_status` topic에 publisher와 subscriber가 각각 하나씩 연결되었다.
- Raspberry Pi에서 custom message 전달을 실제로 검증했다.

## 다음 실습

현재까지의 실습을 README에 요약하고, Raspberry Pi 기반 간단한 ROS 2 응용 프로젝트의 방향을 정한다.
