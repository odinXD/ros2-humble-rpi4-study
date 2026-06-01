# 2026-06-01 Python Service와 Client 실습 일지

## 실습 환경

- Device: Raspberry Pi 4B
- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `~/ros2_ws`

## 실습 목적

`ament_python` 기반 `py_srvcli` package를 만들고 `AddTwoInts` 타입의 service server와 client를 작성한다.

Raspberry Pi에서 CLI 요청과 Python client 요청을 각각 실행한다.

## 1. Package 생성

```bash
cd ~/ros2_ws/src
ros2 pkg create \
  --build-type ament_python \
  --license Apache-2.0 \
  py_srvcli \
  --dependencies rclpy example_interfaces
```

주요 결과:

```text
package name: py_srvcli
destination directory: /home/doyeong/ros2_ws/src
package format: 3
build type: ament_python
dependencies: ['rclpy', 'example_interfaces']
```

## 2. Server Source 작성

`src/py_srvcli/py_srvcli/add_two_ints_server.py`를 작성했다.

```python
def add_callback(self, request, response):
    response.sum = request.a + request.b
    return response
```

## 3. Server 실행 설정

`setup.py`에 server console script를 등록했다.

```python
'server = py_srvcli.add_two_ints_server:main',
```

## 4. Server 빌드와 실행

```bash
cd ~/ros2_ws
./scripts/build.sh
source install/setup.bash
ros2 run py_srvcli server
```

결과:

```text
Summary: 4 packages finished [23.7s]
Build completed.

[py_add_two_ints_server]: Ready to add two ints.
```

## 5. CLI에서 Service 확인

```bash
source ~/ros2_ws/install/setup.bash
ros2 service list -t
ros2 service type /py_add_two_ints
```

주요 결과:

```text
/py_add_two_ints [example_interfaces/srv/AddTwoInts]
example_interfaces/srv/AddTwoInts
```

## 6. CLI에서 Service 호출

```bash
ros2 service call /py_add_two_ints example_interfaces/srv/AddTwoInts "{a: 30, b: 40}"
```

결과:

```text
requester: making request: example_interfaces.srv.AddTwoInts_Request(a=30, b=40)

response:
example_interfaces.srv.AddTwoInts_Response(sum=70)
```

Server 로그:

```text
[py_add_two_ints_server]: Request: 30 + 40 = 70
```

## 7. Client Source 작성

`src/py_srvcli/py_srvcli/add_two_ints_client.py`를 작성했다.

```python
def send_request(self, a, b):
    request = AddTwoInts.Request()
    request.a = a
    request.b = b
    return self.client.call_async(request)
```

## 8. Client 실행 설정

`setup.py`에 client console script를 등록했다.

```python
'client = py_srvcli.add_two_ints_client:main',
```

## 9. Client 추가 후 Raspberry Pi 빌드

```bash
cd ~/ros2_ws
./scripts/build.sh
```

결과:

```text
Starting >>> cpp_practice
Starting >>> cpp_srvcli
Starting >>> py_practice
Starting >>> py_srvcli
Finished <<< cpp_srvcli [2.96s]
Finished <<< cpp_practice [3.08s]
Finished <<< py_practice [7.09s]
Finished <<< py_srvcli [7.40s]

Summary: 4 packages finished [8.73s]
Build completed.
```

## 10. Python Client 실행

```bash
source install/setup.bash
ros2 run py_srvcli client 9 6
```

Client 결과:

```text
[py_add_two_ints_client]: Sum: 15
```

Server 결과:

```text
[py_add_two_ints_server]: Request: 9 + 6 = 15
```

## 11. Git 동기화

빌드와 실행 검증 후 source를 commit, push했다.

```text
06c049b feat: add Python service and client
```

Windows 저장소에서도 pull 후 최신 source를 확인했다.

## 확인한 내용

- Python service server는 `create_service()`로 만들 수 있다.
- Server callback은 요청을 처리하고 응답 객체를 반환한다.
- Python service client는 `create_client()`로 만들 수 있다.
- `call_async()`로 비동기 요청을 보낼 수 있다.
- `rclpy.spin_until_future_complete()`로 응답 완료까지 기다릴 수 있다.
- Raspberry Pi에서 CLI 요청과 Python client 요청을 모두 검증했다.

## 다음 실습

Custom msg/srv interface package를 작성한다.
