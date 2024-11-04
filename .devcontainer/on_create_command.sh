curl -LsSf https://astral.sh/uv/install.sh | sh
. $HOME/.cargo/env
uv venv --allow-existing ${UV_PROJECT_ENVIRONMENT}
