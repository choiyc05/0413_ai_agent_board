import { Routes, Route } from 'react-router-dom';
import MainLayout from '@components/Layout/MainLayout';
import BoardList from '@components/Board/BoardList';
import BoardDetail from '@components/Board/BoardDetail';
import ChatInterface from '@components/Chat/ChatInterface';
import NotFound from '@components/Layout/NotFound';

function App() {
  return (
    <Routes>
      <MainLayout bottomContent={<ChatInterface />}>
        <Route path="/" element={<BoardList />} />
        <Route path="/post/:id" element={<BoardDetail />} />
      </MainLayout>
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}

export default App;
