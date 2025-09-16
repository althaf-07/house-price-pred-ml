from pathlib import Path
from typing import Literal

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


def get_model(
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
    ],
    hyper_params,
):
    models = {
        "linr": LinearRegression,
        "logr": LogisticRegression,
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
    available = ", ".join(models.keys())
    try:
        return models[model_name](**hyper_params)
    except KeyError:
        raise KeyError(
            f"Unsupported model name: '{model_name}'. Available options: {available}"
        )


def auto_generate(file_path: Path, content: str, section_name: str):
    start_marker = f"[//]: # (START:{section_name})"
    end_marker = f"[//]: # (END:{section_name})"
    try:
        text = file_path.read_text()
    except FileNotFoundError:
        raise
    if start_marker not in text or end_marker not in text:
        raise ValueError(f"Section markers for {section_name} not found!")

    before, rest = text.split(start_marker, 1)
    _, after = rest.split(end_marker, 1)

    updated_content = f"{before}{start_marker}\n\n{content}\n\n{end_marker}{after}"
    file_path.write_text(updated_content)
