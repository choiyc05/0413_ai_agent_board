
function NotFound() {
  return (
    <div style={{ padding: '20px', textAlign: 'center' }}>
      <h1>404 - 페이지를 찾을 수 없습니다.</h1>
      <p>요청하신 주소가 올바르지 않거나 변경되었습니다.</p>
      <a href="/">홈으로 돌아가기</a>
    </div>
  );
}

export default NotFound;