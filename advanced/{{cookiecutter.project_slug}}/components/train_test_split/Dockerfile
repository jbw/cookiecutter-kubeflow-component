FROM python:3.8-slim-buster

ARG PIP_PACKAGES

# python
ENV PYTHONHASHSEED=0
ENV TF_CPP_MIN_LOG_LEVEL=3
ENV PYTHONUNBUFFERED=1
# prevents python creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# pip
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get install -y --no-install-recommends git g++ gcc \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove gcc g++ \
    && pip install --no-cache-dir -r requirements.txt

WORKDIR /code
COPY components/train_test_split/ components/train_test_split
COPY components/common/ components/common
COPY train_test_split.py train_test_split.py
