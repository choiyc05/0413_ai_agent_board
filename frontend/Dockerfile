# 1단계: 빌드 (Build Stage)
FROM node:20-alpine AS build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# 2단계: 실행 (Production Stage)
FROM nginx:alpine AS production
# 빌드 스테이지의 결과물(/app/dist)을 Nginx 경로로 복사
COPY --from=build-stage /app/dist /usr/share/nginx/html
# 설정 파일 복사
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]