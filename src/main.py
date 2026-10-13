from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import settings
from src.http_client import CMCHTTPClient
from src.router import router as router_crypto


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.cmc_client = CMCHTTPClient(
        base_url="https://pro-api.coinmarketcap.com",
        api_key=settings.CMC_API_KEY,
    )
    yield
    await app.state.cmc_client.close()



app = FastAPI(lifespan=lifespan)
app.include_router(router_crypto)


origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)