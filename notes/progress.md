# 학습 진행 상황

## 현재 단계

ROS 2 CLI 기초 실습을 진행하고 있다.

ROS 2 CLI 기초 실습과 Launching nodes 실습을 완료했다.

첫 ROS 2 CMake package 생성과 Raspberry Pi 빌드 검증을 완료했다.

`cpp_practice` package의 C++ publisher node 작성과 Raspberry Pi 검증을 완료했다.

C++ publisher와 subscriber node 작성 및 Raspberry Pi 통신 검증을 완료했다.

`ament_python` 기반 `py_practice` package 생성과 Python publisher 검증을 완료했다.

Python publisher와 subscriber node 작성 및 Raspberry Pi 통신 검증을 완료했다.

C++ service/client 작성과 Raspberry Pi 요청 및 응답 검증을 완료했다.

Python service/client 작성과 Raspberry Pi 요청 및 응답 검증을 완료했다.

Custom msg/srv interface package 생성과 Raspberry Pi 빌드 검증을 완료했다.

다음 단계는 `StudyStatus` custom message를 실제 publisher/subscriber에서 사용하는 실습이다.

## 완료한 실습

- Raspberry Pi 4B ROS 2 Humble 환경 확인
- `./scripts/check_env.sh` 실행
- `./scripts/build.sh` 실행
- ROS 2 Nodes CLI 실습
- ROS 2 Topics CLI 실습
- `demo_nodes_cpp`의 `talker`와 `listener` 연결 확인
- ROS 2 Services CLI 실습
- `demo_nodes_cpp`의 `add_two_ints_server` 요청 및 응답 확인
- ROS 2 Parameters CLI 실습
- SSH 환경에서 `QT_QPA_PLATFORM=offscreen`으로 `/turtlesim` 실행
- `/turtlesim`의 parameter 목록, 조회, 변경, dump 확인
- ROS 2 Actions CLI 실습
- `/turtle1/rotate_absolute` action goal, feedback, result 확인
- ROS 2 Launching nodes CLI 실습
- `turtlesim/multisim.launch.py`로 두 개의 namespaced node 실행 확인
- CMake 기반 `cpp_practice` package 생성
- Raspberry Pi에서 `cpp_practice` package 빌드 성공
- `ros2 run cpp_practice hello_node` 실행 확인
- `hello_node`를 `rclcpp` 기반 C++ publisher node로 확장
- `/hello_publisher`에서 `/practice_chatter` topic 발행 확인
- C++ `listener_node` subscriber 작성
- `/hello_subscriber`에서 `/practice_chatter` topic 수신 확인
- `ament_python` 기반 `py_practice` package 생성
- Python `/py_hello_publisher`에서 `/py_practice_chatter` topic 발행 확인
- Python `/py_hello_subscriber`에서 `/py_practice_chatter` topic 수신 확인
- C++ `cpp_srvcli` package 생성
- `/cpp_add_two_ints` service server와 client 요청 및 응답 확인
- Python `py_srvcli` package 생성
- `/py_add_two_ints` service server와 client 요청 및 응답 확인
- `study_interfaces` package 생성
- Custom `StudyStatus.msg`, `AddThreeInts.srv` 생성
- Raspberry Pi에서 custom interface 빌드 및 조회 확인

## Raspberry Pi 검증 결과

- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `/home/doyeong/ros2_ws`
- `ros2` 명령 정상 인식
- `colcon` 명령 정상 인식
- 초기 workspace 빌드 결과: `0 packages finished`
- 실행 node: `/talker`, `/listener`
- Topic: `/chatter`
- Message Type: `std_msgs/msg/String`
- Publisher Count: `1`
- Subscription Count: `1`
- Publish Rate: 약 `1 Hz`
- Service Server Node: `/add_two_ints_server`
- Service: `/add_two_ints`
- Service Type: `example_interfaces/srv/AddTwoInts`
- Request: `a=7`, `b=5`
- Response: `sum=12`
- Turtlesim Package: 설치 확인
- Headless Node: `/turtlesim`
- Parameter: `background_g=86`
- Parameter 변경: `background_r=150`
- Parameter 복원: `background_r=69`
- Action Server: `/turtlesim`
- Action: `/turtle1/rotate_absolute`
- Action Type: `turtlesim/action/RotateAbsolute`
- Goal: `theta=1.57`
- Result: `delta=-1.5520000457763672`
- Goal Status: `SUCCEEDED`
- Launch File: `turtlesim/multisim.launch.py`
- Launched Node: `/turtlesim1/turtlesim`
- Launched Node: `/turtlesim2/turtlesim`
- Package: `cpp_practice`
- Build Type: `ament_cmake`
- Executable: `hello_node`
- Raspberry Pi Build Result: `1 package finished`
- Runtime Output: `hello world cpp_practice package`
- Publisher Node: `/hello_publisher`
- Publisher Topic: `/practice_chatter`
- Publisher Message Type: `std_msgs/msg/String`
- Publisher Count: `1`
- Publisher Subscription Count: `0`
- Publisher Rate: 약 `1 Hz`
- Publisher Message: `Hello from cpp_practice: <count>`
- Subscriber Executable: `listener_node`
- Subscriber Node: `/hello_subscriber`
- Subscriber Topic: `/practice_chatter`
- Topic Publisher Count: `1`
- Topic Subscription Count: `1`
- Subscriber Message: `I heard: 'Hello from cpp_practice: <count>'`
- Python Package: `py_practice`
- Python Build Type: `ament_python`
- Python Publisher Executable: `publisher_node`
- Python Publisher Node: `/py_hello_publisher`
- Python Publisher Topic: `/py_practice_chatter`
- Python Message Type: `std_msgs/msg/String`
- Python Publisher Count: `1`
- Python Subscription Count: `0`
- Python Publisher Rate: 약 `1 Hz`
- Python Publisher Message: `Hello from py_practice: <count>`
- Python Subscriber Executable: `subscriber_node`
- Python Subscriber Node: `/py_hello_subscriber`
- Python Subscriber Topic: `/py_practice_chatter`
- Python Topic Publisher Count: `1`
- Python Topic Subscription Count: `1`
- Python Subscriber Message: `I heard: 'Hello from py_practice: <count>'`
- C++ Service Package: `cpp_srvcli`
- C++ Service Server Node: `/cpp_add_two_ints_server`
- C++ Service Client Node: `/cpp_add_two_ints_client`
- C++ Service: `/cpp_add_two_ints`
- C++ Service Type: `example_interfaces/srv/AddTwoInts`
- CLI Request: `a=10`, `b=20`
- CLI Response: `sum=30`
- C++ Client Request: `a=7`, `b=8`
- C++ Client Response: `sum=15`
- Python Service Package: `py_srvcli`
- Python Service Server Node: `/py_add_two_ints_server`
- Python Service Client Node: `/py_add_two_ints_client`
- Python Service: `/py_add_two_ints`
- Python Service Type: `example_interfaces/srv/AddTwoInts`
- Python CLI Request: `a=30`, `b=40`
- Python CLI Response: `sum=70`
- Python Client Request: `a=9`, `b=6`
- Python Client Response: `sum=15`
- Interface Package: `study_interfaces`
- Custom Message: `study_interfaces/msg/StudyStatus`
- Custom Service: `study_interfaces/srv/AddThreeInts`
- Raspberry Pi Build Result: `5 packages finished`

## 다음 작업

1. Custom message publisher/subscriber 작성
2. `py_practice`에 `study_interfaces` 의존성 추가
3. `StudyStatus` publisher 작성
4. `StudyStatus` subscriber 작성
5. Raspberry Pi에서 package 빌드
6. `/study_status` topic 메시지 전달 확인

## 관련 문서

- `notes/00_environment_setup.md`
- `notes/01_nodes_topics.md`
- `notes/02_services.md`
- `notes/03_parameters.md`
- `notes/04_actions.md`
- `notes/05_launching_nodes.md`
- `notes/06_cpp_package.md`
- `notes/07_cpp_publisher.md`
- `notes/08_cpp_subscriber.md`
- `notes/09_py_package_publisher.md`
- `notes/10_py_subscriber.md`
- `notes/11_cpp_service_client.md`
- `notes/12_py_service_client.md`
- `notes/13_custom_interfaces.md`
- `archive/2026-06-01_nodes_topics_lab.md`
- `archive/2026-06-01_services_lab.md`
- `archive/2026-06-01_parameters_lab.md`
- `archive/2026-06-01_actions_lab.md`
- `archive/2026-06-01_launching_nodes_lab.md`
- `archive/2026-06-01_cpp_package_lab.md`
- `archive/2026-06-01_cpp_publisher_lab.md`
- `archive/2026-06-01_cpp_subscriber_lab.md`
- `archive/2026-06-01_py_package_publisher_lab.md`
- `archive/2026-06-01_py_subscriber_lab.md`
- `archive/2026-06-01_cpp_service_client_lab.md`
- `archive/2026-06-01_py_service_client_lab.md`
- `archive/2026-06-02_custom_interfaces_lab.md`
