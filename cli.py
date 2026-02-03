import argparse
from client import get_authenticated_client
from validators import validate_order_params
from orders import place_futures_order
from logging_config import setup_logger

def main() -> None:
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True, dest="order_type")
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_order_params(
            symbol=args.symbol,
            side=args.side,
            order_type=args.order_type,
            quantity=args.quantity,
            price=args.price
        )
    except ValueError as e:
        print(f"Validation Error: {e}")
        return

    client = get_authenticated_client()
    logger = setup_logger()

    order_params = {
        "symbol": args.symbol,
        "side": args.side,
        "type": args.order_type,
        "quantity": args.quantity,
    }

    if args.order_type == "LIMIT":
        order_params.update({
            "price": args.price,
            "timeInForce": "GTC"
        })

    place_futures_order(client, logger, order_params)

if __name__ == "__main__":
    main()

