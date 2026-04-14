from fastapi import APIRouter, Depends, HTTPException, logger
from src.mariadb_crud import findAll, findOne
from src.core import Query, get_app_state, logger

router = APIRouter(tags=["Board"], prefix="/board")

@router.get("/list")
def get_board():
    """DB에서 삭제되지 않은 게시글 목록을 최신순으로 조회"""
    try:
        # delYn이 0인 데이터만, no 역순으로 가져옵니다.
        sql = "SELECT no, title, name, content FROM list WHERE delYn = 0 ORDER BY no DESC"
        posts = findAll(sql)
        return {"status": True, "data": posts}
    except Exception as e:
        logger.error(f"목록 조회 중 에러: {str(e)}")
        return {"status": False, "message": "목록을 불러오는데 실패했습니다."}

@router.get("/post/{post_no}")
def read_post(post_no: int):
    """DB에서 게시글 조회"""
    try:
        sql = "SELECT no, title, name, content FROM list WHERE no = ? AND delYn = 0"
        post = findOne(sql, (post_no,))
        if not post:
            return {"status": False, "message": "존재하지 않거나 삭제된 게시글입니다."}
        return {"status": True, "post": post}
    except Exception as e:
        logger.error(f"상세 조회 중 에러: {str(e)}")
        raise HTTPException(status_code=500, detail="데이터 조회 중 오류 발생")

@router.post("/ask")
async def ask_agent(query: Query, state=Depends(get_app_state)):
    """AI 에이전트에게 명령을 전달하는 엔드포인트"""
    try:
        agent = state.agent_executor

        config = {"configurable": {"thread_id": "user1"}}
        inputs = {"messages": [("user", query.input)]}
        result = await agent.ainvoke(inputs, config=config)

        # 에이전트의 마지막 메시지(결과 보고) 추출
        final_message = result["messages"][-1].content
        
        return {"status": True, "answer": final_message}
    except Exception as e:
        logger.error(f"실행 중 에러: {str(e)}")
        raise HTTPException(status_code=500, detail=f"에이전트 처리 중 오류: {str(e)}")