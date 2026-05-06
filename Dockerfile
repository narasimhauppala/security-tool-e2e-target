FROM python:3.9-slim-bullseye

LABEL org.opencontainers.image.source="https://github.com/narasimhauppala/security-tool-e2e-target"
LABEL org.opencontainers.image.description="Security Tool company-style E2E target image"
LABEL org.opencontainers.image.licenses="MIT"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip \
    && python -m pip install --no-cache-dir -r /app/requirements.txt

COPY app /app/app

CMD ["python", "-m", "app.main"]
