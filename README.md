## Запуск проекта в Docker контейнере
* Установите Docker
* Параметры запуска описаны в файлах `docker-compose.yml`
* Запустите docker compose:
```bash
docker-compose up --build
```
  > После сборки появятся 2 контейнера:
  > 1. контейнер базы данных **db**
  > 2. контейнер приложения **backend**

* Дополнительные команды очистки докера:
```bash
docker stop $(docker ps -aq) && docker rm $(docker ps -aq)
docker rmi $(docker images -a -q)
docker volume prune
```
Админку можно посмотреть по адресу http://127.0.0.1:8000/admin. Нужно создать учетку админа, написав команду
```bash
docker exec -it <container_id> python manage.py createsuperuser
```
