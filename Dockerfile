FROM python:3.9-slim-buster
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install --upgrade pip
RUN pip install poetry==1.2.2
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi
COPY ./ /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]