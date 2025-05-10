from pathlib import Path

import pandas as pd

from house_price_prediction.utils import parse_yaml, setup_logger


def write_md(file_path, modified_content, section_name):
    start_marker = f"[//]: # (START:{section_name})"
    end_marker = f"[//]: # (END:{section_name})"
    text = file_path.read_text()
    if start_marker not in text or end_marker not in text:
        raise ValueError(f"Section markers for {section_name} not found!")

    before = text.split(start_marker)[0]
    after = text.split(end_marker)[1]
    updated_content = (
        f"{before}{start_marker}\n\n{modified_content}\n\n{end_marker}{after}"
    )
    file_path.write_text(updated_content)


def main():
    log = setup_logger()
    config = parse_yaml(log)
    cat_cols = config["cols"]["cat"]
    target = config["cols"]["target"]
    numc_cols = config["cols"]["numc"]
    numd_cols = config["cols"]["numd"]
    experiment_doc = Path(config["paths"]["reports"]["experiment_document"])

    # Load dataset
    try:
        df_path = Path(config["paths"]["data"]["processed"]["train"])
        df = pd.read_csv(df_path)
        log.success("Loaded dataset")
    except Exception:
        log.exception("Failed to load dataset")
        raise

    # Convert dtypes
    try:
        df[cat_cols + numd_cols] = df[cat_cols + numd_cols].astype("category")
        log.success("Converted dtypes of columns")
    except Exception:
        log.exception("Failed to convert dtypes of columns")
        raise

    model_experiment_results = [
        {
            "Model": "log_reg",
            "Hyperparameters": {},
            "Accuracy": 0.81,
            "F1 Score": 0.81,
            "Notes": "Baseline model",
        },
        {
            "Model": "rfr",
            "Hyperparameters": {},
            "Accuracy": 0.85,
            "F1 Score": 0.85,
            "Notes": "OK",
        },
        {
            "Model": "xgbr",
            "Hyperparameters": {},
            "Accuracy": 0.87,
            "F1 Score": 0.87,
            "Notes": "Best performance so far",
        },
    ]

    model_experiment_results_md = pd.DataFrame(model_experiment_results).to_markdown()
    write_md(experiment_doc, model_experiment_results_md, "MODEL_EXPERIMENT_RESULTS")

    numc_target_describe = df[numc_cols + [target]].describe().T.to_markdown()
    numd_cat_describe = df[numd_cols + cat_cols].describe().T.to_markdown()
    numc_table = f"### Continuous Numerical Features\n\n{numc_target_describe}\n\n"
    numd_cat_table = (
        f"### Discrete Numerical and Categorical Features\n\n{numd_cat_describe}"
    )
    eda_table = numc_table + numd_cat_table
    write_md(experiment_doc, eda_table, "EDA_INSIGHTS")


if __name__ == "__main__":
    main()
