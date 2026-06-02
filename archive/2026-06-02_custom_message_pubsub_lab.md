# 2026-06-02 Custom Message Publisher / Subscriber 실습 일지

## 실습 환경

- Device: Raspberry Pi 4B
- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `~/ros2_ws`

## 실습 목적

`study_interfaces/msg/StudyStatus` custom message를 `py_practice` package의 Python publisher와 subscriber에서 사용한다.

Raspberry Pi에서 package 빌드, node 실행, topic 연결, field 전달을 검증한다.

## 1. Package 의존성 추가

`src/py_practice/package.xml`에 다음 의존성을 추가했다.

```xml
<depend>study_interfaces</depend>
```

## 2. Custom Message Publisher 작성

`src/py_practice/py_practice/status_publisher.py`를 작성했다.

Publisher는 `StudyStatus` message를 생성하고 `/study_status` topic으로 1초마다 발행한다.

주요 필드:

```text
learner: doyeong
topic: custom_interfaces
progress: 0부터 100까지 증가
completed: progress가 100 이상이면 true
```

## 3. Custom Message Subscriber 작성

`src/py_practice/py_practice/status_subscriber.py`를 작성했다.

Subscriber는 `/study_status` topic을 구독하고 수신한 `StudyStatus` field를 로그로 출력한다.

## 4. Entry Point 추가

`src/py_practice/setup.py`에 실행 가능한 node를 등록했다.

```python
'status_publisher = py_practice.status_publisher:main',
'status_subscriber = py_practice.status_subscriber:main',
```

## 5. Raspberry Pi에서 빌드

```bash
cd ~/ros2_ws
./scripts/build.sh
```

결과:

```text
Starting >>> study_interfaces
Starting >>> cpp_practice
Starting >>> cpp_srvcli
Starting >>> py_srvcli
Finished <<< cpp_srvcli [2.41s]
Finished <<< cpp_practice [2.59s]
Finished <<< study_interfaces [3.34s]
Starting >>> py_practice
Finished <<< py_srvcli [7.34s]
Finished <<< py_practice [5.56s]

Summary: 5 packages finished [10.2s]
Build completed.
```

## 6. Publisher와 Subscriber 실행

Publisher terminal:

```bash
source ~/ros2_ws/install/setup.bash
ros2 run py_practice status_publisher
```

Subscriber terminal:

```bash
source ~/ros2_ws/install/setup.bash
ros2 run py_practice status_subscriber
```

Subscriber에서 다음 형식의 로그를 확인했다.

```text
[study_status_subscriber]: I heard: learner=doyeong, topic=custom_interfaces, progress=100, completed=True
```

## 7. Node와 Topic 확인

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

## 8. 환경 문제와 해결

처음 subscriber를 실행했을 때 Python에서 custom interface module을 찾지 못했다.

```text
ModuleNotFoundError: No module named 'study_interfaces'
```

새 interface를 빌드한 뒤에도 기존 terminal session에는 최신 workspace overlay가 자동으로 반영되지 않는다.

각 terminal에서 setup script를 다시 source하여 해결했다.

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
```

## 확인한 내용

- `py_practice` package에서 `study_interfaces` 의존성을 사용할 수 있다.
- `StudyStatus` custom message를 Python publisher와 subscriber에서 사용할 수 있다.
- `/study_status` topic에 publisher와 subscriber가 각각 하나씩 연결되었다.
- `learner`, `topic`, `progress`, `completed` field가 Raspberry Pi에서 실제로 전달되었다.
- 새 package나 generated interface를 사용하려면 기존 terminal에서도 최신 overlay를 다시 source해야 한다.

## 다음 실습

`study_interfaces/srv/AddThreeInts` custom service를 실제 server와 client에서 사용한다.
