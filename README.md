# House Price Prediction - ML API Service

![Python](https://img.shields.io/badge/python-3.12-blue) [![GitHub last commit (branch)](https://img.shields.io/github/last-commit/althaf-07/house-price-pred-ml/main)](https://github.com/althaf-07/house-price-pred-ml/commits/main/) [![GitHub License](https://img.shields.io/github/license/althaf-07/house-price-pred-ml?color=yellow)](https://opensource.org/license/mit)

Welcome! This is an ML API service that lets you submit house property data to get its predicted price.

## :compass: Table of Contents

- [:pushpin: Project Overview](#pushpin-project-overview)
- [:rocket: Getting Started](#rocket-getting-started)
- [:file_folder: Project Structure](#file_folder-project-structure)
- [:test_tube: Testing](#test_tube-testing)
- [:question: FAQ](#question-faq)
- [:warning: Known Issues](#warning-known-issues)
- [:mortar_board: Learned](#mortar_board-learned)
- [:handshake: Contributing](#handshake-contributing)
- [:bust_in_silhouette: Author](#bust_in_silhouette-author)
- [:envelope: Contact](#envelope-contact)
- [:page_facing_up: License](#page_facing_up-license)

---

## :pushpin: Project Overview

- **Project Name**: House Price Prediction
- **Dataset**: This project uses the [Housing Price Prediction Dataset](https://www.kaggle.com/datasets/muhammadbinimran/housing-price-prediction-data/data) from Kaggle. The dataset contains information about houses and their features, and is suitable for building models to predict house prices. It is provided in CSV format with approximately 5,000 rows and 12 columns.
- **Objective**: Build a supervised machine learning regression model to predict house prices from the given features.
- **Training Strategy**: Batch Training
- **Type of ML**: Supervised Learning
- **Type of Problem**: Regression
- **Evaluation Metrics**: $\mathrm{RMSE}$, $\mathrm{MAE}$, and $R^2$
- **Hardware**: This project doesn't have any specific hardware requirements. This is a very lightweight and simple project that is runnable on any modern machine.
- **OS**: This project was initially developed on a Devcontainer in an Ubuntu machine. I tried to maintain this project OS-independent, but there is no guarantee that it is.

---

## :rocket: Getting Started

Follow these steps to run the House Price Prediction ML API Service locally. This will start the API server at [http://localhost:8000](http://localhost:8000).

### 1. Install Prerequisites

- [Docker](https://docs.docker.com/engine/install/) (for Docker setup) or [uv](https://astral.sh/uv/) (for manual setup)
- [cURL](https://curl.se/) (for cURL requests) or Python `requests` module (for Python requests)

### 2. Run the API

#### Option 1 - Docker (Recommended)

```bash
docker run -p 8000:8000 althaf07/house-price-pred-ml
```

#### Option 2 - Manual

1. Clone the repository
    - **HTTPS**

        ```bash
        git clone https://github.com/althaf-07/house-price-pred-ml
        ```

    - **SSH**

        ```bash
        git clone git@github.com:althaf-07/house-price-pred-ml.git
        ```

1. Navigate to the project directory

    ```bash
    cd house-price-pred-ml
    ```

1. Install dependencies with uv

    ```bash
    uv sync --no-dev
    ```

1. Start the API server

    ```bash
    uv run uvicorn src.house_price_pred_ml.app:app \
    --reload --host 0.0.0.0 --port 8000
    ```

### 3. API Documentation

Once the server is up and running, explore the interactive API docs:

- [Swagger UI](http://localhost:8000/docs)
- [ReDoc](http://localhost:8000/redoc)

### 4. API Endpoints

#### 4.1 Health Check

Check if the API is up and running.

**Endpoint:** `GET /api/health`

**cURL Request:**

```bash
curl http://localhost:8000/api/health
```

**Python Request:**

```python
import requests

url = "http://localhost:8000/api/health"
response = requests.get(url)
if response.ok:
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")
```

**Expected Response:**

```json
{
    "status": "ok"
}
```

#### 4.2 Predict House Price

Send housing features to get a predicted price.

**Endpoint:** `POST /api/predict`

**Request Structure:**

| Field          | Type  | Description                              | Example |
| -------------- | ----- | ---------------------------------------- | ------- |
| `square_feet`  | float | Total area of the house                  | 2513    |
| `bedrooms`     | int   | Number of bedrooms                       | 3       |
| `bathrooms`    | int   | Number of bathrooms                      | 2       |
| `neighborhood` | enum  | Neighborhood type (rural, suburb, urban) | suburb  |
| `year_built`   | int   | Year the house was built                 | 2014    |

**Response Structure:**

| Field        | Type  | Description           | Example   |
| ------------ | ----- | --------------------- | --------- |
| `prediction` | float | Predicted house price | 242420.45 |

**cURL Request:**

```bash
curl -X POST http://localhost:8000/api/predict \
     -H "Content-Type: application/json" \
     -d '{
           "square_feet": 2513,
           "bedrooms": 3,
           "bathrooms": 2,
           "neighborhood": "suburb",
           "year_built": 2014
         }'
```

**Python Request:**

```python
import requests

url = "http://localhost:8000/api/predict"
payload = {
    "square_feet": 2513,
    "bedrooms": 3,
    "bathrooms": 2,
    "neighborhood": "suburb",
    "year_built": 2014
}
response = requests.post(url, json=payload)
if response.ok:
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")
```

**Expected Response:**

```json
{
    "prediction": 242420.45
}
```

---

## :file_folder: Project Structure

[//]: # "START:PROJECT_STRUCTURE"

```bash
house-price-pred-ml              # Root project directory
├── .devcontainer/               # Dev Container directory
│   ├── devcontainer.env         # Dev Container environment variables file
│   ├── devcontainer.json        # Dev Container configurations file
│   ├── Dockerfile               # Dev Container Dockerfile
│   └── post_create_script.sh     # Post-build setup script file
├── .git/                        # Git directory
├── .venv/                       # Python virtual environment directory
├── data/                        # Datasets directory
│   ├── interim/                 # Intermediate cleaned datasets directory
│   │   └── interim.csv          # Cleaned intermediate dataset CSV file
│   ├── processed/               # Train-test split datasets directory
│   │   ├── test.csv             # Test dataset CSV file
│   │   └── train.csv            # Training dataset CSV file
│   └── raw/                     # Raw and unprocessed datasets directory
│       └── raw.csv              # Original raw dataset CSV file
├── logs/                        # Log files directory
├── notebooks/                   # Jupyter notebooks directory
├── reports/                     # Reports and documentation directory
│   └── figures/                 # Generated figures directory
│       └── univariate/          # Univariate analysis figures directory
├── src/                         # Source code directory
│   └── house_price_pred_ml/     # Main Python package directory
│       ├── plot/                # Plotting scripts directory
│       │   └── univariate/      # Univariate plotting scripts directory
│       │       ├── cat_numd.py
│       │       └── numc.py      # Continuous numerical plots script file
│       ├── utils/               # Utility modules directory
│       │   ├── functions.py     # General utility functions file
│       │   ├── logger.py        # Logger configuration file
│       │   ├── tree.py          # Project directory tree generator script file
│       │   └── tree.yaml        # Directory descriptions file
│       ├── __init__.py          # Package initializer file
│       ├── app.py               # API endpoints for model serving script file
│       ├── clean_data.py        # Data cleaning script file
│       ├── config.py            # Configurations loader script file
│       ├── config.yaml          # Configurations file
│       ├── evaluate.py          # Model evaluation script file
│       ├── ingest_data.py       # Data ingestion script file
│       ├── main.py              # Main entry point script file
│       ├── predict.py           # Model prediction script file
│       ├── split_data.py        # Train-test data split script file
│       └── train.py             # Model training script file
├── tmp/                         # Temporary files directory
├── .editorconfig                # Editor configuration rules file
├── .gitattributes               # Git attributes file
├── .gitignore                   # Git ignore rules file
├── .pre-commit-config.yaml      # Pre-commit hook configuration YAML file
├── .python-version              # Python version specification file
├── CONTRIBUTING.md              # Contribution guidelines file
├── Dockerfile                   # Deployment build instructions Dockerfile
├── pyproject.toml               # Python dependencies and build configuration file
├── README.md                    # Project documentation and usage instructions file
└── uv.lock                      # uv dependency lock file
```

[//]: # "END:PROJECT_STRUCTURE"

## :test_tube: Testing

---

## :question: FAQ

---

## :warning: Known Issues

---

## :mortar_board: Learned

- Development Containers
- Using Section Markers to auto-generate parts of a file
- Set membership (`in`) is faster (O(1)) than list membership (O(n))
- Using a wrapper function around recursion for additional flexibility
- Storing strings in memory with `StringIO` from the `io` module
- Logging best practices
- Exception handling techniques
- Input data validation: **LBYL** (Look Before You Leap) vs **EAFP** (Easier to Ask Forgiveness than Permission)
- Understanding **TOCTOU** (Time-of-Check to Time-of-Use) issues
- Strong typing vs weak typing
- Static typing vs dynamic typing
- Nominal typing vs structural typing vs duck typing
- ISO standard: using a dot between seconds and milliseconds in timestamps
- Git branching strategies
- Git branch naming conventions (Conventional Branches)
- Git commit conventions (Conventional Commits)
- Using GitHub README badges (Shields)

---

## :handshake: Contributing

For contributing to this project, see the [CONTRIBUTING.md](CONTRIBUTING.md) file for details.

---

## :bust_in_silhouette: Author

**Althaf Muhammad**:

- [Email](mailto:zoory9900@gmail.com)
- [GitHub](https://github.com/althaf-07)

---

## :envelope: Contact

For questions, suggestions, or collaborations, feel free to reach out the author via [Email](mailto:zoory9900@gmail.com) or open an [issue](https://github.com/althaf-07/house-price-pred-ml/issues/new).

---

## :page_facing_up: License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---
