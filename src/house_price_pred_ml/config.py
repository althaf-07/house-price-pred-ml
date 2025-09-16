from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

import yaml


@dataclass
class ColumnConfig:
    target: str
    cols_renamed: dict
    cat_cols: list[str]
    numc_cols: list[str]
    numd_cols: list[str]
    cat_numd_cols: list[str] = field(init=False)

    def __post_init__(self):
        self.cat_numd_cols = self.cat_cols + self.numd_cols


@dataclass
class ModelConfig:
    models_dir: Path
    model_name: Literal[
        "linr",
        "logr",
        "rfc",
        "rfr",
        "knnc",
        "knnr",
        "svc",
        "svr",
        "dtc",
        "dtr",
        "gbc",
        "gbr",
        "etc",
        "etr",
    ]
    hyper_params: dict[str, int | float | str]


@dataclass
class DataConfig:
    raw: Path
    interim: Path
    processed_test: Path
    processed_train: Path
    tts_params: dict
    data_url: str


@dataclass
class MainConfig:
    data_config: DataConfig
    model_config: ModelConfig
    column_config: ColumnConfig


def load_config(path: Path = Path("src/house_price_pred_ml/config.yaml")) -> MainConfig:
    with path.open("r") as file:
        cfg_file = yaml.safe_load(file)

    data_config = DataConfig(
        raw=Path(cfg_file["paths"]["data"]["raw"]["raw"]),
        interim=Path(cfg_file["paths"]["data"]["interim"]["interim"]),
        processed_test=Path(cfg_file["paths"]["data"]["processed"]["test"]),
        processed_train=Path(cfg_file["paths"]["data"]["processed"]["train"]),
        tts_params=cfg_file["train_test_split"],
        data_url=cfg_file["data_url"],
    )

    model_config = ModelConfig(
        model_name=cfg_file["model"]["name"],
        models_dir=cfg_file["paths"]["models"],
        hyper_params=cfg_file["model"]["hyper_params"],
    )

    column_config = ColumnConfig(
        target=cfg_file["cols"]["target"],
        cols_renamed=cfg_file["cols_renamed"],
        cat_cols=cfg_file["cols"]["cat"],
        numc_cols=cfg_file["cols"]["numc"],
        numd_cols=cfg_file["cols"]["numd"],
    )

    return MainConfig(
        data_config=data_config,
        model_config=model_config,
        column_config=column_config,
    )
