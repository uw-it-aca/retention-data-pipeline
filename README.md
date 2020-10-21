# retention-data-pipeline
App for getting data into RAD app

This is a docker image that connects to the EDW and a small Django app that fetches and stores data.  Currently it fetches students for a given year and quarter combination

Notes:
I don't know what broke/changed since I last worked on this, but for whatever reason tdsodbc has to be installed manually despite being included in the Dockerfile.


Using the container
1. Set environemntal variables for the EDW user and password

    `export EDW_USER="netid\\put_netid_here"`

    `export EDW_PASSWORD="password"`

2. Build and start the container

    `docker-compose up -d -build`
3. Connect to the container.
    Get the container id and connect to the shell on that container

    `docker ps`     This lists all containers, get the id from here

    `docker exec -u 0 -it [container ID] /bin/bash`

    Example:

    command:
    `docker ps`

    output:
    <pre>
        CONTAINER ID        IMAGE                         COMMAND                  CREATED             STATUS              PORTS                    NAMES
    770330ba50ed        retention-data-pipeline_app   "dumb-init --rewrite…"   6 minutes ago       Up 6 minutes        0.0.0.0:8000->8000/tcp   app
    </pre>

    command:
    `docker exec -u 0 -it 770330ba50ed /bin/bash`

    output (this is the container shell):
    `root@770330ba50ed:/app#`

4. Install tdsodbc

    (Again, I don't know why this needs to be installed again after docker installs it and why it worked before.  This is a blocker level bug to using this container)
    
    `apt-get install tdsodbc`
    
5. Either be on the UW network physically or set up the Big IP VPN client to get a campus IP, EDW is restricted to on-campus networking only (this applies to the host running the docker container, eg your workstation)

6. Activate the virtualenv

    `source bin/activate`

7. Run the test command to verify the connection

    `./manage.py edw_connect`
    
    Should take ~30-90 seconds, will only output on error.  You can use the dbshell to see the locally stored data