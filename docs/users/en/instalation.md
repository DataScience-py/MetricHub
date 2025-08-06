# Installing using Docker (recommended)

First install [Docker](https://www.docker.com/).

Then install [Docker Compose](https://docs.docker.com/compose/). If you already have it installed, then there is no need.

Copy the repository to your device using [git](https://git-scm.com/):

```bash
git clone https://github.com/DataScience-py/MetricHub.git
```

Go to the project directory:

```bash
cd MetricHub
```

Run the script:

```bash
docker-compose up -d
```

To stop the server, use the following command:

```bash
docker-compose down
```

On your computer, open a browser and enter in the address bar: `http://localhost:8000/`.
