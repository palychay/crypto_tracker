from typing import Annotated

from fastapi import Request

from src.http_client import CMCHTTPClient


async def get_cmc_client(request: Request) -> CMCHTTPClient:
    return request.app.state.cmc_client
