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

backend
├── .python-version          
├── pyproject.toml           
├── uv.lock                  
├── README.md                
├── settings.py              # 공통 환경 설정 (pydantic-settings)
├── main.py                  # FastAPI 진입점
└── src/                     
    ├── board.py             # 게시판 도메인 관련 로직
    ├── core.py              # LangGraph 에이전트 및 LLM 초기화 (lifespan)
    └── mariadb_crud.py      # MariaDB 연결

frontend
├── 

```

```bash

```