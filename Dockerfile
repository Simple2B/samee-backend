FROM python:3.8

WORKDIR /app

RUN apt-get update
RUN apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev
RUN python -m pip install  --no-cache-dir --upgrade pip
# TODO: Add install poetry + self update
COPY pyproject.toml ./
COPY poetry.lock ./
# TODO: Refactor
RUN poetry install --no-interaction


COPY . .

EXPOSE 5000

ENTRYPOINT [ "flask" ]
CMD ["run", "--host=0.0.0.0", "--port=5000"]
