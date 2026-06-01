# 03. ROS 2 Parameters

## 학습 목표

Raspberry Pi 4B에서 `/turtlesim` node를 실행하고, parameter 목록 조회, 값 확인, 값 변경, 전체 설정 dump를 실습한다.

SSH 환경에서 GUI 프로그램을 실행할 때 발생할 수 있는 Qt display 오류를 확인하고, 화면 없이 node를 실행하는 방법도 익힌다.

## 핵심 개념

Parameter는 node의 동작을 조절하는 설정값이다.

코드를 수정하지 않고 CLI에서 parameter를 조회하거나 변경할 수 있다. 이번 실습에서는 `/turtlesim` node의 배경색 설정을 사용했다.

- `background_r`: 빨간색 값
- `background_g`: 초록색 값
- `background_b`: 파란색 값

## 사용한 명령어

### turtlesim 설치 여부 확인

```bash
ros2 pkg executables turtlesim
```

### SSH 환경에서 turtlesim headless 실행

```bash
source /opt/ros/humble/setup.bash
QT_QPA_PLATFORM=offscreen ros2 run turtlesim turtlesim_node
```

### Parameter 확인과 변경

```bash
source /opt/ros/humble/setup.bash
ros2 node list
ros2 param list /turtlesim
ros2 param get /turtlesim background_g
ros2 param set /turtlesim background_r 150
ros2 param dump /turtlesim
ros2 param set /turtlesim background_r 69
```

## 실행 결과 요약

Raspberry Pi 4B에 `turtlesim` 패키지가 설치되어 있는 것을 확인했다.

```text
turtlesim draw_square
turtlesim mimic
turtlesim turtle_teleop_key
turtlesim turtlesim_node
```

일반 실행은 SSH 환경에서 display에 연결할 수 없어 실패했다.

```text
qt.qpa.xcb: could not connect to display
qt.qpa.plugin: Could not load the Qt platform plugin "xcb"
```

`QT_QPA_PLATFORM=offscreen`을 지정하자 창 없이 `/turtlesim` node가 정상 실행됐다.

```text
[turtlesim]: Starting turtlesim with node name /turtlesim
[turtlesim]: Spawning turtle [turtle1] at x=[5.544445], y=[5.544445], theta=[0.000000]
```

Parameter 목록을 확인했다.

```text
background_b
background_g
background_r
qos_overrides./parameter_events.publisher.depth
qos_overrides./parameter_events.publisher.durability
qos_overrides./parameter_events.publisher.history
qos_overrides./parameter_events.publisher.reliability
use_sim_time
```

`background_g`의 값은 `86`이었다.

```text
Integer value is: 86
```

`background_r`을 `150`으로 변경하고 전체 설정을 dump했다.

```text
Set parameter successful
```

```text
/turtlesim:
  ros__parameters:
    background_b: 255
    background_g: 86
    background_r: 150
    use_sim_time: false
```

마지막으로 `background_r`을 기존 값 `69`로 복원했다.

```text
Set parameter successful
```

## 에러 및 해결

### SSH 터미널에서 turtlesim GUI 실행 실패

SSH 터미널에서 일반 실행 명령을 사용하자 Qt가 display에 연결하지 못했다.

```bash
ros2 run turtlesim turtlesim_node
```

이 문제는 ROS 2 패키지 재설치가 필요한 오류가 아니라, SSH 환경에서 GUI를 표시할 display 연결이 없어서 발생한 문제이다.

CLI 기반 parameter 실습을 이어가기 위해 Qt의 offscreen 플랫폼을 지정했다.

```bash
QT_QPA_PLATFORM=offscreen ros2 run turtlesim turtlesim_node
```

화면은 표시되지 않지만 `/turtlesim` node와 parameter 기능은 정상 동작했다.

## 정리

Parameter를 사용하면 node의 설정값을 실행 중에 확인하고 변경할 수 있다.

이번 실습에서는 `/turtlesim`의 배경색 parameter를 조회하고 변경한 뒤 원래 값으로 복원했다. SSH 환경에서는 GUI를 직접 볼 수 없었지만, `param set` 결과와 `param dump` 출력으로 변경이 적용됐음을 검증했다.

## 발표/설명용 요약

이번 실습에서는 ROS 2 parameter를 학습했다. Raspberry Pi의 SSH 환경에서 `/turtlesim`을 headless 모드로 실행하고, 배경색 parameter를 조회, 변경, dump, 복원했다. 이를 통해 parameter가 node의 동작 설정을 코드 수정 없이 조절하는 기능임을 확인했다.
