from datetime import datetime
from pathlib import Path
import inspect

import yaml
from loguru import logger
from sklearn.ensemble import (
    GradientBoostingClassifier,
    GradientBoostingRegressor,
    RandomForestClassifier,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.svm import SVC, SVR
from sklearn.tree import (
    DecisionTreeClassifier,
    DecisionTreeRegressor,
    ExtraTreeClassifier,
    ExtraTreeRegressor,
)


def setup_logger():
    name = Path(inspect.stack()[1][1]).stem
    log_path = Path("logs/")
    log_path.mkdir(exist_ok=True, parents=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = log_path / f"{name}_{timestamp}.log"
    logger.add(log_file)
    return logger


def parse_yaml(log) -> dict:
    try:
        config_path = Path(__file__).resolve().parent / "config.yaml"
        with config_path.open("r") as file:
            config = yaml.safe_load(file)
        log.success("Parsed config.yaml")
        return config
    except Exception:
        log.exception("Failed to parse config.yaml")
        raise


def get_model(config: dict):
    model_name = config["model"]["name"]
    hyper_params = config.get("hyper_params", {})
    models = {
        "lin_reg": LinearRegression,
        "log_reg": LogisticRegression,
        "rfc": RandomForestClassifier,
        "rfr": RandomForestRegressor,
        "knnc": KNeighborsClassifier,
        "knnr": KNeighborsRegressor,
        "svc": SVC,
        "svr": SVR,
        "dtc": DecisionTreeClassifier,
        "dtr": DecisionTreeRegressor,
        "gbc": GradientBoostingClassifier,
        "gbr": GradientBoostingRegressor,
        "etc": ExtraTreeClassifier,
        "etr": ExtraTreeRegressor,
    }

    if model_name not in models:
        available = ", ".join(models.keys())
        raise ValueError(
            f"Unsupported model name: '{model_name}'. Available options: {available}"
        )

    return models[model_name](**hyper_params)
