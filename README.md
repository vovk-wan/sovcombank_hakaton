# sovcombank_hakaton

## поднимаем контейнеры на локальной машине для разработки
```shell
docker-compose -d docker-compose.dev.yml up -d --build
```

контейнер фронта можно удалить, если он не нужен.

фронт доступен по адресу: 127.0.0.1:4101
апи доступен по адресу: 127.0.0.1:4101/api/v1
swagger доступен по адресу: http://127.0.0.1:4101/api/v1/redoc/
swagger доступен по адресу: http://127.0.0.1:4101/api/v1/swagger/
админка джанго доступна по адресу: http://127.0.0.1:4101/api/v1/admin/
админка джанго доступна по адресу: http://127.0.0.1:4101/api/v1/admin/

## установка backend

* найти линукс
* установить докер, докер-компост, гит
* сделать гит клон проекта
* выполнить docker-compose up --build -d
** не забыть про 2 (два) .env
..
