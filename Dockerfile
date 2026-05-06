FROM python:3.11-slim

LABEL org.opencontainers.image.source="https://github.com/narasimhauppala/security-tool-e2e-target"
LABEL org.opencontainers.image.description="Security Tool company-style E2E target image"
LABEL org.opencontainers.image.licenses="MIT"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml /app/pyproject.toml
COPY app /app/app
RUN python -m pip install --upgrade pip \
    && python -m pip install --no-cache-dir .

EXPOSE 8080

CMD ["python", "-m", "app.main"]
