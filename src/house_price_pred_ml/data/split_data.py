import logging
import sys
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from house_price_pred_ml.config import MainConfig, load_config
from house_price_pred_ml.utils.logger import load_logger


def export_df(
    X_train: pd.DataFrame, X_test: pd.DataFrame, logger: logging.Logger, cfg: MainConfig
):
    try:
        cfg.data_config.processed_test.parent.mkdir(exist_ok=True, parents=True)
        X_test.to_csv(cfg.data_config.processed_test, index=False, mode="x")
        X_train.to_csv(cfg.data_config.processed_train, index=False, mode="x")
        logger.info(f"Exported datasets to {cfg.data_config.processed_test.parent}")
    except FileExistsError as e:
        logger.exception(
            f"Failed to export datasets to {cfg.data_config.processed_test.parent}: {e}"
        )
        sys.exit(1)
    except Exception as e:
        logger.exception(
            f"Failed to export datasets to {cfg.data_config.processed_test.parent}: {e}"
        )
        sys.exit(1)


def split_data(
    df: pd.DataFrame, logger: logging.Logger, cfg: MainConfig
) -> tuple[pd.DataFrame, pd.DataFrame]:
    try:
        X_train, X_test = train_test_split(
            df,
            test_size=cfg.data_config.tts_params["test_size"],
            random_state=cfg.data_config.tts_params["random_state"],
        )
        logger.info(f"Splitted dataset with parameters: {cfg.data_config.tts_params}")
    except Exception as e:
        logger.exception(f"Failed to split dataset: {e}")
        raise
    return X_train, X_test


def load_dataset(logger: logging.Logger, cfg: MainConfig) -> pd.DataFrame:
    try:
        df = pd.read_csv(cfg.data_config.interim)
        logger.info(f"Loaded dataset from {cfg.data_config.interim}")
    except FileNotFoundError as e:
        logger.exception(f"Failed to load dataset from {cfg.data_config.interim}: {e}")
        sys.exit(1)
    except Exception as e:
        logger.exception(f"Failed to load dataset from {cfg.data_config.interim}: {e}")
        sys.exit(1)
    return df


def main() -> None:
    cfg = load_config()
    logger = load_logger(__name__, Path(__file__).stem)
    df = load_dataset(logger, cfg)
    X_train, X_test = split_data(df, logger, cfg)
    export_df(X_train, X_test, logger, cfg)


if __name__ == "__main__":
    main()
