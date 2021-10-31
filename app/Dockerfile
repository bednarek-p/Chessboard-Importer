FROM nvidia/cuda:11.3.1-cudnn8-runtime-ubuntu20.04

ENV PYTHONUNBUFFERED 1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
# RUN pip install -U pip setuptools
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.9 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN pip install poetry==1.1.5
WORKDIR /code

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi
COPY ./code .
