# 16. Bringup Launch Package

## 학습 목표

여러 ROS 2 node를 한 번에 실행할 수 있는 bringup package를 구성한다.

Raspberry Pi 4B에서 launch file을 실행하고, custom message publisher와 subscriber가 함께 시작되는 것을 확인한다.

## 핵심 개념

각 node를 `ros2 run`으로 하나씩 실행할 수도 있지만, 실제 ROS 2 시스템은 여러 node를 함께 시작해야 하는 경우가 많다.

Launch file은 실행할 node 목록과 설정을 하나의 파일로 묶는다. 이를 사용하면 반복되는 실행 명령을 줄이고 시스템 시작 절차를 일정하게 유지할 수 있다.

이번 실습에서는 launch 전용 package인 `study_bringup`을 만들고, 다음 두 node를 함께 실행했다.

```text
/study_status_publisher
/study_status_subscriber
```

## Package 구조

```text
src/study_bringup/
├── launch/
│   └── status_bringup_launch.py
├── package.xml
├── resource/
│   └── study_bringup
├── setup.cfg
├── setup.py
└── study_bringup/
    └── __init__.py
```

## Package 설정

### `package.xml`

Launch file과 실행 대상 package를 사용하기 위한 의존성을 추가했다.

```xml
<depend>launch</depend>
<depend>launch_ros</depend>
<depend>py_practice</depend>
```

### `setup.py`

빌드 후 launch file이 install 영역에 포함되도록 설정했다.

```python
import os
from glob import glob
```

```python
(os.path.join('share', package_name, 'launch'),
    glob('launch/*_launch.py')),
```

### Launch File

`status_bringup_launch.py`는 `status_publisher`와 `status_subscriber`를 함께 실행한다.

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

## 사용한 명령어

### Package 생성

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

### Raspberry Pi에서 빌드와 실행

```bash
cd ~/ros2_ws
./scripts/build.sh
source install/setup.bash
ros2 launch study_bringup status_bringup_launch.py
```

### Node와 Topic 확인

```bash
source ~/ros2_ws/install/setup.bash
ros2 node list
ros2 topic info /study_status
ros2 topic echo /study_status
```

## 실행 결과 요약

Raspberry Pi에서 여섯 package 빌드가 성공했다.

```text
Summary: 6 packages finished [16.0s]
Build completed.
```

Launch가 두 프로세스를 함께 시작했다.

```text
[INFO] [status_publisher-1]: process started
[INFO] [status_subscriber-2]: process started
```

실행된 node와 topic 연결 상태를 확인했다.

```text
/study_status_publisher
/study_status_subscriber

Type: study_interfaces/msg/StudyStatus
Publisher count: 1
Subscription count: 1
```

`progress` 값이 `0`부터 `100`까지 증가하고, 완료 시 `completed=True`가 전달되는 것을 확인했다.

```text
[study_status_subscriber]: I heard: learner=doyeong, topic=custom_interfaces, progress=0, completed=False
[study_status_subscriber]: I heard: learner=doyeong, topic=custom_interfaces, progress=100, completed=True
```

## 에러 및 해결

이번 실습에서는 별도로 기록할 구조적 오류가 발생하지 않았다.

## 정리

Bringup package는 여러 node의 실행 방법을 한곳에 모아 시스템 시작 절차를 관리한다.

이번 실습에서는 `ros2 launch study_bringup status_bringup_launch.py` 명령 하나로 custom message publisher와 subscriber를 함께 실행했다.

## 발표/설명용 요약

이번 실습에서는 ROS 2 bringup package와 Python launch file을 작성했다. Raspberry Pi에서 launch 명령 하나로 custom message publisher와 subscriber를 동시에 실행하고 `/study_status` topic 연결을 확인했다. 이를 통해 여러 node로 구성된 시스템의 시작 절차를 일관되게 관리하는 방식을 이해했다.
