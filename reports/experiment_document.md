# Experimentation Document

## Dataset Information

- **Source**: [Kaggle](https://www.kaggle.com/datasets/muhammadbinimran/housing-price-prediction-data/data)
- **Rows**: 40,000
- **Columns**: 6 (5 features + 1 target)
- **Continuous Features**: 1
- **Discrete Numerical Features**: 2
- **Continuous Numerical Features**: 2
- **Target Column**: `price`
- **Duplicate Rows**: None
- **Useless Columns**: None
- **Memory Usage**: ~1.8 MB

---

## Experiment Results

[//]: # (START:MODEL_EXPERIMENT_RESULTS)

|    | Model   | Hyperparameters   |   Accuracy |   F1 Score | Notes                   |
|---:|:--------|:------------------|-----------:|-----------:|:------------------------|
|  0 | log_reg | {}                |       0.81 |       0.81 | Baseline model          |
|  1 | rfr     | {}                |       0.85 |       0.85 | OK                      |
|  2 | xgbr    | {}                |       0.87 |       0.87 | Best performance so far |

[//]: # (END:MODEL_EXPERIMENT_RESULTS)

---

## EDA Insights

---

[//]: # (START:EDA_INSIGHTS)

### Continuous Numerical Features

|             |   count |      mean |        std |      min |    25% |    50% |    75% |    max |
|:------------|--------:|----------:|-----------:|---------:|-------:|-------:|-------:|-------:|
| square_feet |   40000 |   2005.67 |   575.603  |   1000   |   1511 |   2006 |   2505 |   2999 |
| year_built  |   40000 |   1985.41 |    20.7222 |   1950   |   1967 |   1985 |   2003 |   2021 |
| price       |   40000 | 224802    | 76133.4    | -36588.2 | 170012 | 224965 | 279370 | 492195 |

### Discrete Numerical and Categorical Features

|              |   count |   unique | top   |   freq |
|:-------------|--------:|---------:|:------|-------:|
| bedrooms     |   40000 |        4 | 3     |  10082 |
| bathrooms    |   40000 |        3 | 2     |  13417 |
| neighborhood |   40000 |        3 | rural |  13430 |

[//]: # (END:EDA_INSIGHTS)

---

## Project Conventions & Glossary

### Dataset Variables

- `entire_data`: Combined train and test data
- `df`: This variable can be either entire_data (combined train + test) or just train data depending on the context. But this is commonly used for the train data.
- `df_train`, `df_test`: Train and test data
- `df_bak`: Backup (copy) of the df
- `cat_cols`: Categorical columns
- `numd_cols`: Discrete numerical columns
- `numc_cols`: Continuous numerical columns
- `num_cols`: All numerical columns (numc_cols + numd_cols)
- `target`: Target variable
- `X`, `y`: Features and target variable
- `X_train`, `X_test`: Train and test splits of `X`
- `y_train`, `y_test`: Train and test splits of `y`
- `y_pred`: Prediction done by the model

### Model Abbreviations

- `lin_reg`: Linear Regressor
- `rfr`: Random Forest Regressor
- `knnr`: KNeighbors Regressor
- `svr`: Support Vector Regressor
- `dtr`: Decision Tree Regressor
- `gbr`: Gradient Boosting Regressor
- `etr`: Extra Trees Regressor

### Preprocessing Terms

- `tts`: Train-Test Split
- `pl`: Pipeline
- `ct`: Column Transformer
- `oe`: Ordinal Encoder
- `ohe`: One-Hot Encoder
- `le`: Label Encoder
- `ss`: Standard Scaler
- `mms`: Min-Max Scaler
- `reg`: Regressor model

> All column names and values in categorical columns follow `snake_case` format.

---
