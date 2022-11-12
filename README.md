# sovcombank_hakaton

## поднимаем контейнеры на локальной машине для разработки
```shell
docker-compose -d docker-compose.dev.yml up --build -d scb-redis scb-rabbit scb-postgres scb-pgadmin scb-backend scb-frontend
```

контейнер фронта можно удалить, если он не нужен.

фронт доступен по адресу: 127.0.0.1:4101
апи доступен по адресу: 127.0.0.1:4101/api/v1

## установка backend

* найти линукс
* установить докер, докер-компост, гит
* сделать гит клон проекта
* выполнить docker-compose up --build -d
** не забыть про 2 (два) .env
.
