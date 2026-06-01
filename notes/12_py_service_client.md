# 12. Python Service와 Client 작성

## 학습 목표

`ament_python` 기반 package에 service server와 client를 작성한다.

Raspberry Pi 4B에서 두 정수를 전달하고 합계를 응답받는 흐름을 검증한다.

## 핵심 개념

Python ROS 2 service도 C++과 동일하게 요청과 응답 구조를 사용한다.

이번 실습에서는 `example_interfaces/srv/AddTwoInts` 타입을 Python server와 client에 적용했다.

- Package: `py_srvcli`
- Server Node: `/py_add_two_ints_server`
- Client Node: `/py_add_two_ints_client`
- Service: `/py_add_two_ints`
- Service Type: `example_interfaces/srv/AddTwoInts`

## Package 구조

```text
src/py_srvcli/
├── package.xml
├── setup.cfg
├── setup.py
└── py_srvcli/
    ├── __init__.py
    ├── add_two_ints_server.py
    └── add_two_ints_client.py
```

## 변경한 파일

### `package.xml`

```xml
<depend>rclpy</depend>
<depend>example_interfaces</depend>
```

### `py_srvcli/add_two_ints_server.py`

Server는 요청의 `a`, `b`를 더하고 응답의 `sum`에 저장한다.

```python
def add_callback(self, request, response):
    response.sum = request.a + request.b
    return response
```

### `py_srvcli/add_two_ints_client.py`

Client는 service를 찾은 뒤 비동기 요청을 보낸다.

```python
request = AddTwoInts.Request()
request.a = a
request.b = b
return self.client.call_async(request)
```

### `setup.py`

```python
'console_scripts': [
    'server = py_srvcli.add_two_ints_server:main',
    'client = py_srvcli.add_two_ints_client:main',
],
```

## 사용한 명령어

### Package 생성

```bash
cd ~/ros2_ws/src
ros2 pkg create \
  --build-type ament_python \
  --license Apache-2.0 \
  py_srvcli \
  --dependencies rclpy example_interfaces
```

### Raspberry Pi에서 빌드와 Server 실행

```bash
cd ~/ros2_ws
./scripts/build.sh
source install/setup.bash
ros2 run py_srvcli server
```

### CLI에서 Service 확인과 호출

```bash
source ~/ros2_ws/install/setup.bash
ros2 service list -t
ros2 service type /py_add_two_ints
ros2 service call /py_add_two_ints example_interfaces/srv/AddTwoInts "{a: 30, b: 40}"
```

### Python Client 실행

```bash
source ~/ros2_ws/install/setup.bash
ros2 run py_srvcli client 9 6
```

## 실행 결과 요약

Raspberry Pi에서 네 package 빌드가 성공했다.

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

Server가 요청을 기다리는 상태로 실행됐다.

```text
[py_add_two_ints_server]: Ready to add two ints.
```

CLI로 `30`, `40`을 요청하자 `70`이 응답으로 돌아왔다.

```text
requester: making request: example_interfaces.srv.AddTwoInts_Request(a=30, b=40)

response:
example_interfaces.srv.AddTwoInts_Response(sum=70)
```

Python client로 `9`, `6`을 요청하자 `15`가 응답으로 돌아왔다.

```text
[py_add_two_ints_client]: Sum: 15
```

Server에서도 처리된 요청을 확인했다.

```text
[py_add_two_ints_server]: Request: 9 + 6 = 15
```

## 에러 및 해결

이번 실습에서는 별도로 기록할 구조적 오류가 발생하지 않았다.

## 정리

Python에서도 `create_service()`와 `create_client()`를 사용해 service server와 client를 작성할 수 있다.

이번 실습에서는 CLI와 직접 작성한 Python client 두 방식으로 `/py_add_two_ints` service를 검증했다.

## 발표/설명용 요약

이번 실습에서는 Python ROS 2 service server와 client를 작성했다. Raspberry Pi에서 `/py_add_two_ints` service에 두 정수를 전달하고 합계를 응답받았다. C++과 Python 모두 같은 요청 및 응답 구조를 사용한다는 점을 확인했다.
