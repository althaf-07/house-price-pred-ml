from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from house_price_prediction.utils import parse_yaml, setup_logger


def plot_pie(df, col, col_cfg, ax):
    pie_cfg = col_cfg.get("pie_cfg", {})
    pie_plt_kws = pie_cfg.get("plt_kws", {})
    pie_axs_kws = pie_cfg.get("axs_kws", {})
    pie_plt_kws["autopct"] = pie_plt_kws.get("autopct", "%0.2f%%")
    values = df[col].value_counts()
    ax.pie(values, labels=values.index, **pie_plt_kws)
    ax.set(**pie_axs_kws)


def plot_count(df, col, col_cfg, ax):
    count_cfg = col_cfg.get("count_cfg", {})
    count_sns_kws = count_cfg.get("sns_kws", {})
    count_axs_kws = count_cfg.get("axs_kws", {})
    count_grid = count_cfg.get("grid", True)
    sns.countplot(x=df[col], ax=ax, **count_sns_kws)
    ax.set(**count_axs_kws)
    ax.grid(count_grid)


def main():
    log = setup_logger()
    config = parse_yaml(log)
    cat_cols = config["cols"]["cat"]
    numd_cols = config["cols"]["numd"]
    plt_cfg = config.get("plt_cfg", {})

    try:
        df_path = Path(config["paths"]["data"]["processed"]["train"])
        df = pd.read_csv(df_path, usecols=cat_cols + numd_cols)
        log.success("Loaded dataset")
    except Exception:
        log.exception("Failed to load dataset")
        raise

    save_dir = Path(config["paths"]["reports"]["univariate"])
    save_dir.mkdir(exist_ok=True, parents=True)

    for col in cat_cols + numd_cols:
        fig, axs = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle(f"Distribution of {col}", fontsize=14)
        save_path = save_dir / f"{col}.png"
        col_cfg = plt_cfg.get(col, {})
        if save_path.exists() and not col_cfg.get("force_generate", False):
            log.info(f"⚠️ : {col} already exists, so skipped it.")
            continue
        plot_count(df, col, col_cfg, axs[0])
        plot_pie(df, col, col_cfg, axs[1])
        plt.tight_layout()
        plt.savefig(save_path, bbox_inches="tight")
        plt.close()
        log.success(f"Saved: {save_path}")


if __name__ == "__main__":
    main()
