from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    WALLET_ADDRESS: str = ""


settings = Settings()

GNOSIS_API_TOKENLIST_URI = f"https://gnosis.blockscout.com/api/v2/addresses/{settings.WALLET_ADDRESS}/token-balances"
REALT_API_TOKENLIST_URI = "https://api.realt.community/v1/token"
REALT_OFFLINE_TOKENS_LIST = "RealT_OfflineTokensList.json"
REALT_OFFLINE_TOKENS_LIST_FREE = "RealT_OfflineTokensList_Free.json"
EXCHANGE_RATES_API_URI = "https://open.er-api.com/v6/latest/"
EXCHANGE_OFFLINE_RATES_PATH = "./"
