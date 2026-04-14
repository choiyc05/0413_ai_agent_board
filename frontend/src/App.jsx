import { Routes, Route } from 'react-router-dom';
import MainLayout from '@components/Layout/MainLayout';
import BoardList from '@components/Board/BoardList';
import BoardDetail from '@components/Board/BoardDetail';
import ChatInterface from '@components/Chat/ChatInterface';

function App() {
  return (
    <MainLayout bottomContent={<ChatInterface />}>
      <Routes>
        <Route path="/" element={<BoardList />} />
        <Route path="/post/:id" element={<BoardDetail />} />
      </Routes>
    </MainLayout>
  );
}

export default App;
