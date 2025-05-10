from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

from house_price_prediction.utils import get_model, parse_yaml, setup_logger


def build_ct(config: dict):
    numc_cols = config["cols"]["numc"]
    oe_cols = config["preprocessing"]["oe"]
    oe_pl = Pipeline([("encoder", OrdinalEncoder())])
    numc_pl = Pipeline([("scaler", StandardScaler())])
    ct = ColumnTransformer(
        [("numc", numc_pl, numc_cols), ("oe", oe_pl, oe_cols)], remainder="passthrough"
    )
    return ct


def main():
    log = setup_logger()
    config = parse_yaml(log)
    target = config["cols"]["target"]

    try:
        df = pd.read_csv(config["paths"]["data"]["processed"]["train"])
        X_train = df.drop(target, axis=1)
        y_train = df[target]
        log.success("Loaded training dataset")
    except Exception:
        log.exception("Failed to load training dataset")
        raise

    ct = build_ct(config)
    reg = get_model(config)
    pl = Pipeline([("ct", ct), ("reg", reg)])

    try:
        cv_scores = cross_val_score(pl, X_train, y_train, cv=5)
        cv_mean, cv_std = round(cv_scores.mean(), 4), round(cv_scores.std(), 4)
        log.success(f"5-Fold CV Accuracy: {cv_mean} ± {cv_std}")
    except Exception:
        log.exception("Cross-validation failed")
        raise

    try:
        pl.fit(X_train, y_train)
        model_dir = Path(config["paths"]["models"])
        model_dir.mkdir(exist_ok=True, parents=True)
        joblib.dump(pl, model_dir / "pl.joblib")
        log.success(f"Pipeline trained and saved to {model_dir / 'pl.joblib'}")
    except Exception:
        log.exception("Pipeline training and saving failed")
        raise


if __name__ == "__main__":
    main()
