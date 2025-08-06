# Гайд по установке

Для начала установить [python](https://www.python.org/downloads/). Рекомендованная версия 3.12.11.

Далее установите [poetry](https://python-poetry.org/docs/). Используйте для этого удобный для вас способ.

Скопируйте репозиторий на свое устройство используя [git](https://git-scm.com/):

```bash
git clone https://github.com/DataScience-py/MetricHub.git
```

Перейдите в директорию проекта:

```bash
cd MetricHub
```

Создайте виртуальное окружение (используя poetry):

```bash
poetry env use python
```

Затем активируйте его:

```bash
poetry env activate
```

Перейдите в директорию запуска скрипта:

```bash
cd src
```

Затем запустите скрипт:

```bash
python main.py --port 8000 --host 0.0.0.0
```

Это запустит на вашем устройстве локальный сервер. На вашем компьютере откройте браузер и введите в адресную строку: `http://localhost:8000/`.
