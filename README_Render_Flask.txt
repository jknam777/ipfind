# Render Flask Starter (무료 배포용)

이 저장소는 Flask 앱을 **Render 무료 플랜**에 바로 배포하기 위한 최소 구성입니다.

## 포함 파일
- `app.py` — Flask 앱 (/ /ip /health)
- `requirements.txt` — Flask, gunicorn, requests
- `Procfile` — Render에서 gunicorn으로 서비스 실행
- `render.yaml` — Render 인프라 정의(웹 서비스)

## 배포 방법 (GitHub → Render)
1. GitHub에 새 저장소 생성 → 이 4개 파일을 업로드(commit)
2. https://render.com → **New +** → **Blueprint** 선택 → GitHub 저장소 연결
3. 화면에서 `render.yaml` 읽혀지면 설정을 확인하고 **Create Resources** 클릭
4. 빌드 후 **Live URL** 로 접속 → `/health` 200 OK 확인 → `/ip` 테스트

## 로컬 테스트
```
pip install -r requirements.txt
python app.py
# http://127.0.0.1:5000
```

## 자주 묻는 질문
- **무료 플랜 슬립**: 장시간 미사용 시 슬립될 수 있으며, 최초 접속 때 깨우느라 몇 초 지연될 수 있습니다.
- **지역(region)**: `render.yaml`의 `region`을 가까운 곳(예: singapore)로 바꾸면 지연이 줄어듭니다.
- **비밀값/환경변수**: Render 대시보드 → Service → Environment 탭에서 추가하세요.
