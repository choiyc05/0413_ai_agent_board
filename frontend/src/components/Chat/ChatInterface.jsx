import React, { useState, useRef, useEffect } from 'react';
import { Send, Terminal, Loader2, ChevronDown, ChevronUp } from 'lucide-react';
import api from '@/api';
import './ChatInterface.css';

const ChatInterface = () => {
  const [messages, setMessages] = useState([
    { id: 1, type: 'ai', text: 'Hello! 저는 여러분의 AI 게시판 관리자입니다. 게시글 작성, 게시글 수정 또는 삭제를 저에게 요청할 수 있습니다.' }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [loading, setLoading] = useState(false);
  const [isMinimized, setIsMinimized] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    if (!isMinimized) {
      scrollToBottom();
    }
  }, [messages, isMinimized]);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!inputValue.trim()) return;

    const userInput = inputValue;
    const newMessage = { id: Date.now(), type: 'user', text: userInput };
    setMessages(prev => [...prev, newMessage]);
    setInputValue('');
    setLoading(true);

    try {
      const response = await api.post('/board/ask', { input: userInput });
      if (response.data.status) {
        setMessages(prev => [...prev, {
          id: Date.now() + 1,
          type: 'ai',
          text: response.data.answer
        }]);
        // 응답이 도착하면 자동으로 창을 펼침
        setIsMinimized(false);
        window.dispatchEvent(new Event('refreshBoard'));
      } else {
        throw new Error("Failed to get a proper response from AI");
      }
    } catch (error) {
      setMessages(prev => [...prev, {
        id: Date.now() + 1,
        type: 'ai',
        text: '죄송합니다. 오류가 발생했습니다. 연결을 확인해주세요.'
      }]);
      setIsMinimized(false);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={`chat-container ${isMinimized ? 'minimized' : ''}`}>
      <div className="chat-header" onClick={() => setIsMinimized(!isMinimized)} style={{ cursor: 'pointer' }}>
        {loading ? <Loader2 size={18} className="spinner" /> : <Terminal size={18} color="var(--text-secondary)" />}
        <div className="chat-title" style={{ flex: 1 }}>
          {loading ? 'Processing...' : 'Agent Terminal'} <span className={`status-dot ${loading ? 'pulsing' : ''}`}></span>
        </div>
        {isMinimized ? <ChevronUp size={20} color="var(--text-secondary)" /> : <ChevronDown size={20} color="var(--text-secondary)" />}
      </div>

      <div className="chat-messages">
        {messages.map((msg) => (
          <div key={msg.id} className={`message ${msg.type}`}>
            {msg.text}
          </div>
        ))}
        {loading && (
          <div className="message ai" style={{ opacity: 0.6 }}>
            AI가 생각 중입니다...
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <form className="chat-input-area" onSubmit={handleSend}>
        <div className="chat-input-wrapper">
          <input
            type="text"
            className="chat-input"
            placeholder="AI에게 명령하세요 (예: 'AI에 대한 게시글을 작성해줘.')"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            disabled={loading}
          />
          <button
            type="submit"
            className="send-btn"
            disabled={!inputValue.trim() || loading}
          >
            <Send size={20} />
          </button>
        </div>
      </form>
    </div>
  );
};

export default ChatInterface;
