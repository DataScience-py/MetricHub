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

# Installation Local Guide (no recommended)

First, install [python](https://www.python.org/downloads/). The recommended version is 3.12.11.

Next, install [poetry](https://python-poetry.org/docs/). Use the method that is most convenient for you.

Copy the repository to your device using [git](https://git-scm.com/):

```bash
git clone https://github.com/DataScience-py/MetricHub.git
```

Go to the project directory:

```bash
cd MetricHub
```

Create a virtual environment (using poetry):

```bash
poetry env use python
```

Then activate it:

```bash
poetry env activate
```

Go to the script run directory:

```bash
cd src
```

Then run the script:

```bash
python main.py --port 8000 --host 0.0.0.0
```

This will start a local server on your device. On your computer, open a browser and type in the address bar: `http://localhost:8000/`.
