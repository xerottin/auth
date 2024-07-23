## Инструкция

Для локального тестирования необходимо создать виртуальное окружение командой `python3 -m venv venv` и активировать его.
Команда `venv\Scripts\activate.bat` - для Windows; `source venv/bin/activate` - для Linux и MacOS.

Затем необходимо перейти в папку и установить зависимости командой `pip install -r requirements.txt`.

С начала нужно запустить redis `redis-server`

затем celery `celery -A celery_worker worker --loglevel=info`

Затем необходимо перейти в папку `src` командой `cd src` и запустить команду `uvicorn main:app --reload` для запуска
сервера `uvicorn`.

каждую из них нужно запустить в отдельный терминал в одном окружение

После этого можно зайти в браузере по адресу `http://localhost:8000/docs` для просмотра доступных эндпоинтов.
