FROM python:3.8

WORKDIR /app

RUN apt-get update
RUN apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev
RUN python -m pip install  --no-cache-dir --upgrade pip
RUN pip install 'poetry==1.1.11'
COPY pyproject.toml ./
COPY poetry.lock ./
RUN poetry install --no-interaction --no-dev

COPY . .

EXPOSE 5000

ENTRYPOINT [ "flask" ]
CMD ["run", "--host=0.0.0.0", "--port=5000"]
