FROM python:3.14
LABEL authors="fanielhabte"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /data-forge

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/data-forge/src"

COPY pyproject.toml requirements.txt* uv.lock* ./
RUN uv pip install --system -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "main.py"]