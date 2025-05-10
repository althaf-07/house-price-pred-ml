from pathlib import Path
from typing import Literal

import pandas as pd

from house_price_prediction.utils import parse_yaml, setup_logger


def data_preprocessor(df_type: Literal["train", "test"], config, log, export_df=True):
    cat_cols = config["cols"]["cat"]
    numd_cols = config["cols"]["numd"]

    # Load dataset
    try:
        raw_data_path = Path(config["paths"]["data"]["interim"][df_type])
        df = pd.read_csv(raw_data_path)
        log.success(f"Loaded {df_type} dataset")
    except Exception:
        log.exception(f"Failed to load {df_type} dataset")
        raise

    # Rename columns
    try:
        df.rename(columns=config["col_names_renamed"], inplace=True)
        log.success(
            f"Renamed columns: {df.columns[:3].to_list()}... (+{len(df.columns) - 3} more)"
        )
    except Exception:
        log.exception("Failed to rename columns")
        raise

    # Clean values
    try:
        for col in cat_cols:
            df[col] = df[col].str.lower().str.replace(" ", "_")
        log.success("Cleaned values in columns")
    except Exception:
        log.exception("Failed to clean values in columns")
        raise
    
    # Convert dtypes
    try:
        df[cat_cols + numd_cols] = df[cat_cols + numd_cols].astype("category")
        log.success("Converted dtypes of columns")
    except Exception:
        log.exception("Failed to convert dtypes of columns")
        raise

    if export_df:
        # Export dataset
        try:
            processed_path = Path(config["paths"]["data"]["processed"][df_type])
            processed_path.parent.mkdir(exist_ok=True, parents=True)
            df.to_csv(processed_path, index=False)
            log.success(f"Exported {df_type} dataset")
        except Exception:
            log.exception(f"Failed to export {df_type} dataset")
            raise
    else:
        return df


def main():
    log = setup_logger()
    config = parse_yaml(log)
    data_preprocessor("train", config, log)
    data_preprocessor("test", config, log)


if __name__ == "__main__":
    main()
