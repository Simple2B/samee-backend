# samee

## Workflow


# samee-develop



## Set up

To successfully build containers, you must have a `.env` file in a `root` folder that must contain all secret variables. Alse u will need to download twilio.

### Set up virtual environment:

### Steps of downloading twilio:
        Link for dowloading twilio for basic OS:
            https://www.twilio.com/docs/sms/quickstart/python

### Set up poetry and all dependencies:
    Firstly, u need a poetry, u can use pip command to download it :
        pip install poetry

    To download all dependencies u need execute next command:
        poetry install



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

## Code update script

If changes have been made to the code of any part of the project, the following scenario should be followed:

1. Push changes to the GitHub repository.

2. Stop all docker containers (execute `docker-compose down` command).

3. Update the version of container`s image which up the part that you have changed (increase by one point).

For example, if the API Server is changed, update the version of webapi image:

   from

   ```bash
   webapi:
      image: ehealtho/webapi:1.1
   ```

   to

   ```bash
   webapi:
      image: ehealtho/webapi:1.2
   ```

4. If the changes concerned the frontend part, additional steps must be taken:

   1. Go to `webapp` folder: (execute `cd webapp` command):
   2. Build the app for production to the `webapp/build` folder: execute `npm run build` command (see more about this command in `webbapp/READMI.md` file)
   3. Go to the eLucide-dev folder where `docker-compose.yaml` file is placed (execute `cd ..` command)
   4. Update the version of `webapp` container`s image by one point. For example

      from

      ```bash
      webapp:
         image: ehealtho/webapp:1.1
      ```

      to:

      ```bash
      webapp:
         image: ehealtho/webapp:1.2
      ```

5. Log in to the ehealtho account on DockerHub (execute `docker login` command). Enter credentials (username (`ehealtho`) & password);

6. Rebuild all containers (execute `docker-compose build` command).

7. Push all containers to the Docker Hub (execute `docker-compose push`)

8. If you wanna logout from the docker hub account, execute `docker logout` command.
