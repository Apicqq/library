# Библиотека у дома - Тестовое задание

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)


## Ключевые возможности сервиса
### Веб-интерфейс:
- Адаптивная страница регистрации (через одну форму может зарегистрироваться как читатель, так и библиотекарь)
- Взаимодействие с имеющимися книгами в библиотеке (можно взять книгу на руки, вернуть её, просмотреть список всех имеющихся книг.)
- Просмотр имеющихся у пользователя книг на руках (страница "Мои книги")
- Список должников для библиотекарей (отображает список пользователей, у которых в данный момент есть книги на руках)
- Копирование названия книги при помощи отдельной кнопки (реализовано при помощи JavaScript)
### Админ-панель:
- Просмотр, редактирование, удаление пользователей
- Просмотр, редактирование, удаление книг
- Фильтрация по пользователям (когда-либо брал книгу на руки, есть книги на руках)
- История изменений книг

### API:
- Аутентификация с помощью токенов (библиотека djoser)
- Просмотр списка книг в библиотеке
- Получение/возврат книг на руки
- Получение списка книг у пользователя на руках


В текущей реализации проект использует базу данных SQLite, но при необходимости можно без проблем перейти и на боевой вариант, например, MySQL либо Postgres.

## Использованные при реализации проекта технологии
 - Python 3.10
 - Django
 - DRF
 - немного JavaScript
 - drf-yasg
 - factory-boy
 - Faker

## Как установить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Apicqq/library
```

```
cd <путь_до_папки_с_проектом>/library
```

Установить зависимости проекта:

* Если у вас установлен Poetry:
    ```
    poetry install (--with testing для тестирования, --with development для
  наполнения тестовой БД данными)
    ```
* Либо через стандартный менеджер зависимостей pip:
    
  Создайте виртуальное окружение:

    ```
    python3 -m venv venv
    ```
  Активируйте его:

    * Если у вас Linux/macOS
    
        ```
        source venv/bin/activate
        ```
    
    * Если у вас windows
    
        ```
        source venv/scripts/activate
        ```
    
        ```
        python3 -m pip install --upgrade pip
        ```
  И установите зависимости:
    ```
    pip install -r requirements.txt
    ```

Запустить проект (в зависимости от выбранного менеджера зависимости) можно командами:
- `poetry run python library/manage.py runserver`
- `python library/manage.py runserver`

### Наполнение тестовой БД данными

Если вы хотите протестировать приложение, для этого вы можете использовать реализованные фабрики при помощи management-команды `fill-test-db`. Она имеет следующую сигнатуру:
```
[-b, --books] [-r, --readers] [-l, --librarians] [-a AMOUNT] 
```

### Документация

Для проекта реализована API-документация.

После запуска приложения она будет доступна по адресам:

Для документации Swagger:

[http://127.0.0.1:8000/api/swagger](http://127.0.0.1:8000/api/swagger)


Для документации ReDoc:

[http://127.0.0.1:8000/api/redoc](http://127.0.0.1:8000/api/redoc)
## Автор проекта

[Никита Смыков](https://github.com/Apicqq)


