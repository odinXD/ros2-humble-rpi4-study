# 15. Custom Service / Client

## 학습 목표

직접 정의한 `study_interfaces/srv/AddThreeInts` service를 Python server와 client에서 사용한다.

Raspberry Pi 4B에서 package를 빌드하고, 세 정수를 요청으로 보내 합계를 응답으로 받는 과정을 확인한다.

## 핵심 개념

Topic은 publisher가 message를 계속 발행하고 subscriber가 이를 구독하는 통신 방식이다.

Service는 client가 요청을 보냈을 때 server가 한 번 응답하는 통신 방식이다.

이번 실습에서는 기존 `example_interfaces/srv/AddTwoInts` 대신 프로젝트에서 직접 정의한 `AddThreeInts` service를 사용했다.

```text
int64 a
int64 b
int64 c
---
int64 sum
```

`---` 위쪽은 client가 보내는 request이고, 아래쪽은 server가 돌려주는 response이다.

## Package 변경 사항

### `package.xml`

`py_srvcli` package가 `study_interfaces`를 사용할 수 있도록 의존성을 추가했다.

```xml
<depend>study_interfaces</depend>
```

### `setup.py`

새 Python node를 `ros2 run`으로 실행할 수 있도록 entry point를 추가했다.

```python
'three_ints_server = py_srvcli.add_three_ints_server:main',
'three_ints_client = py_srvcli.add_three_ints_client:main',
```

### Server

`three_ints_server`는 `/py_add_three_ints` service를 생성한다.

```python
self.service = self.create_service(
    AddThreeInts,
    'py_add_three_ints',
    self.add_callback,
)
```

Request를 받으면 세 정수의 합계를 response에 저장한다.

```python
response.sum = request.a + request.b + request.c
```

### Client

`three_ints_client`는 `/py_add_three_ints` service를 호출한다.

```python
self.client = self.create_client(
    AddThreeInts,
    'py_add_three_ints',
)
```

## 사용한 명령어

### Raspberry Pi에서 빌드

```bash
cd ~/ros2_ws
./scripts/build.sh
source install/setup.bash
```

### Server 실행

```bash
ros2 run py_srvcli three_ints_server
```

### Service 조회와 CLI 요청

```bash
source ~/ros2_ws/install/setup.bash
ros2 service list -t
ros2 service type /py_add_three_ints
ros2 service call /py_add_three_ints study_interfaces/srv/AddThreeInts "{a: 10, b: 20, c: 30}"
```

### Python Client 실행

```bash
ros2 run py_srvcli three_ints_client 7 8 9
```

## 실행 결과 요약

Raspberry Pi에서 다섯 package 빌드가 성공했다.

```text
Summary: 5 packages finished [11.2s]
Build completed.
```

Service 타입을 확인했다.

```text
/py_add_three_ints [study_interfaces/srv/AddThreeInts]
```

CLI에서 세 정수를 요청하고 합계를 응답으로 받았다.

```text
requester: making request: study_interfaces.srv.AddThreeInts_Request(a=10, b=20, c=30)

response:
study_interfaces.srv.AddThreeInts_Response(sum=60)
```

Python client에서도 응답을 확인했다.

```text
[py_add_three_ints_client]: Sum: 24
```

## 에러 및 해결

이번 실습에서는 별도로 기록할 구조적 오류가 발생하지 않았다.

## 정리

Custom service를 사용하면 프로젝트 목적에 맞는 request와 response 구조를 직접 설계할 수 있다.

이번 실습에서는 `AddThreeInts` service를 Python server와 client에 연결하고, Raspberry Pi에서 CLI 호출과 Python client 호출을 모두 검증했다.

## 발표/설명용 요약

이번 실습에서는 직접 정의한 `AddThreeInts` custom service를 Python server와 client에서 사용했다. Raspberry Pi에서 세 정수를 요청하고 합계를 응답으로 받는 과정을 CLI와 Python client로 확인했다. 이를 통해 프로젝트 목적에 맞는 service 요청과 응답 구조를 직접 설계하고 사용하는 방식을 이해했다.
