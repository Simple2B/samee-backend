# samee

## Set up

To successfully build containers, you must have a `.env` file in a `root` folder that must contain all secret variables. Alse u will need to download twilio.

### Set up virtual environment
First of all, u need to set up an virtual environment, where u will do further set ups. You can do it by using next code:

    python3.9 -m /path/to/directory

For activating virual environment use:

    source /path/to/venv/bin/activate

Deactivating:

    deactivate

### Steps of downloading twilio
Link for dowloading twilio for basic OS:

    https://www.twilio.com/docs/sms/quickstart/python

### Set up poetry and all dependencies
Firstly, u need a poetry, u can use pip command to download it :

    pip install poetry

To download all dependencies u need execute next command:

    poetry install

### Prepare database

Execute following lines under virtual environment

    flask drob-db
    flask create-db


## Useful commands

1. To build and up all containers, execute:

   ```bash
   docker-compose up -d --build
   ```

2. To build and up a particular container, execute:

   ```bash
   docker-compose up -d --build <name of container>
   ```

3. To stop all containers, execute:

   ```bash
   docker-compose down
   ```

4. See logs of all containers:

   ```bash
   docker-compose logs -f
   ```

5. See logs of a particular container:

   ```bash
   docker-compose logs -f <name of container>
   ```
