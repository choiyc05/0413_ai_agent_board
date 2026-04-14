# 0413_ai_agent_board

```bash
~0415(수)
frontend - react
backend - python

- 주제 : 프롬프트를 이용하는 게시판

1. 게시글 목록
2. 프롬프트 입력 시 => 게시글 작성 하기 / 게시글 상세 화면 / 수정 / 삭제 기능
```bash
## 🛠 Tech Stack
- **Framework**: FastAPI
- **LLM**: Ollama (Gemma4:e4b)
- **Agent**: LangGraph (ReAct Agent)
- **Database**: MariaDB
- **Package Manager**: uv

## 📁 Directory Guide
- `main.py`: API 라우팅.
- `src/core.py`: AI 에이전트의 페르소나와 Tool 정의.
- `settings.py`: DB URL, Ollama Endpoint 등 환경 변수 관리.

.
├── backend/                    # FastAPI 기반 백엔드 서비스
│   ├── src/
│   │   ├── board.py            # 게시판 관련 API 엔드포인트
│   │   ├── core.py             # AI 에이전트 및 LangGraph 설정
│   │   └── mariadb_crud.py     # 데이터베이스 CRUD
│   ├── main.py                 # FastAPI 애플리케이션 진입점
│   ├── settings.py             # 환경 설정 (Pydantic-Settings)
│   ├── pyproject.toml          # uv 의존성 관리
│   └── uv.lock                 # uv 패키지 잠금 파일
│
├── frontend/                   # Vite + React 프론트엔드 서비스
│   ├── src/
│   │   ├── components/         # 기능별 컴포넌트 분리
│   │   │   ├── Board/          # 리스트 및 상세 보기 관련
│   │   │   ├── Chat/           # AI 에이전트 채팅 인터페이스
│   │   │   └── Layout/         # 페이지 메인 레이아웃
│   │   ├── styles/             # 전역 및 테마 CSS 파일
│   │   ├── api.js              # Axios 등 백엔드 통신 로직
│   │   ├── App.jsx             # 메인 앱 컴포넌트 및 라우팅
│   │   └── main.jsx            # 리액트 진입점
│   ├── Dockerfile              # Nginx 등을 활용한 배포 설정
│   ├── nginx.conf              # 프론트엔드용 웹 서버 설정
│   └── package.json            # Node.js 의존성 관리
│
├── db/                         # 데이터베이스 초기화 및 설정
│   └── initdb.d/
│       └── ddl.sql             # 컨테이너 실행 시 자동 생성될 테이블 스키마
│
└── compose.yml                 # DB-Back-Front 멀티 컨테이너 설정
```

```bash

```