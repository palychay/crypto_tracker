from fastapi import APIRouter
from src.dependencies import get_cmc_client
from fastapi import Depends
from src.http_client import CMCHTTPClient


router = APIRouter(
    prefix="/cryptocurrencies"
)

@router.get("")
async def get_cryptocurrencies(cmc_client: CMCHTTPClient = Depends(get_cmc_client)):
    return await cmc_client.get_listings()


@router.get("/{currency_id}")
async def get_cryptocurrency(currency_id: int, cmc_client: CMCHTTPClient = Depends(get_cmc_client)):
    return await cmc_client.get_currency(currency_id=currency_id)