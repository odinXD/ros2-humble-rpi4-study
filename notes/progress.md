# 학습 진행 상황

## 현재 단계

ROS 2 CLI 기초 실습을 진행하고 있다.

Nodes, Topics, Services 실습을 완료했으며, 다음 단계는 Parameters 실습이다.

## 완료한 실습

- Raspberry Pi 4B ROS 2 Humble 환경 확인
- `./scripts/check_env.sh` 실행
- `./scripts/build.sh` 실행
- ROS 2 Nodes CLI 실습
- ROS 2 Topics CLI 실습
- `demo_nodes_cpp`의 `talker`와 `listener` 연결 확인
- ROS 2 Services CLI 실습
- `demo_nodes_cpp`의 `add_two_ints_server` 요청 및 응답 확인

## Raspberry Pi 검증 결과

- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `/home/doyeong/ros2_ws`
- `ros2` 명령 정상 인식
- `colcon` 명령 정상 인식
- 현재 사용자 작성 패키지는 없으므로 빌드 결과는 `0 packages finished`
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

## 다음 작업

1. Parameters CLI 실습
2. `turtlesim` 패키지 설치 여부 확인
3. `/turtlesim` node 실행
4. parameter 목록, 조회, 변경, dump 확인
5. `notes/03_parameters.md` 작성

## 관련 문서

- `notes/00_environment_setup.md`
- `notes/01_nodes_topics.md`
- `notes/02_services.md`
- `archive/2026-06-01_nodes_topics_lab.md`
- `archive/2026-06-01_services_lab.md`
