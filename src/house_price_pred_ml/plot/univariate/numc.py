from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from house_price_prediction.utils import parse_yaml, setup_logger


def plot_summary(df):
    df_describe = df.describe().T
    df_describe[]
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    plt.savefig('dataframe_image.png', bbox_inches='tight')
    plt.close()


def plot_box(df, col, col_cfg, ax):
    box_cfg = col_cfg.get("box_cfg", {})
    box_sns_kws = box_cfg.get("sns_kws", {})
    box_axs_kws = box_cfg.get("axs_kws", {})
    box_grid = box_cfg.get("grid", True)
    sns.boxplot(x=df[col], ax=ax, **box_sns_kws)
    ax.set(**box_axs_kws)
    ax.grid(box_grid)

def plot_hist(df, col, col_cfg, ax):
    hist_cfg = col_cfg.get("hist_cfg", {})
    hist_sns_kws = hist_cfg.get("sns_kws", {})
    hist_axs_kws = hist_cfg.get("axs_kws", {})
    hist_grid = hist_cfg.get("grid", True)
    hist_sns_kws["kde"] = hist_sns_kws.get("kde", True)
    sns.histplot(df[col], ax=ax, **hist_sns_kws)
    ax.set(**hist_axs_kws)
    ax.grid(hist_grid)


def main():
    log = setup_logger()
    config = parse_yaml(log)
    numc_cols = config["cols"]["numc"]
    target = config["cols"]["target"]
    plt_cfg = config.get("plt_cfg", {})

    try:
        df_path = Path(config["paths"]["data"]["processed"]["train"])
        df = pd.read_csv(df_path, usecols=numc_cols + [target])
        log.success("Loaded dataset")
    except Exception:
        log.exception("Failed to load dataset")
        raise

    save_dir = Path(config["paths"]["reports"]["univariate"])
    save_dir.mkdir(exist_ok=True, parents=True)

    for col in numc_cols + [target]:
        fig, axs = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle(f"Distribution of {col}", fontsize=14)
        save_path = save_dir / f"{col}.png"
        col_cfg = plt_cfg.get(col, {})
        if save_path.exists() and not col_cfg.get("force_generate", False):
            log.info(f"⚠️ : {col} already exists, so skipped it.")
            continue
        plot_hist(df, col, col_cfg, axs[0])
        plot_box(df, col, col_cfg, axs[1])
        plt.tight_layout()
        plt.savefig(save_path, bbox_inches="tight")
        plt.close()
        log.success(f"Saved: {save_path}")


if __name__ == "__main__":
    main()
