import mariadb
from settings import settings

conn_params = {
  "user" : settings.db_user,
  "password" : settings.db_password,
  "host" : settings.db_host,
  "database" : settings.db_database,
  "port" : settings.db_port
}

def getConn():
    """DB 연결 객체 생성 및 반환"""
    try:
        conn = mariadb.connect(**conn_params)
        return conn
    except mariadb.Error as e:
        print(f"접속 오류 : {e}")
        return None

def findOne(sql, params=None):
    """단일 행 조회 (딕셔너리 반환)"""
    result = None
    try:
        with getConn() as conn:
            # dictionary=True 옵션으로 별도의 zip 작업 없이 딕셔너리 반환
            with conn.cursor(dictionary=True) as cur:
                cur.execute(sql, params)
                result = cur.fetchone()
    except mariadb.Error as e:
        print(f"MariaDB Error (findOne): {e}")
    return result

def findAll(sql, params=None):
    """전체 행 조회 (딕셔너리 리스트 반환)"""
    result = []
    try:
        with getConn() as conn:
            with conn.cursor(dictionary=True) as cur:
                cur.execute(sql, params)
                result = cur.fetchall()
    except mariadb.Error as e:
        print(f"MariaDB Error (findAll): {e}")
    return result

def save(sql, params=None):
    """데이터 삽입/수정/삭제 (성공 여부 반환)"""
    try:
        with getConn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                conn.commit()
                return True
    except mariadb.Error as e:
        print(f"MariaDB Error (save): {e}")
        return False

