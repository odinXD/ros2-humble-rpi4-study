# 2026-06-01 Launching Nodes 실습 일지

## 실습 환경

- Device: Raspberry Pi 4B
- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `~/ros2_ws`
- Access: SSH terminal

## 실습 목적

`turtlesim` 패키지에 포함된 `multisim.launch.py`를 실행하고, 하나의 launch file로 여러 node가 동시에 시작되는지 확인한다.

SSH 환경이므로 Qt 기반 node는 offscreen 모드로 실행한다.

## 1. Launch file 실행

첫 번째 터미널에서 다음 명령을 실행했다.

```bash
source /opt/ros/humble/setup.bash
QT_QPA_PLATFORM=offscreen ros2 launch turtlesim multisim.launch.py
```

launch 시스템 로그:

```text
[INFO] [launch]: All log files can be found below /home/doyeong/.ros/log/2026-06-01-14-01-39-870310-doyeong-desktop-3846
[INFO] [launch]: Default logging verbosity is set to INFO
```

두 개의 프로세스가 시작됐다.

```text
[INFO] [turtlesim_node-1]: process started with pid [3857]
[INFO] [turtlesim_node-2]: process started with pid [3859]
```

## 2. Namespaced turtlesim node 시작 확인

각 프로세스의 로그를 확인했다.

```text
[turtlesim_node-2] [INFO] [turtlesim2.turtlesim]: Starting turtlesim with node name /turtlesim2/turtlesim
[turtlesim_node-1] [INFO] [turtlesim1.turtlesim]: Starting turtlesim with node name /turtlesim1/turtlesim
```

각 node는 기본 거북이 `turtle1`을 생성했다.

```text
[turtlesim_node-2] [INFO] [turtlesim2.turtlesim]: Spawning turtle [turtle1] at x=[5.544445], y=[5.544445], theta=[0.000000]
[turtlesim_node-1] [INFO] [turtlesim1.turtlesim]: Spawning turtle [turtle1] at x=[5.544445], y=[5.544445], theta=[0.000000]
```

## 3. Node 목록 확인

다른 터미널에서 ROS 2 환경을 불러오고 node 목록을 확인했다.

```bash
source /opt/ros/humble/setup.bash
ros2 node list
```

결과:

```text
/turtlesim1/turtlesim
/turtlesim2/turtlesim
```

## 확인한 내용

- Launch file은 여러 node와 설정을 한 번에 실행할 수 있다.
- `ros2 launch turtlesim multisim.launch.py`는 두 개의 `turtlesim_node` 프로세스를 시작한다.
- Namespace를 사용하면 동일한 종류의 node를 이름 충돌 없이 여러 개 실행할 수 있다.
- 실행된 node 이름은 `/turtlesim1/turtlesim`, `/turtlesim2/turtlesim`이다.
- SSH headless 환경에서도 `QT_QPA_PLATFORM=offscreen`을 사용해 launch 동작을 검증할 수 있다.

## 다음 실습

첫 ROS 2 package 생성과 Raspberry Pi 빌드를 진행한다.

```bash
cd ~/ros2_ws
mkdir -p src
cd src
ros2 pkg create --build-type ament_cmake --license Apache-2.0 --node-name hello_node cpp_practice
```
