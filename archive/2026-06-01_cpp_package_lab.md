# 2026-06-01 첫 C++ Package 생성 실습 일지

## 실습 환경

- Device: Raspberry Pi 4B
- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `~/ros2_ws`

## 실습 목적

`~/ros2_ws/src`에 첫 CMake 기반 ROS 2 package를 생성한다.

생성된 파일 구조를 확인하고, Raspberry Pi에서 실제로 빌드한 뒤 `ros2 run`으로 실행 파일을 실행한다.

## 1. Workspace 구조 확인

```bash
cd ~/ros2_ws
ls
```

결과:

```text
AGENTS.md  archive  build  install  log  notes  README.md  scripts  src
```

`src` 디렉터리는 이미 존재했다.

```bash
mkdir -p src
cd src
ls
```

이 시점에는 `src`가 비어 있었다.

## 2. Package 생성

```bash
ros2 pkg create --build-type ament_cmake --license Apache-2.0 --node-name hello_node cpp_practice
```

주요 결과:

```text
package name: cpp_practice
destination directory: /home/doyeong/ros2_ws/src
package format: 3
version: 0.0.0
licenses: ['Apache-2.0']
build type: ament_cmake
dependencies: []
node_name: hello_node
```

생성된 파일:

```text
creating folder ./cpp_practice
creating ./cpp_practice/package.xml
creating source and include folder
creating folder ./cpp_practice/src
creating folder ./cpp_practice/include/cpp_practice
creating ./cpp_practice/CMakeLists.txt
creating ./cpp_practice/src/hello_node.cpp
```

## 3. Package 구조 확인

```bash
cd ~/ros2_ws/src/cpp_practice
ls
```

결과:

```text
CMakeLists.txt  include  LICENSE  package.xml  src
```

## 4. 생성된 Source Code 확인

```bash
cd ~/ros2_ws
sed -n '1,160p' src/cpp_practice/src/hello_node.cpp
```

결과:

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

이 코드는 문자열을 출력하고 종료하는 기본 C++ 실행 파일이다.

이름은 `hello_node`지만 아직 `rclcpp`를 초기화하거나 ROS graph에 node를 등록하지 않는다.

## 5. CMake 설정 확인

```bash
sed -n '1,200p' src/cpp_practice/CMakeLists.txt
```

주요 부분:

```cmake
find_package(ament_cmake REQUIRED)

add_executable(hello_node src/hello_node.cpp)

install(TARGETS hello_node
  DESTINATION lib/${PROJECT_NAME})
```

`ament_cmake`를 사용하고, `hello_node.cpp`를 빌드하여 package 실행 파일로 설치하도록 설정되어 있다.

## 6. Raspberry Pi에서 빌드

```bash
cd ~/ros2_ws
./scripts/build.sh
```

결과:

```text
Starting >>> cpp_practice
Finished <<< cpp_practice [6.51s]

Summary: 1 package finished [8.32s]
Build completed.
```

이전에 package가 없을 때는 `0 packages finished`였지만, 이제 `cpp_practice` 1개가 빌드됐다.

## 7. Workspace 환경 Source

```bash
source install/setup.bash
```

빌드 후 workspace의 설치 결과를 현재 shell에서 사용할 수 있도록 불러왔다.

## 8. 실행 파일 확인

```bash
ros2 run cpp_practice hello_node
```

결과:

```text
hello world cpp_practice package
```

## 9. Git 상태 확인

```bash
git status --short
```

결과:

```text
?? src/
```

생성된 source package를 Git에 추가하고 commit, push했다.

Windows 저장소에서도 pull 후 fast-forward 동기화를 확인했다.

```text
8400bd8 feat: add initial C++ practice package
```

## 확인한 내용

- ROS 2 source package는 workspace의 `src/` 아래에 둔다.
- `ros2 pkg create`로 package 기본 구조를 만들 수 있다.
- `--build-type ament_cmake`는 CMake 기반 C++ package를 생성한다.
- `--node-name hello_node`는 기본 C++ 실행 파일을 함께 생성한다.
- `./scripts/build.sh`를 실행하자 Raspberry Pi에서 `cpp_practice` 빌드가 성공했다.
- `source install/setup.bash` 후 `ros2 run cpp_practice hello_node`를 실행할 수 있었다.
- 현재 `hello_node`는 ROS graph node가 아니라 문자열을 출력하고 종료하는 초기 실행 파일이다.

## 다음 실습

`hello_node.cpp`를 실제 ROS 2 publisher node로 확장한다.

이를 위해 `rclcpp`와 `std_msgs` 의존성을 추가하고 topic 발행 결과를 Raspberry Pi에서 검증한다.
