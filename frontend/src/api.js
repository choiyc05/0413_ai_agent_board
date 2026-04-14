import axios from 'axios';

const api = axios.create({
  baseURL: '/api', // This works locally (via Vite proxy) and in Docker (via Nginx proxy)
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;
