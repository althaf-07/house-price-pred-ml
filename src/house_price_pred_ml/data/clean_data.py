import logging
import sys
from pathlib import Path

import pandas as pd

from house_price_pred_ml.config import MainConfig, load_config
from house_price_pred_ml.utils.logger import load_logger


def export_df(df: pd.DataFrame, logger: logging.Logger, cfg: MainConfig):
    try:
        cfg.data_config.interim.parent.mkdir(exist_ok=True, parents=True)
        df.to_csv(cfg.data_config.interim, index=False, mode="x")
        logger.info(f"Exported dataset to {cfg.data_config.interim}")
    except FileExistsError as e:
        logger.exception(f"Failed to export dataset to {cfg.data_config.interim}: {e}")
        sys.exit(1)
    except Exception as e:
        logger.exception(f"Failed to export dataset to {cfg.data_config.interim}: {e}")
        sys.exit(1)


def clean_values(
    df: pd.DataFrame, logger: logging.Logger, cfg: MainConfig
) -> pd.DataFrame:
    try:
        for col in cfg.column_config.cat_cols:
            df[col] = df[col].str.lower().str.replace(" ", "_")
        logger.info("Cleaned values in columns")
    except Exception as e:
        logger.exception(f"Failed to clean values in columns: {e}")
        sys.exit(1)
    return df


def rename_cols(
    df: pd.DataFrame, logger: logging.Logger, cfg: MainConfig
) -> pd.DataFrame:
    try:
        df.rename(columns=cfg.column_config.cols_renamed, inplace=True)
        logger.info("Renamed columns")
    except Exception as e:
        logger.exception(f"Failed to rename columns: {e}")
        sys.exit(1)
    return df


def load_dataset(logger: logging.Logger, cfg: MainConfig) -> pd.DataFrame:
    try:
        df = pd.read_csv(cfg.data_config.raw)
        logger.info(f"Loaded dataset from {cfg.data_config.raw}")
    except FileNotFoundError as e:
        logger.exception(f"Failed to load dataset from {cfg.data_config.raw}: {e}")
        sys.exit(1)
    except Exception as e:
        logger.exception(f"Failed to load dataset from {cfg.data_config.raw}: {e}")
        sys.exit(1)
    return df


def main() -> None:
    cfg = load_config()
    logger = load_logger(__name__, Path(__file__).stem)
    df = load_dataset(logger, cfg)
    df = rename_cols(df, logger, cfg)
    df = clean_values(df, logger, cfg)
    export_df(df, logger, cfg)


if __name__ == "__main__":
    main()
