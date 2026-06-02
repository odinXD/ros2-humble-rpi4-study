# 14. Custom Message Publisher / Subscriber

## 학습 목표

직접 정의한 `study_interfaces/msg/StudyStatus` message를 Python publisher와 subscriber에서 사용한다.

Raspberry Pi 4B에서 package를 빌드하고, `/study_status` topic을 통해 여러 필드가 하나의 message로 전달되는 것을 확인한다.

## 핵심 개념

기존 publisher/subscriber 실습에서는 `std_msgs/msg/String`을 사용했다.

이번에는 프로젝트에서 직접 정의한 `StudyStatus` message를 사용했다.

```text
string learner
string topic
int32 progress
bool completed
```

Custom message를 사용하면 문자열 하나만 전달하는 대신, 의미가 분리된 여러 필드를 하나의 데이터 구조로 묶어서 전달할 수 있다.

## Package 변경 사항

### `package.xml`

`py_practice` package가 `study_interfaces`를 사용할 수 있도록 의존성을 추가했다.

```xml
<depend>study_interfaces</depend>
```

### `setup.py`

새 Python node를 `ros2 run`으로 실행할 수 있도록 entry point를 추가했다.

```python
'status_publisher = py_practice.status_publisher:main',
'status_subscriber = py_practice.status_subscriber:main',
```

### Publisher

`status_publisher`는 `/study_status` topic으로 학습 상태를 1초마다 발행한다.

```python
self.publisher_ = self.create_publisher(StudyStatus, 'study_status', 10)
```

### Subscriber

`status_subscriber`는 `/study_status` topic을 구독하고 수신한 필드를 로그로 출력한다.

```python
self.subscription = self.create_subscription(
    StudyStatus,
    'study_status',
    self.listener_callback,
    10,
)
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
source ~/ros2_ws/install/setup.bash
ros2 run py_practice status_publisher
```

### Subscriber 실행

```bash
source ~/ros2_ws/install/setup.bash
ros2 run py_practice status_subscriber
```

### Topic 연결 확인

```bash
source ~/ros2_ws/install/setup.bash
ros2 node list
ros2 topic info /study_status
ros2 topic echo /study_status
```

## 실행 결과 요약

Raspberry Pi에서 다섯 package 빌드가 성공했다.

```text
Summary: 5 packages finished [10.2s]
Build completed.
```

두 node가 실행된 것을 확인했다.

```text
/study_status_publisher
/study_status_subscriber
```

`/study_status` topic에는 publisher와 subscriber가 각각 하나씩 연결되었다.

```text
Type: study_interfaces/msg/StudyStatus
Publisher count: 1
Subscription count: 1
```

Subscriber와 CLI에서 custom message 필드가 전달되는 것을 확인했다.

```text
learner: doyeong
topic: custom_interfaces
progress: 100
completed: true
```

## 에러 및 해결

처음 subscriber를 실행했을 때 다음 오류가 발생했다.

```text
ModuleNotFoundError: No module named 'study_interfaces'
```

Custom interface를 새로 빌드했더라도, 이미 열려 있던 터미널에는 최신 workspace overlay가 자동으로 반영되지 않는다.

각 터미널에서 최신 setup script를 다시 source하여 해결했다.

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
```

## 정리

Custom message는 node 사이에서 주고받는 데이터 구조를 프로젝트 목적에 맞게 설계할 수 있게 한다.

이번 실습에서는 `StudyStatus` message를 Python publisher와 subscriber에 연결하고, Raspberry Pi에서 실제 topic 통신을 확인했다.

새 package나 interface를 빌드한 뒤에는 이미 열려 있던 터미널에서도 workspace overlay를 다시 source해야 한다.

## 발표/설명용 요약

이번 실습에서는 직접 정의한 `StudyStatus` custom message를 Python publisher와 subscriber에서 사용했다. Raspberry Pi에서 `/study_status` topic의 연결 상태와 message 필드 전달을 확인했다. 이를 통해 여러 데이터를 의미 있는 하나의 구조로 묶어 node 사이에서 전달하는 방식을 이해했다.
