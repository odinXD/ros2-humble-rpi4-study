# 2026-06-02 Custom Service / Client 실습 일지

## 실습 환경

- Device: Raspberry Pi 4B
- OS: Ubuntu 22.04.5 LTS
- Architecture: `aarch64`
- ROS Distribution: ROS 2 Humble
- Workspace: `~/ros2_ws`

## 실습 목적

`study_interfaces/srv/AddThreeInts` custom service를 `py_srvcli` package의 Python server와 client에서 사용한다.

Raspberry Pi에서 package 빌드, service 조회, CLI 요청, Python client 요청을 검증한다.

## 1. Package 의존성 추가

`src/py_srvcli/package.xml`에 다음 의존성을 추가했다.

```xml
<depend>study_interfaces</depend>
```

## 2. Custom Service Server 작성

`src/py_srvcli/py_srvcli/add_three_ints_server.py`를 작성했다.

Server는 `/py_add_three_ints` service를 생성하고 세 정수의 합계를 response로 반환한다.

```python
response.sum = request.a + request.b + request.c
```

## 3. Custom Service Client 작성

`src/py_srvcli/py_srvcli/add_three_ints_client.py`를 작성했다.

Client는 command line argument로 받은 세 정수를 request에 넣고 `/py_add_three_ints` service를 비동기로 호출한다.

## 4. Entry Point 추가

`src/py_srvcli/setup.py`에 실행 가능한 node를 등록했다.

```python
'three_ints_server = py_srvcli.add_three_ints_server:main',
'three_ints_client = py_srvcli.add_three_ints_client:main',
```

## 5. Raspberry Pi에서 빌드

```bash
cd ~/ros2_ws
./scripts/build.sh
source install/setup.bash
```

결과:

```text
Starting >>> study_interfaces
Starting >>> cpp_practice
Starting >>> cpp_srvcli
Finished <<< cpp_practice [1.11s]
Finished <<< cpp_srvcli [1.18s]
Finished <<< study_interfaces [2.99s]
Starting >>> py_practice
Starting >>> py_srvcli
Finished <<< py_practice [6.88s]
Finished <<< py_srvcli [6.96s]

Summary: 5 packages finished [11.2s]
Build completed.
```

## 6. Server 실행

```bash
ros2 run py_srvcli three_ints_server
```

결과:

```text
[py_add_three_ints_server]: Ready to add three ints.
[py_add_three_ints_server]: Request: 10 + 20 + 30 = 60
[py_add_three_ints_server]: Request: 7 + 8 + 9 = 24
```

## 7. Service 조회

```bash
source ~/ros2_ws/install/setup.bash
ros2 service list -t
ros2 service type /py_add_three_ints
```

결과:

```text
/py_add_three_ints [study_interfaces/srv/AddThreeInts]
study_interfaces/srv/AddThreeInts
```

## 8. CLI 요청

```bash
ros2 service call /py_add_three_ints study_interfaces/srv/AddThreeInts "{a: 10, b: 20, c: 30}"
```

결과:

```text
requester: making request: study_interfaces.srv.AddThreeInts_Request(a=10, b=20, c=30)

response:
study_interfaces.srv.AddThreeInts_Response(sum=60)
```

## 9. Python Client 요청

```bash
ros2 run py_srvcli three_ints_client 7 8 9
```

결과:

```text
[py_add_three_ints_client]: Sum: 24
```

## 확인한 내용

- `py_srvcli` package에서 `study_interfaces` 의존성을 사용할 수 있다.
- `AddThreeInts` custom service를 Python server와 client에서 사용할 수 있다.
- `/py_add_three_ints` service 타입은 `study_interfaces/srv/AddThreeInts`이다.
- CLI 요청 `10 + 20 + 30`의 응답은 `60`이다.
- Python client 요청 `7 + 8 + 9`의 응답은 `24`이다.
- Raspberry Pi에서 custom service 요청과 응답을 실제로 검증했다.

## 다음 실습

여러 node를 한 번에 실행할 수 있도록 간단한 bringup launch 구조를 구성한다.
