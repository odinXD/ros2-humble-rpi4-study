# 2026-06-02 Custom msg/srv Interface 실습 일지

## 실습 환경

- Device: Raspberry Pi 4B
- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `~/ros2_ws`

## 실습 목적

`study_interfaces` package에 custom message와 service 타입을 정의한다.

Raspberry Pi에서 interface code generation을 수행하고 CLI로 결과를 조회한다.

## 1. Interface Package 생성

```bash
cd ~/ros2_ws/src
ros2 pkg create \
  --build-type ament_cmake \
  --license Apache-2.0 \
  study_interfaces

cd study_interfaces
mkdir msg srv
```

## 2. Custom Message 작성

`src/study_interfaces/msg/StudyStatus.msg`를 작성했다.

```text
string learner
string topic
int32 progress
bool completed
```

## 3. Custom Service 작성

`src/study_interfaces/srv/AddThreeInts.srv`를 작성했다.

```text
int64 a
int64 b
int64 c
---
int64 sum
```

## 4. Interface 생성 설정

`CMakeLists.txt`에 generator package와 interface 파일을 등록했다.

```cmake
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/StudyStatus.msg"
  "srv/AddThreeInts.srv"
)
```

`package.xml`에는 build, runtime, group 설정을 추가했다.

```xml
<build_depend>rosidl_default_generators</build_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```

## 5. Raspberry Pi에서 빌드

```bash
cd ~/ros2_ws
./scripts/build.sh
source install/setup.bash
```

결과:

```text
Starting >>> cpp_practice
Starting >>> cpp_srvcli
Starting >>> py_practice
Starting >>> py_srvcli
Finished <<< cpp_practice [2.97s]
Finished <<< cpp_srvcli [3.03s]
Starting >>> study_interfaces
Finished <<< py_practice [8.09s]
Finished <<< py_srvcli [8.31s]
Finished <<< study_interfaces [30.2s]

Summary: 5 packages finished [34.5s]
Build completed.
```

## 6. Interface 목록 확인

```bash
ros2 interface package study_interfaces
```

결과:

```text
study_interfaces/srv/AddThreeInts
study_interfaces/msg/StudyStatus
```

## 7. Custom Message 확인

```bash
ros2 interface show study_interfaces/msg/StudyStatus
```

결과:

```text
string learner
string topic
int32 progress
bool completed
```

## 8. Custom Service 확인

```bash
ros2 interface show study_interfaces/srv/AddThreeInts
```

결과:

```text
int64 a
int64 b
int64 c
---
int64 sum
```

## 확인한 내용

- ROS 2 interface package는 custom msg/srv 타입을 별도로 관리한다.
- `rosidl_default_generators`가 interface code를 생성한다.
- `rosidl_generate_interfaces()`에 `.msg`, `.srv` 파일을 등록한다.
- `ros2 interface package`로 package가 제공하는 interface 목록을 확인할 수 있다.
- `ros2 interface show`로 interface 필드 구조를 확인할 수 있다.
- Raspberry Pi에서 `study_interfaces` 빌드와 interface 조회를 검증했다.

## 다음 실습

`StudyStatus` custom message를 Python publisher와 subscriber에서 사용한다.
