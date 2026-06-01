# AGENTS.md

## 1. 프로젝트 개요

이 저장소는 Raspberry Pi 4B에서 ROS 2 Humble을 학습하고, 공식 튜토리얼 실습 과정을 포트폴리오 형태로 정리하기 위한 프로젝트이다.

목표는 단순히 튜토리얼을 끝내는 것이 아니라, ROS 2의 핵심 개념을 이해하고, 실습 결과를 문서화하며, 이후 발표나 회의에서 진행 상황을 명확히 설명할 수 있는 자료를 축적하는 것이다.

이 프로젝트는 다음 목적을 가진다.

* ROS 2 Humble 입문
* ROS 2 공식 튜토리얼 실습
* Raspberry Pi 기반 ROS 실행 환경 이해
* ROS 2 node, topic, service, parameter, action, launch 개념 학습
* C++ / Python 기반 ROS 2 패키지 작성
* 학습 내용과 실습 결과를 GitHub 포트폴리오 형태로 정리
* 발표나 회의에서 설명 가능한 수준의 요약 자료 축적

---

## 2. 현재 개발 및 실행 환경

### 실제 ROS 실행 환경

* Target Device: Raspberry Pi 4B
* OS: Ubuntu Desktop 22.04 LTS 64-bit
* Architecture: aarch64
* ROS Distribution: ROS 2 Humble
* Workspace Path: `~/ros2_ws`
* Remote Access:

  * Tailscale
  * SSH
  * VSCode Remote SSH

### 보조 작업 환경

* Windows 개발 PC
* GitHub clone repository
* Codex CLI 사용
* 주 용도:

  * 문서 정리
  * 코드 초안 작성
  * README / AGENTS.md 관리
  * notes 작성
  * Git diff 검토
  * 다음 실습 계획 수립

---

## 3. 핵심 운영 원칙

이 프로젝트의 실제 ROS 2 빌드와 실행 검증은 반드시 Raspberry Pi에서 수행한다.

Windows 환경과 Codex는 문서 작성, 코드 초안 작성, 구조 설계, 정리 작업에 사용할 수 있지만, Windows에서 ROS 2 빌드나 실행 결과를 성공했다고 가정하면 안 된다.

Codex는 다음을 가정하지 않는다.

* `colcon build`가 성공했다는 것
* `ros2 run`이 성공했다는 것
* topic, service, action 통신이 정상 동작했다는 것
* Raspberry Pi에서 패키지가 실제로 실행 가능하다는 것

실제 성공 여부는 사용자가 Raspberry Pi 터미널 출력 또는 실행 결과를 제공했을 때만 확인된 것으로 본다.

---

## 4. 권장 작업 모드

이 프로젝트는 작업 종류에 따라 두 가지 모드로 진행한다.

### Mode A. Raspberry Pi 직접 실습 모드

ROS 2 코드 작성, 빌드, 실행, 튜토리얼 실습은 가능하면 Raspberry Pi에서 직접 진행한다.

권장 흐름:

1. Raspberry Pi에 SSH 또는 VSCode Remote SSH로 접속한다.
2. `~/ros2_ws`를 연다.
3. 필요한 파일을 직접 수정한다.
4. `./scripts/check_env.sh`로 환경을 확인한다.
5. `./scripts/build.sh` 또는 `colcon build --symlink-install`로 빌드한다.
6. `ros2 run`, `ros2 topic`, `ros2 service` 등으로 실제 실행을 확인한다.
7. 결과를 notes에 기록한다.
8. Git commit 후 push한다.

이 모드는 다음 작업에 우선 사용한다.

* ROS 2 패키지 생성
* C++ / Python publisher, subscriber 작성
* service/client 작성
* custom msg/srv 작성
* launch file 작성
* 실제 `ros2 run` 테스트
* Raspberry Pi 하드웨어와 연결되는 실습

### Mode B. Windows + Codex 보조 작업 모드

Windows의 clone repository에서 Codex를 사용하여 문서와 코드 초안을 정리한다.

권장 흐름:

1. Windows에서 repository를 연다.
2. Codex를 실행한다.
3. Codex가 AGENTS.md를 먼저 읽고 현재 프로젝트 상태를 파악한다.
4. 문서, README, notes, 코드 초안 등을 작성하거나 수정한다.
5. 실제 실행이 필요한 내용은 Raspberry Pi에서 검증해야 한다고 명시한다.
6. 변경 내용을 Git commit / push한다.
7. Raspberry Pi에서 pull 후 실제 테스트한다.

이 모드는 다음 작업에 적합하다.

* README 개선
* AGENTS.md 정리
* notes 초안 작성
* 발표용 설명 구조 정리
* 실습 결과 요약
* 코드 구조 설계
* 에러 로그 분석
* Git commit 단위 추천
* 다음 학습 계획 수립

---

## 5. Git 및 동기화 규칙

GitHub는 Windows와 Raspberry Pi 사이의 동기화 및 백업 중심으로 사용한다.

작업 시작 전에는 항상 현재 상태를 확인한다.

```bash
git status
git pull
```

작업 후에는 변경 내용을 확인하고 커밋한다.

```bash
git status
git diff
git add .
git commit -m "적절한 커밋 메시지"
git push
```

다른 장비에서 작업을 이어갈 때는 먼저 pull 한다.

```bash
git pull
```

동시에 Windows와 Raspberry Pi 양쪽에서 커밋되지 않은 변경을 만들지 않는다.
한쪽에서 작업 중이면 먼저 commit/push 한 뒤 다른 쪽에서 pull 한다.

---

## 6. 저장소 관리 정책

Git에 포함할 항목:

* `src/`
* `notes/`
* `archive/`
* `scripts/`
* `README.md`
* `AGENTS.md`
* `.gitignore`
* `.gitattributes`

Git에 포함하지 않을 항목:

* `build/`
* `install/`
* `log/`
* `logs/`
* cache 파일
* 임시 파일
* OS 또는 에디터 자동 생성 파일

`build/`, `install/`, `log/`는 colcon 빌드 결과물이므로 수정하거나 커밋하지 않는다.
`logs/`는 원본 터미널 출력처럼 부피가 큰 로컬 기록을 임시 보관하는 위치이므로 커밋하지 않는다.

---

## 7. 현재 완료된 상태

현재 완료된 작업은 다음과 같다.

* Raspberry Pi 4B에 Ubuntu Desktop 22.04 LTS 64-bit 설치
* Tailscale 원격 접속 구성
* SSH 접속 구성
* VSCode Remote SSH 구성
* ROS 2 Humble 설치
* rviz2 설치
* `demo_nodes_cpp`, `demo_nodes_py` 설치
* `talker` / `listener` pub-sub 테스트 성공
* `~/ros2_ws` 워크스페이스 생성
* Git 초기화
* GitHub remote 연결 및 push 성공
* `README.md` 작성
* `.gitignore` 작성
* `.gitattributes` 작성
* `AGENTS.md` 작성
* `notes/00_environment_setup.md` 작성
* `scripts/check_env.sh` 작성
* `scripts/build.sh` 작성
* Nodes / Topics CLI 실습
* `/talker`에서 `/chatter` topic 발행 확인
* `/listener`에서 `/chatter` topic 구독 확인
* Services CLI 실습
* `/add_two_ints` service 요청 및 응답 확인
* Parameters CLI 실습
* SSH 환경에서 `QT_QPA_PLATFORM=offscreen`을 사용한 `/turtlesim` headless 실행 확인
* `/turtlesim`의 `background_r` parameter 조회, 변경, dump 확인
* Actions CLI 실습
* `/turtle1/rotate_absolute` action goal, feedback, result 확인
* Launching nodes CLI 실습
* `turtlesim/multisim.launch.py`로 두 개의 namespaced node 실행 확인
* CMake 기반 `cpp_practice` package 생성
* Raspberry Pi에서 `cpp_practice` package 빌드 성공
* `ros2 run cpp_practice hello_node` 실행 확인
* `hello_node`를 `rclcpp` 기반 C++ publisher node로 확장
* `/hello_publisher`에서 `/practice_chatter` topic 발행 확인
* C++ `listener_node` subscriber 작성
* `/hello_subscriber`에서 `/practice_chatter` topic 수신 확인
* `ament_python` 기반 `py_practice` package 생성
* Python `/py_hello_publisher`에서 `/py_practice_chatter` topic 발행 확인
* Python `/py_hello_subscriber`에서 `/py_practice_chatter` topic 수신 확인
* C++ `cpp_srvcli` package 생성
* `/cpp_add_two_ints` service server와 client 요청 및 응답 확인

회의 로그 파일은 이 저장소에서 관리하지 않는다.
회의 자료나 발표 자료는 별도 위치에서 관리할 수 있으며, 이 저장소에는 ROS 2 학습과 실습에 직접 관련된 내용만 남긴다.

---

## 8. 학습 진행 순서

앞으로의 추천 학습 순서는 다음과 같다.

1. ROS 2 환경 확인
2. Nodes
3. Topics
4. Services
5. Parameters
6. Actions
7. Launch files
8. colcon workspace
9. package 생성
10. C++ publisher/subscriber 작성
11. Python publisher/subscriber 작성
12. C++ service/client 작성
13. Python service/client 작성
14. custom msg/srv 작성
15. 간단한 bringup 구조 구성
16. Raspberry Pi 기반 간단한 ROS 2 응용 프로젝트로 확장

각 단계는 다음 흐름으로 진행한다.

1. 개념 학습
2. 공식 튜토리얼 실습
3. Raspberry Pi에서 명령어 실행
4. 결과 확인
5. notes에 정리
6. Git commit
7. 필요 시 README 업데이트

---

## 9. notes 작성 규칙

학습 노트는 한국어로 작성한다.

각 노트는 가능한 한 다음 구조를 따른다.

```text
# 제목

## 학습 목표

## 핵심 개념

## 사용한 명령어

## 실행 결과 요약

## 에러 및 해결

## 정리

## 발표/설명용 요약
```

단, 모든 섹션을 억지로 채울 필요는 없다.
실습 성격에 맞게 필요한 항목만 사용한다.

공식 문서를 그대로 복사하지 말고, 사용자가 이해한 방식으로 재정리한다.

설명은 다음 기준을 따른다.

* 처음 배우는 사람도 이해할 수 있게 작성한다.
* ROS 2 용어는 가능한 한 쉬운 비유와 함께 설명한다.
* 명령어는 왜 쓰는지 함께 설명한다.
* 실습 결과는 실제 Raspberry Pi에서 확인한 결과만 적는다.
* 추측이 필요한 내용은 추측이라고 명시한다.

`notes/progress.md`에는 현재 완료한 실습, Raspberry Pi에서 검증된 결과, 다음 작업을 간단히 기록한다.
Codex는 다음 작업을 시작할 때 이 파일을 먼저 확인한다.

상세한 실습 순서와 의미 있는 터미널 출력은 `archive/`에 날짜별 실습 일지로 기록한다.
원본 터미널 출력 전체를 보관해야 할 때는 Git에 포함되지 않는 `logs/`를 사용한다.
단순 오타나 일회성 입력 실수는 기록하지 않는다.
다시 발생할 수 있는 환경 문제, 설정 오류, 구조적 원인과 해결 방법만 기록한다.

---

## 10. 발표 및 보고 준비 규칙

이 저장소는 포트폴리오 성격도 가지므로, 각 주요 학습 단계마다 발표나 설명에 활용할 수 있는 요약을 남긴다.

notes의 마지막에는 가능하면 다음 형식의 짧은 요약을 포함한다.

```text
발표/설명용 요약:
이번 실습에서는 ROS 2의 [개념]을 학습했고, Raspberry Pi에서 [명령/패키지]를 실행하여 [결과]를 확인했다. 이를 통해 [의미]를 이해했다.
```

Codex는 사용자가 요청하면 다음을 능동적으로 제안한다.

* 현재까지의 진행 상황 요약
* 발표용 1분 설명
* 발표용 3분 설명
* 회의 보고용 bullet 요약
* README에 넣을 포트폴리오 문장
* 다음 학습 단계 제안

단, 회의 전용 로그 파일은 이 저장소에 만들지 않는다.

---

## 11. scripts 사용 규칙

현재 제공되는 스크립트:

```bash
./scripts/check_env.sh
./scripts/build.sh
```

### check_env.sh

ROS 2 환경, colcon, 시스템 상태, Git 상태를 빠르게 확인하는 스크립트이다.

사용:

```bash
./scripts/check_env.sh
```

### build.sh

ROS 2 Humble 환경을 source한 뒤 `colcon build --symlink-install`을 실행하는 스크립트이다.

사용:

```bash
./scripts/build.sh
```

Codex가 스크립트를 수정할 경우, 실제 실행 가능 여부는 Raspberry Pi에서 확인해야 한다.

`.sh` 파일은 LF 줄바꿈을 유지해야 한다.
Windows에서 수정할 경우 `.gitattributes` 규칙을 유지한다.

---

## 12. Codex 작업 규칙

Codex는 작업 전 다음을 확인한다.

1. `AGENTS.md`
2. `README.md`
3. `notes/progress.md`
4. 관련 notes
5. 관련 archive
6. 관련 scripts
7. `src/` 구조

Codex는 파일 수정 전 가능하면 먼저 계획을 제시한다.

Codex는 다음 상황에서 사용자 확인을 받는다.

* 여러 파일을 동시에 크게 수정할 때
* 기존 구조를 바꾸려 할 때
* Git 기록에 영향을 주는 작업을 제안할 때
* Raspberry Pi에서 테스트가 필요한 코드를 작성할 때
* 공식 튜토리얼 흐름을 벗어난 확장 작업을 제안할 때

Codex는 다음을 하지 않는다.

* Raspberry Pi 실행 결과를 임의로 가정하지 않는다.
* `build/`, `install/`, `log/`를 수정하지 않는다.
* 검증되지 않은 코드를 성공했다고 문서화하지 않는다.
* 회의 로그 파일을 새로 만들지 않는다.
* 불필요하게 복잡한 구조를 먼저 만들지 않는다.

---

## 13. Git commit 메시지 규칙

작고 의미 있는 단위로 커밋한다.

권장 형식:

```text
docs: 문서 변경
scripts: 스크립트 변경
feat: 기능 또는 예제 코드 추가
fix: 오류 수정
chore: 설정 또는 정리 작업
```

예시:

```text
docs: summarize ROS 2 nodes and topics
docs: update environment setup notes
scripts: add environment check script
scripts: add workspace build script
feat: add simple C++ publisher
feat: add simple Python subscriber
fix: correct ROS environment setup command
chore: add line ending rules
```

---

## 14. 다음 작업 후보

현재 다음으로 진행할 작업은 다음과 같다.

1. Python service/client 작성
2. `ament_python` 기반 `py_srvcli` package 생성
3. `example_interfaces/srv/AddTwoInts` 기반 service server 작성
4. service client 작성
5. Raspberry Pi에서 package 빌드
6. server와 client를 각각 실행
7. 요청값과 응답 결과 확인
8. Git commit / push

Raspberry Pi에서 사용할 기본 실습 명령어 예시는 다음과 같다.

```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python --license Apache-2.0 py_srvcli --dependencies rclpy example_interfaces
```

다른 터미널에서:

```bash
cd ~/ros2_ws
./scripts/build.sh
source install/setup.bash
```

실행 결과를 바탕으로 notes를 작성한다.

---

## 15. 최종 운영 요약

이 프로젝트는 다음 구조로 운영한다.

```text
Windows + Codex:
문서 정리, 코드 초안, 계획 수립, 발표용 요약, GitHub 작업 보조

Raspberry Pi:
실제 ROS 2 빌드, 실행, 테스트, 튜토리얼 실습

GitHub:
Windows와 Raspberry Pi 사이의 동기화, 백업, 포트폴리오 관리

notes:
학습 내용과 실습 결과 정리

archive:
상세한 실습 순서와 의미 있는 터미널 출력 기록

logs:
Git에 포함하지 않는 원본 터미널 출력 임시 보관

README:
외부에 보여줄 프로젝트 소개

AGENTS.md:
Codex가 따라야 할 작업 규칙
```

핵심 원칙은 다음과 같다.

실제 ROS 2 결과는 Raspberry Pi에서 확인한다.
Codex는 이를 돕는 보조 도구로 사용한다.
GitHub는 작업 단위가 끝났을 때 동기화와 백업을 위해 사용한다.
