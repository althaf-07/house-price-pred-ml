ARG VARIANT=3.12-slim-bookworm 
ARG UV_VERSION=0.7.2

FROM python:${VARIANT}

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get -y install --no-install-recommends curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/${UV_VERSION}/install.sh | sh && \
    mv /root/.local/bin/uv /usr/local/bin/
    
COPY uv.lock pyproject.toml ./

RUN uv sync --no-install-project --no-editable --no-dev

RUN adduser --disabled-password --gecos '' appuser

COPY --chown=appuser:appuser src/house_price_pred_ml/predict.py src/house_price_pred_ml/main.py src/house_price_pred_ml/
COPY --chown=appuser:appuser models/pl.joblib models/   

USER appuser

CMD ["uv", "run", "uvicorn", "src.house_price_pred_ml.main:app", "--host", "0.0.0.0", "--port", "8000"]
