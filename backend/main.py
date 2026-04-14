from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core import lifespan
from src import board

routers = [board]
app = FastAPI(title="AI Agent Board", lifespan=lifespan)
for router in routers:
    app.include_router(router.router)

ORIGINS = ["http://localhost", "http://localhost:5173", "http://192.168.0.111:5173", "http://aiedu.tplinkdns.com:6110", "http://aiedu.tplinkdns.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}