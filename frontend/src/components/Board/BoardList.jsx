import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '@/api';
import './BoardList.css';

const BoardList = () => {
  const [posts, setPosts] = useState([]);
  const navigate = useNavigate();

  const fetchPosts = async () => {
    try {
      const response = await api.get('/board/list');
      if (response.data.status) {
        setPosts(response.data.data);
      } else {
        console.error("Failed to fetch posts:", response.data.message);
      }
    } catch (error) {
      console.error("Failed to fetch posts:", error);
    }
  };

  useEffect(() => {
    fetchPosts();
  }, []);

  return (
    <div className="board-container">
      <div className="board-header">
        <div>
          <h1 className="board-title">AI Agent Board</h1>
          <p className="board-subtitle">Ask the AI agent below to manage posts.</p>
        </div>
      </div>

      <div className="board-grid">
        {posts.map((post) => (
          <div key={post.no} className="board-card" onClick={() => navigate(`/post/${post.no}`)}>
            <div className="card-date">No. {post.no}</div>
            <h2 className="card-title">{post.title}</h2>
            <p className="card-preview">{post.content}</p>
            <div className="card-footer">
              <div className="card-author">
                <div className="author-avatar">{post.name?.charAt(0) || '?'}</div>
                <span>{post.name}</span>
              </div>
            </div>
          </div>
        ))}
        {posts.length === 0 && (
          <div style={{ color: 'var(--text-muted)', gridColumn: '1 / -1', textAlign: 'center', padding: '40px 0' }}>
            No posts found. Use the AI interface below to create one!
          </div>
        )}
      </div>
    </div>
  );
};

export default BoardList;
