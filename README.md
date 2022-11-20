# sovcombank_hakaton

# команда "Фоксики"

## Структура проекта
* клиентская часть выполнена на фреймворке ```Angular```
* серверная часть реализована на python, фреймворк django + DjangoRestFramework + SimpleJWt + Celery
* хранение данных - СУБД Postgresql
* кэширование данных - redis
* асинхронная очередь заданий - Celery + rabbitmq  

## Основная идея проекта
* выполнение клиентских запросов через асинхронную очередь заданий
* возврат данных клиенту через высокоскоростной кэш Redis

## запуск проекта
Для запуска вам потребуется ЭВМ под управлением ОС Linux + docker
Для развёртывания проекта вам необходимо:
* клонировать репозоторий в локальную папку.
* создать локальную папку ```https://t.me/joinchat/crxpZ3dvhPBiMWYy``` и дать ей разрешения 777 
* выполнить запуск контейнеров: 
```shell
docker-compose -d docker-compose.dev.yml up -d --build
```

## Тестовый суперпользователь
* login ```scb```
* password ```ScbPassword```


* Клиентская часть доступна по адресу: 127.0.0.1:4101
* Api доступен по адресу: 127.0.0.1:4101/api/v1
* swagger доступен по адресу: http://127.0.0.1:4101/api/v1/swagger/
* Административный доступ к данным: http://127.0.0.1:4101/api/v1/admin/

##ci-cd
настройка непрерывной интеграции в проекте: ```./github/workflows/deploy.yml```