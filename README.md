# Тестовое задание "Разработка системы управления библиотекой"

## Описание

Необходимо разработать консольное приложение для управления библиотекой книг.
Приложение должно позволять добавлять, удалять, искать и отображать книги.
Каждая книга должна содержать следующие поля:

- id (уникальный идентификатор, генерируется автоматически)
- title (название книги)
- author (автор книги)
- year (год издания)
- status (статус книги: “в наличии”, “выдана”)

## Требования

* Добавление книги: Пользователь вводит title, author и year, после чего книга добавляется в библиотеку с уникальным id
  и статусом “в наличии”.
* Удаление книги: Пользователь вводит id книги, которую нужно удалить.
* Поиск книги: Пользователь может искать книги по title, author или year.
* Отображение всех книг: Приложение выводит список всех книг с их id, title, author, year и status.
* Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).

### Дополнительные требования

* Реализовать хранение данных в текстовом или json формате.
* Обеспечить корректную обработку ошибок (например, попытка удалить несуществующую книгу).
* Написать функции для каждой операции (добавление, удаление, поиск, отображение, изменение статуса).
* Не использовать сторонние библиотеки.

Будет плюсом:

* Аннотации: Аннотирование функций и переменных в коде.
* Документация: Наличие документации к функциям и основным блокам кода.
* Описание функционала: Подробное описание функционала приложения в README файле.
* Тестирование.
* Объектно-ориентированный подход программирования.

## Установка и запуск

```bash
poetry install
```

```bash
poetry run python -m main
```

## Тестирование

```bash
poetry run python -m unittest tests.py
```

## Структура проекта

```
tz-library/
├── actions.py - функции для работы с библиотекой
├── exceptions.py - Исключения
├── manager.py - функции для работы с хранением данных
├── main.py - главный файл программы
└── tests.py - тесты
```

## Пример работы программы

После запуска программы, пользователь видит следующее меню:

```
Добро пожаловать в библиотеку!
1. Добавить книгу
2. Удалить книгу
3. Найти книгу
4. Показать все книги
5. Изменить статус книги
6. Выход
```

### Добавление книги

1. Пользователь выбирает пункт меню “Добавить книгу”.
2. Далее пользователь вводит title, author и year книги.
3. Пользователь видит сообщение “Книга добавлена” и пользователю предлагается продолжить добавление книги или выйти в
   главное меню возвращается в главное меню.

### Удаление книги

1. Пользователь выбирает пункт меню “Удалить книгу”.
2. Далее пользователь вводит id книги, которую нужно удалить.
3. Пользователь видит сообщение “Книга удалена” и пользователю предлагается продолжить удаление книги или выйти в
   главное меню.

### Поиск книги

1. Пользователь выбирает пункт меню “Найти книгу”.
2. Далее пользователь вводит значение поиска.
3. Пользователь видит список найденных книг и пользователю предлагается продолжить поиск книги или выйти в главное меню.

### Отображение всех книг

1. Пользователь выбирает пункт меню “Показать все книги”.
2. Пользователь видит список всех книг с их id, title, author, year и status.

### Изменение статуса книги

1. Пользователь выбирает пункт меню “Изменить статус книги”.
2. Далее пользователь вводит id книги и новый статус.
3. Пользователь видит сообщение “Статус книги изменен” и пользователю предлагается продолжить изменение статуса книги
   или выйти в главное меню.
