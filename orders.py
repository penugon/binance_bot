from typing import Dict, Any
from binance.client import Client
from binance.exceptions import BinanceAPIException
from logging import Logger

def place_futures_order(
    client: Client,
    logger: Logger,
    params: Dict[str, Any]
) -> Dict[str, Any] | None:

    logger.info(f"SENT: {params}")

    try:
        response = client.futures_create_order(**params)

        logger.info(
            f"RECEIVED: orderId={response.get('orderId')}, "
            f"status={response.get('status')}, "
            f"avgPrice={response.get('avgPrice')}"
        )

        return response

    except BinanceAPIException as e:
        logger.error(f"BINANCE ERROR: {e.message}")
    except Exception as e:
        logger.error(f"UNEXPECTED ERROR: {str(e)}")

    return None
