# 06. 첫 C++ ROS 2 Package 생성

## 학습 목표

Raspberry Pi 4B의 `~/ros2_ws/src`에 CMake 기반 ROS 2 package를 생성하고, package 구조를 확인한다.

생성된 package를 `colcon`으로 빌드하고 실행 파일을 실행하여 workspace 개발 흐름을 검증한다.

## 핵심 개념

ROS 2 package는 관련 source code, 의존성, 빌드 설정을 묶어 관리하는 단위이다.

이번 실습에서는 `ament_cmake` 빌드 타입의 `cpp_practice` package를 생성했다.

```text
src/cpp_practice/
├── CMakeLists.txt
├── LICENSE
├── package.xml
├── include/cpp_practice/
└── src/hello_node.cpp
```

주요 파일의 역할:

- `package.xml`: package 이름, 버전, 라이선스, 의존성 등 메타데이터
- `CMakeLists.txt`: C++ 실행 파일의 빌드 및 설치 방법
- `src/hello_node.cpp`: 실행할 C++ source code
- `include/cpp_practice/`: package의 header file 위치

## 사용한 명령어

### Package 생성

```bash
cd ~/ros2_ws
mkdir -p src
cd src
ros2 pkg create --build-type ament_cmake --license Apache-2.0 --node-name hello_node cpp_practice
```

### 구조와 생성된 코드 확인

```bash
cd ~/ros2_ws
sed -n '1,160p' src/cpp_practice/src/hello_node.cpp
sed -n '1,200p' src/cpp_practice/CMakeLists.txt
```

### Raspberry Pi에서 빌드와 실행

```bash
cd ~/ros2_ws
./scripts/build.sh
source install/setup.bash
ros2 run cpp_practice hello_node
```

## 실행 결과 요약

`cpp_practice` package가 정상적으로 생성됐다.

```text
creating folder ./cpp_practice
creating ./cpp_practice/package.xml
creating folder ./cpp_practice/src
creating folder ./cpp_practice/include/cpp_practice
creating ./cpp_practice/CMakeLists.txt
creating ./cpp_practice/src/hello_node.cpp
```

Raspberry Pi에서 빌드가 성공했다.

```text
Starting >>> cpp_practice
Finished <<< cpp_practice [6.51s]

Summary: 1 package finished [8.32s]
Build completed.
```

생성된 실행 파일을 실행하자 문자열이 출력됐다.

```text
hello world cpp_practice package
```

## 현재 코드의 범위

생성된 `hello_node.cpp`는 다음과 같이 문자열을 출력하고 종료한다.

```cpp
#include <cstdio>

int main(int argc, char ** argv)
{
  (void) argc;
  (void) argv;

  printf("hello world cpp_practice package\n");
  return 0;
}
```

실행 파일 이름은 `hello_node`지만 아직 ROS graph에 등록되는 `rclcpp` 기반 node는 아니다.

다음 실습에서 `rclcpp`와 `std_msgs`를 추가하고 실제 ROS 2 publisher node로 확장한다.

## 에러 및 해결

이번 실습에서는 별도의 에러가 발생하지 않았다.

## 정리

처음에는 사용자 작성 package가 없어 빌드 결과가 `0 packages finished`였다.

`cpp_practice`를 생성한 뒤 Raspberry Pi에서 다시 빌드하자 `1 package finished`가 출력됐고, 설치된 실행 파일도 `ros2 run`으로 정상 실행됐다.

## 발표/설명용 요약

이번 실습에서는 Raspberry Pi의 ROS 2 workspace에 첫 C++ package를 생성했다. `ament_cmake` 기반 `cpp_practice` package를 만든 뒤 `colcon` 빌드와 `ros2 run` 실행에 성공했다. 이를 통해 source package가 workspace에서 빌드되고 설치된 실행 파일로 실행되는 기본 흐름을 확인했다.
