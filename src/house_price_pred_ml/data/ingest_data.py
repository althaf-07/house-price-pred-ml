import sys
from pathlib import Path

import gdown

from house_price_pred_ml.config import load_config
from house_price_pred_ml.utils.logger import load_logger


def main() -> None:
    cfg = load_config()
    logger = load_logger(__name__, Path(__file__).stem)

    if not cfg.data_config.raw.is_file():
        try:
            cfg.data_config.raw.parent.mkdir(parents=True, exist_ok=True)
            gdown.download(cfg.data_config.data_url, str(cfg.data_config.raw))
            logger.info(
                f"Downloaded dataset from {cfg.data_config.data_url} to {cfg.data_config.raw}"
            )
        except Exception as e:
            logger.exception(
                f"Failed to download dataset from {cfg.data_config.data_url} to {cfg.data_config.raw}: {e}"
            )
            sys.exit()
    else:
        logger.info(
            f"Dataset already exists at {cfg.data_config.raw}. Skipping download."
        )


if __name__ == "__main__":
    main()
