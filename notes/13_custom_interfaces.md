# 13. Custom msg/srv Interface 작성

## 학습 목표

프로젝트에서 직접 사용할 ROS 2 message와 service 타입을 정의한다.

Raspberry Pi 4B에서 interface package를 빌드하고, ROS 2 CLI로 생성된 타입을 확인한다.

## 핵심 개념

ROS 2 interface는 node 사이에서 주고받을 데이터 구조를 정의한다.

기존 실습에서는 ROS 2가 제공하는 `std_msgs/msg/String`, `example_interfaces/srv/AddTwoInts`를 사용했다.

이번에는 프로젝트 전용 interface package인 `study_interfaces`를 만들고 message와 service 타입을 직접 정의했다.

- Message: `study_interfaces/msg/StudyStatus`
- Service: `study_interfaces/srv/AddThreeInts`

## Package 구조

```text
src/study_interfaces/
├── CMakeLists.txt
├── package.xml
├── msg/
│   └── StudyStatus.msg
└── srv/
    └── AddThreeInts.srv
```

## Interface 정의

### `msg/StudyStatus.msg`

```text
string learner
string topic
int32 progress
bool completed
```

학습자, 학습 주제, 진행률, 완료 여부를 하나의 메시지로 표현한다.

### `srv/AddThreeInts.srv`

```text
int64 a
int64 b
int64 c
---
int64 sum
```

세 정수를 요청으로 받고 합계를 응답으로 돌려준다.

## 빌드 설정

### `CMakeLists.txt`

```cmake
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/StudyStatus.msg"
  "srv/AddThreeInts.srv"
)
```

### `package.xml`

```xml
<build_depend>rosidl_default_generators</build_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```

## 사용한 명령어

### Package 생성

```bash
cd ~/ros2_ws/src
ros2 pkg create \
  --build-type ament_cmake \
  --license Apache-2.0 \
  study_interfaces

cd study_interfaces
mkdir msg srv
```

### Raspberry Pi에서 빌드

```bash
cd ~/ros2_ws
./scripts/build.sh
source install/setup.bash
```

### 생성된 Interface 확인

```bash
ros2 interface package study_interfaces
ros2 interface show study_interfaces/msg/StudyStatus
ros2 interface show study_interfaces/srv/AddThreeInts
```

## 실행 결과 요약

Raspberry Pi에서 다섯 package 빌드가 성공했다.

```text
Starting >>> cpp_practice
Starting >>> cpp_srvcli
Starting >>> py_practice
Starting >>> py_srvcli
Starting >>> study_interfaces
Finished <<< study_interfaces [30.2s]

Summary: 5 packages finished [34.5s]
Build completed.
```

생성된 interface 목록:

```text
study_interfaces/srv/AddThreeInts
study_interfaces/msg/StudyStatus
```

Custom message 확인:

```text
string learner
string topic
int32 progress
bool completed
```

Custom service 확인:

```text
int64 a
int64 b
int64 c
---
int64 sum
```

## 에러 및 해결

이번 실습에서는 별도로 기록할 구조적 오류가 발생하지 않았다.

## 정리

Interface package를 별도로 만들면 여러 node가 동일한 데이터 구조를 공유할 수 있다.

이번 실습에서는 학습 상태를 표현하는 `StudyStatus` 메시지와 세 정수를 더하는 `AddThreeInts` service를 직접 정의하고 Raspberry Pi에서 생성 결과를 확인했다.

## 발표/설명용 요약

이번 실습에서는 ROS 2 custom interface package를 작성했다. Raspberry Pi에서 `study_interfaces`를 빌드하고 프로젝트 전용 `StudyStatus` message와 `AddThreeInts` service가 생성된 것을 확인했다. 이를 통해 node 사이의 데이터 구조를 직접 설계하고 공유하는 방식을 이해했다.
