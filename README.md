Пример rest-api на litestar с crud таблицы user.

Инструменты изпользовались из тз.

1) склонируйте git репозиторий

2) в деректории litestar_crud  создайте файл .env и заполните его содержимым

user=postgres
password=postgres
host=database:5432
database=postgres

3) выполните по очереди команды для docker-compose (миграции отдельно накатывать не надо)

docker-compose build

docker-compose up

4) помотрите на swagger ui через браузер

http://127.0.0.1:8080/schema/swagger

2 часа
