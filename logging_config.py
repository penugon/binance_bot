import logging

def setup_logger() -> logging.Logger:
    logger = logging.getLogger("TradingBot")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("trading.log")
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger
