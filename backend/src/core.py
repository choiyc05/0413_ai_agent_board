import json
import logging
import re
from pydantic import BaseModel, Field
from src.mariadb_crud import save
from settings import settings
from langchain_ollama import ChatOllama
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Query(BaseModel):
  input: str

class PostCreate(BaseModel):
    title: str = Field(description="게시글 제목")
    name: str = Field(description="작성자 이름")
    content: str = Field(description="게시글 본문 내용")

class PostUpdate(BaseModel):
    post_no: int = Field(description="수정할 게시글의 No (Primary Key)")
    title: str = Field(None, description="수정할 제목")
    content: str = Field(None, description="수정할 본문 내용")

class PostDelete(BaseModel):
    post_no: int = Field(description="삭제할 게시글의 No (Primary Key)")

@tool(args_schema=PostCreate)
def create_board_post(title: str, name: str, content: str):
    """
    사용자의 요청을 바탕으로 새로운 게시글을 데이터베이스에 저장합니다.
    - title: 추출된 제목
    - name: 작성자 이름 (없을 경우 '익명'으로 설정)
    - content: 생성되거나 추출된 본문 내용
    """
    sql = "INSERT INTO board.list (title, name, content, delYn) VALUES (?, ?, ?, 0)"
    params = (title, name, content)
    if save(sql, params):
        return {"status": True, "message": "성공적으로 게시글을 작성했습니다."}
    return {"status": False, "message": "게시글 작성에 실패했습니다."}

@tool(args_schema=PostUpdate)
def update_board_post(post_no: int, title: str = None, content: str = None):
    """
    게시글의 No를 사용하여 제목이나 본문 내용을 수정합니다.
    - post_no: 필수 입력값
    - 사용자가 수정을 원하는 필드(title 또는 content)만 업데이트합니다.
    """
    fields = []
    params = []
    
    if title:
        fields.append("title = ?")
        params.append(title)
    if content:
        fields.append("content = ?")
        params.append(content)
    
    if not fields:
        return "수정할 내용이 제공되지 않았습니다."
    
    params.append(post_no)
    sql = f"UPDATE board.list SET {', '.join(fields)} WHERE no = ?"
    
    if save(sql, tuple(params)):
        return {"status": True, "message": "게시글이 수정되었습니다."}
    return {"status": False, "message": "게시글 수정에 실패했습니다."}

@tool(args_schema=PostDelete)
def delete_board_post(post_no: int):
    """
    게시글 No를 받아 해당 게시글을 논리적으로 삭제(delYn=1)합니다.
    """
    sql = "UPDATE board.list SET delYn = 1 WHERE no = ?"
    params = (post_no,)
    
    if save(sql, params):
        return {"status": True, "message": "게시글이 삭제 처리되었습니다."}
    return {"status": False, "message": "게시글 삭제에 실패했습니다."}

tools = [create_board_post, update_board_post, delete_board_post]

def extract_json(text: str) -> dict:
  match = re.search(r"(\{.*\})", text, re.DOTALL)
  if match:
    return json.loads(match.group(1))
  return json.loads(text)

def get_app_state(request: Request):
  return request.app.state

@asynccontextmanager
async def lifespan(app: FastAPI):
  try:
    llm = ChatOllama(
      model=settings.ollama_model_name, 
      base_url=settings.ollama_base_url, 
      # format="json",
      temperature=0
    )

    system_message = (
      f"당신은 게시판 관리 전문 에이전트입니다."
      f"사용자의 요청에 따라 제공된 도구(tools)를 사용하여 게시글을 작성, 수정, 삭제하세요. "
      f"게시글 작성 시에는 제목(title), 작성자 이름(name), 본문 내용(content)을 포함해야 합니다. "
      f"게시글 수정 시에는 게시글 No(post_no)를 필수로 받고, 제목(title)과 본문 내용(content)은 선택적으로 수정할 수 있습니다. "
      f"게시글 삭제 시에는 게시글 No(post_no)를 필수로 받아 해당 게시글을 삭제 처리(delYn=1)하세요. "
    )

    # 1. 메모리 저장소 생성
    memory = MemorySaver()
    app.state.agent_executor = create_react_agent(llm, tools, prompt=system_message,checkpointer=memory)

    yield
  except Exception as e:
    logger.error(f"초기화 중 오류 발생: {e}")
  finally:
    logger.info("Finalizing shutdown...")