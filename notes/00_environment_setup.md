# 00. ROS 2 Environment Setup

## 목표

Raspberry Pi 4B에 Ubuntu Desktop 22.04 LTS 64-bit와 ROS 2 Humble을 설치하고, 원격 개발 환경과 기본 ROS 2 통신 테스트를 완료한다.

## 사용 환경

- Board: Raspberry Pi 4B
- OS: Ubuntu Desktop 22.04 LTS 64-bit
- ROS: ROS 2 Humble
- Workspace: `~/ros2_ws`
- Remote:
  - Tailscale
  - SSH
  - VSCode Remote / VSCode Server

## 완료한 작업

### 1. 원격 접속 환경 구성

Tailscale을 통해 라즈베리파이에 원격 접속할 수 있도록 구성했다.

SSH 접속을 확인했고, VSCode Remote 환경을 통해 라즈베리파이 내부의 `~/ros2_ws`를 편집할 수 있도록 세팅했다.

### 2. ROS 2 Humble 설치

Ubuntu 22.04 환경에서 ROS 2 Humble을 설치했다.

설치 후 ROS 환경을 불러오기 위해 `.bashrc`에 다음 설정을 추가했다.

```bash
source /opt/ros/humble/setup.bash

if [ -f ~/ros2_ws/install/setup.bash ]; then
  source ~/ros2_ws/install/setup.bash
fi
```

### 3. 기본 통신 테스트

ROS 2의 기본 pub/sub 예제인 talker/listener를 실행했다.

Terminal 1:

```bash
ros2 run demo_nodes_cpp talker
```

Terminal 2:

```bash
ros2 run demo_nodes_py listener
```

listener에서 talker가 publish한 `Hello World` 메시지를 정상적으로 수신하는 것을 확인했다.

## 확인한 개념

ROS 2에서는 하나의 프로그램 단위를 Node라고 부른다.

Node는 Topic을 통해 메시지를 publish하거나 subscribe할 수 있다.

이번 테스트에서 `talker`는 메시지를 publish하는 node이고, `listener`는 해당 메시지를 subscribe하는 node이다.

## 현재 상태

ROS 2 Humble 설치와 기본 pub/sub 테스트는 완료되었다.

다음 단계에서는 공식 튜토리얼을 따라가며 node, topic, service, parameter, action 등의 개념을 정리할 예정이다.

## 회의용 요약

Raspberry Pi 4B에 ROS 2 Humble 개발 환경을 구축했다. Tailscale, SSH, VSCode Remote를 통해 원격 개발 환경을 마련했고, ROS 2 기본 예제인 talker/listener를 실행하여 pub/sub 통신이 정상적으로 동작하는 것을 확인했다. 다음 단계에서는 공식 튜토리얼을 기반으로 ROS 2의 핵심 개념인 node, topic, service, action을 순차적으로 학습하고 실습 내용을 Git으로 정리할 예정이다.
