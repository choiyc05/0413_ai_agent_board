import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { ArrowLeft, User } from 'lucide-react';
import api from '@/api';
import './BoardDetail.css';

const BoardDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [post, setPost] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchPost = async () => {
      try {
        const response = await api.get(`/board/post/${id}`);
        if (response.data.status) {
          setPost(response.data.post);
        } else {
          setError(response.data.message);
        }
      } catch (err) {
        setError("Failed to fetch post details.");
      }
    };
    fetchPost();
  }, [id]);

  if (error) {
    return (
      <div className="detail-container">
        <button className="back-btn" onClick={() => navigate(-1)}>
          <ArrowLeft />
          Back to Board
        </button>
        <p style={{ color: 'var(--text-muted)' }}>{error}</p>
      </div>
    );
  }

  if (!post) return <div className="detail-container">Loading...</div>;

  return (
    <div className="detail-container">
      <button className="back-btn" onClick={() => navigate('/')}>
        <ArrowLeft />
        Back to Board
      </button>

      <div className="detail-header">
        <h1 className="detail-title">{post.title}</h1>
        <div className="detail-meta">
          <div className="detail-author-wrap">
            <User size={16} />
            <span>{post.name}</span>
          </div>
        </div>
      </div>

      <div className="detail-content">
        {post.content}
      </div>
    </div>
  );
};

export default BoardDetail;
