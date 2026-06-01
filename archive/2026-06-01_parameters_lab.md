# 2026-06-01 Parameters 실습 일지

## 실습 환경

- Device: Raspberry Pi 4B
- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `~/ros2_ws`
- Access: SSH terminal

## 실습 목적

`/turtlesim` node의 parameter 목록, 값 조회, 값 변경, dump를 확인한다.

SSH 환경에서 GUI 프로그램을 실행할 때 발생한 Qt display 오류를 해결하고, 화면이 없는 환경에서도 CLI 실습을 이어가는 방법을 기록한다.

## 1. turtlesim 설치 여부 확인

```bash
ros2 pkg executables turtlesim
```

결과:

```text
turtlesim draw_square
turtlesim mimic
turtlesim turtle_teleop_key
turtlesim turtlesim_node
```

`turtlesim_node`를 포함한 실행 파일이 설치되어 있음을 확인했다.

## 2. 일반 GUI 실행 시도

```bash
ros2 run turtlesim turtlesim_node
```

결과:

```text
qt.qpa.xcb: could not connect to display
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized.

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, xcb.

[ros2run]: Aborted
```

SSH 터미널에는 GUI 창을 표시할 display 연결이 없으므로 Qt 기반 프로그램이 시작되지 못했다.

Qt plugin이 없어서 발생한 문제가 아니므로 재설치하지 않고 headless 모드로 실행하기로 했다.

## 3. Offscreen 모드로 turtlesim 실행

```bash
source /opt/ros/humble/setup.bash
QT_QPA_PLATFORM=offscreen ros2 run turtlesim turtlesim_node
```

결과:

```text
[turtlesim]: Starting turtlesim with node name /turtlesim
[turtlesim]: Spawning turtle [turtle1] at x=[5.544445], y=[5.544445], theta=[0.000000]
```

GUI 창은 표시되지 않지만 node는 종료되지 않고 정상적으로 실행됐다.

## 4. Node 확인

다른 터미널에서 ROS 2 환경을 불러오고 실행 중인 node를 확인했다.

```bash
source /opt/ros/humble/setup.bash
ros2 node list
```

결과:

```text
/turtlesim
```

## 5. Parameter 목록 확인

```bash
ros2 param list /turtlesim
```

결과:

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

배경색 설정과 ROS 2 기본 parameter 관련 설정을 확인했다.

## 6. Parameter 값 조회

```bash
ros2 param get /turtlesim background_g
```

결과:

```text
Integer value is: 86
```

## 7. Parameter 값 변경

```bash
ros2 param set /turtlesim background_r 150
```

결과:

```text
Set parameter successful
```

SSH headless 환경이므로 실제 창의 배경색 변화는 눈으로 확인하지 못했다.

## 8. Parameter dump 확인

```bash
ros2 param dump /turtlesim
```

결과:

```text
/turtlesim:
  ros__parameters:
    background_b: 255
    background_g: 86
    background_r: 150
    qos_overrides:
      /parameter_events:
        publisher:
          depth: 1000
          durability: volatile
          history: keep_last
          reliability: reliable
    use_sim_time: false
```

`background_r`이 `150`으로 변경된 것을 CLI 출력으로 검증했다.

## 9. Parameter 원래 값으로 복원

```bash
ros2 param set /turtlesim background_r 69
```

결과:

```text
Set parameter successful
```

## 확인한 내용

- Parameter는 node의 동작을 조절하는 설정값이다.
- `/turtlesim`에는 배경색을 제어하는 `background_r`, `background_g`, `background_b` parameter가 있다.
- `ros2 param get`으로 값을 조회할 수 있다.
- `ros2 param set`으로 실행 중인 node의 값을 변경할 수 있다.
- `ros2 param dump`로 node의 parameter를 YAML 형태로 확인할 수 있다.
- SSH 환경에서 Qt GUI 실행이 실패하면 `QT_QPA_PLATFORM=offscreen`을 사용해 CLI 실습을 이어갈 수 있다.

## 다음 실습

Actions CLI 실습을 진행한다.

SSH 환경이므로 `/turtlesim`은 offscreen 모드로 실행하고, action의 실행 결과는 CLI의 feedback과 result로 확인한다.

```bash
QT_QPA_PLATFORM=offscreen ros2 run turtlesim turtlesim_node
```
