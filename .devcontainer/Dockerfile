ARG VARIANT=1-3.12-bookworm
FROM mcr.microsoft.com/devcontainers/python:$VARIANT

SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive

# hadolint ignore=DL3009
RUN apt-get update

COPY ./private/devcontainer/dockerfile_root_script.sh* /tmp/
RUN if [ -f /tmp/dockerfile_root_script.sh ]; then \
        /tmp/dockerfile_root_script.sh && rm -f /tmp/dockerfile_root_script.sh; \
    fi

# hadolint ignore=DL3059
RUN rm -rf /var/lib/apt/lists/*

USER vscode

ARG NODE_VERSION=24.7.0
ENV NVM_DIR=/usr/local/share/nvm
RUN source $NVM_DIR/nvm.sh && \
    nvm install $NODE_VERSION && \
    nvm alias default $NODE_VERSION && \
    nvm use default

ARG UV_VERSION=0.8.15
RUN curl -LsSf https://astral.sh/uv/$UV_VERSION/install.sh | sh

ARG HADOLINT_VERSION=v2.13.1
RUN curl -Lo ~/.local/bin/hadolint https://github.com/hadolint/hadolint/releases/download/$HADOLINT_VERSION/hadolint-linux-x86_64 && \
    chmod +x ~/.local/bin/hadolint

COPY ./private/devcontainer/dockerfile_vscode_script.sh* /tmp/
RUN if [ -f /tmp/dockerfile_vscode_script.sh ]; then \
        /tmp/dockerfile_vscode_script.sh && rm -f /tmp/dockerfile_vscode_script.sh;\
    fi

ENV DEBIAN_FRONTEND=dialog
