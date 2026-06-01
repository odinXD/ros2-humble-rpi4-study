# 05. ROS 2 Launching Nodes

## 학습 목표

Raspberry Pi 4B에서 ROS 2 launch file을 실행하고, 하나의 명령으로 여러 node를 동시에 시작할 수 있는지 확인한다.

SSH 환경에서 `turtlesim`의 `multisim.launch.py`를 headless 모드로 실행한다.

## 핵심 개념

Launch file은 여러 node와 설정을 한 번에 실행하기 위한 파일이다.

Node 수가 많아지면 터미널마다 `ros2 run` 명령을 반복하는 방식은 관리하기 어렵다. Launch file을 사용하면 하나의 `ros2 launch` 명령으로 시스템에 필요한 여러 node를 함께 시작할 수 있다.

이번 실습에서는 `turtlesim` 패키지에 포함된 `multisim.launch.py`를 실행했다.

이 launch file은 namespace가 다른 두 개의 turtlesim node를 시작한다.

- `/turtlesim1/turtlesim`
- `/turtlesim2/turtlesim`

## 사용한 명령어

### Launch file 실행

```bash
source /opt/ros/humble/setup.bash
QT_QPA_PLATFORM=offscreen ros2 launch turtlesim multisim.launch.py
```

### 실행된 Node 확인

```bash
source /opt/ros/humble/setup.bash
ros2 node list
```

## 실행 결과 요약

Launch 명령을 실행하자 `turtlesim_node` 프로세스 두 개가 시작됐다.

```text
[INFO] [turtlesim_node-1]: process started with pid [3857]
[INFO] [turtlesim_node-2]: process started with pid [3859]
```

각 프로세스는 서로 다른 namespace에서 node를 실행했다.

```text
[turtlesim2.turtlesim]: Starting turtlesim with node name /turtlesim2/turtlesim
[turtlesim1.turtlesim]: Starting turtlesim with node name /turtlesim1/turtlesim
```

다른 터미널에서 node 목록을 확인했다.

```text
/turtlesim1/turtlesim
/turtlesim2/turtlesim
```

## 에러 및 해결

이번 실습에서는 별도의 에러가 발생하지 않았다.

SSH 환경에서는 GUI 창을 표시할 수 없으므로 앞선 실습과 동일하게 `QT_QPA_PLATFORM=offscreen`을 지정했다.

## 정리

Launch file을 사용하면 여러 node를 한 번에 실행할 수 있다.

이번 실습에서는 `multisim.launch.py` 하나로 두 개의 turtlesim node를 동시에 시작하고, namespace가 서로 달라 node 이름이 충돌하지 않는 것을 확인했다.

## 발표/설명용 요약

이번 실습에서는 ROS 2 launch file을 사용해 여러 node를 한 번에 실행했다. Raspberry Pi에서 `turtlesim/multisim.launch.py`를 실행하고 `/turtlesim1/turtlesim`, `/turtlesim2/turtlesim` 두 node가 서로 다른 namespace로 시작되는 것을 확인했다. 이를 통해 복수 node 시스템을 launch file로 관리하는 기본 방식을 이해했다.
