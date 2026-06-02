# ROS 2 Humble Raspberry Pi Study

Raspberry Pi 4B에서 ROS 2 Humble의 핵심 개념을 학습하고, C++ 및 Python 예제를 직접 작성하며 검증한 기록입니다.

단순히 튜토리얼 명령어를 실행하는 데서 멈추지 않고, custom interface와 launch 기반 bringup 구조까지 단계적으로 구성했습니다.

## Environment

| Item | Value |
| --- | --- |
| Target Device | Raspberry Pi 4B |
| OS | Ubuntu Desktop 22.04 LTS 64-bit |
| Architecture | `aarch64` |
| ROS Distribution | ROS 2 Humble |
| Workspace | `~/ros2_ws` |

실제 ROS 2 빌드와 runtime 검증은 Raspberry Pi에서 수행합니다. Windows clone은 문서 정리와 GitHub 동기화에 사용합니다.

## Verified Topics

- ROS 2 CLI: node, topic, service, parameter, action
- `turtlesim` headless 실행과 launch 실습
- C++ publisher / subscriber
- Python publisher / subscriber
- C++ service / client
- Python service / client
- Custom message: `study_interfaces/msg/StudyStatus`
- Custom service: `study_interfaces/srv/AddThreeInts`
- Python launch file을 사용한 bringup 구성

## Packages

| Package | Build Type | Purpose |
| --- | --- | --- |
| `cpp_practice` | `ament_cmake` | C++ publisher / subscriber |
| `py_practice` | `ament_python` | Python publisher / subscriber, custom message 사용 |
| `cpp_srvcli` | `ament_cmake` | C++ service / client |
| `py_srvcli` | `ament_python` | Python service / client, custom service 사용 |
| `study_interfaces` | `ament_cmake` | Custom msg / srv 정의 |
| `study_bringup` | `ament_python` | 여러 node를 함께 실행하는 launch file |

## Quick Start

Raspberry Pi에서 workspace를 빌드합니다.

```bash
cd ~/ros2_ws
./scripts/check_env.sh
./scripts/build.sh
source install/setup.bash
```

Custom message publisher와 subscriber를 한 번에 실행합니다.

```bash
ros2 launch study_bringup status_bringup_launch.py
```

다른 terminal에서 연결 상태와 message를 확인합니다.

```bash
source ~/ros2_ws/install/setup.bash
ros2 node list
ros2 topic info /study_status
ros2 topic echo /study_status
```

검증된 topic 연결:

```text
Type: study_interfaces/msg/StudyStatus
Publisher count: 1
Subscription count: 1
```

## Custom Interfaces

### `StudyStatus.msg`

```text
string learner
string topic
int32 progress
bool completed
```

### `AddThreeInts.srv`

```text
int64 a
int64 b
int64 c
---
int64 sum
```

Custom service server를 실행합니다.

```bash
ros2 run py_srvcli three_ints_server
```

다른 terminal에서 Python client를 실행합니다.

```bash
source ~/ros2_ws/install/setup.bash
ros2 run py_srvcli three_ints_client 7 8 9
```

검증된 응답:

```text
[py_add_three_ints_client]: Sum: 24
```

## Repository Structure

```text
.
├── src/       # ROS 2 packages
├── notes/     # 개념과 결과를 정리한 학습 노트
├── archive/   # 상세 실습 순서와 의미 있는 terminal 출력
├── scripts/   # 환경 확인과 workspace 빌드 스크립트
├── AGENTS.md  # 프로젝트 운영 규칙
└── README.md
```

`build/`, `install/`, `log/`는 colcon 생성물이므로 Git에 포함하지 않습니다.

## Study Notes

- [환경 구성](notes/00_environment_setup.md)
- [Nodes / Topics](notes/01_nodes_topics.md)
- [Services](notes/02_services.md)
- [Parameters](notes/03_parameters.md)
- [Actions](notes/04_actions.md)
- [Launching Nodes](notes/05_launching_nodes.md)
- [C++ Package](notes/06_cpp_package.md)
- [C++ Publisher](notes/07_cpp_publisher.md)
- [C++ Subscriber](notes/08_cpp_subscriber.md)
- [Python Package / Publisher](notes/09_py_package_publisher.md)
- [Python Subscriber](notes/10_py_subscriber.md)
- [C++ Service / Client](notes/11_cpp_service_client.md)
- [Python Service / Client](notes/12_py_service_client.md)
- [Custom Interfaces](notes/13_custom_interfaces.md)
- [Custom Message Publisher / Subscriber](notes/14_custom_message_pubsub.md)
- [Custom Service / Client](notes/15_custom_service_client.md)
- [Bringup Launch Package](notes/16_bringup_launch.md)

현재 진행 상황은 [notes/progress.md](notes/progress.md)에 정리합니다.
