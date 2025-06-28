
FROM python:3.12-slim


WORKDIR /app


RUN apt-get update \
    && apt-get install -y netcat-openbsd gcc libpq-dev curl \
    && apt-get clean


RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root


COPY . .


EXPOSE 8000


CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
