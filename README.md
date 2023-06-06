# Тестовое задание в Фабрику Решений

## Запуск проекта
Нужно добавить токен в environment файле docker-compose.yml
```
- SMS_SERVICE_AUTH_TOKEN=<TOKEN>
```

```
docker-compose build
docker-compose up
```

## Swagger

```
http://localhost:8000/docs
```

## Дополнительные задания

3. подготовить docker-compose для запуска всех сервисов проекта одной командой
5. сделать так, чтобы по адресу /docs/ открывалась страница со Swagger UI и в нём отображалось описание разработанного API. Пример: https://petstore.swagger.io
6. реализовать администраторский Web UI для управления рассылками и получения статистики по отправленным сообщениям