# Установка с использование Docker (рекомендованно)

Для начала установить [Docker](https://www.docker.com/).

Затем установите [Docker Compose](https://docs.docker.com/compose/). Если уже установленно, то нет необходимости.

Скопируйте репозиторий на свое устройство используя [git](https://git-scm.com/):

```bash
git clone https://github.com/DataScience-py/MetricHub.git
```

Перейдите в директорию проекта:

```bash
cd MetricHub
```

Запустите скрипт:

```bash
docker-compose up -d
```

Для того чтобы остановить сервер, используйте следующую команду:

```bash
docker-compose down
```

На вашем компьютере откройте браузер и введите в адресную строку: `http://localhost:8000/`.
