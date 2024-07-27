# bit-test-task

## Запуск:
0. Установка зависимостей:
`
poetry install
`
1. Заполните файл `.env` по подобию `sample.env`
2. Выполните создание таблиц и тестовых данных:
`
python database/database_init.py
`
3. Запустите приложение:
`
python app/main.py
`