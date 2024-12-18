# Курсовой проект по модулю ООП

Информация о вакансиях с платформы hh.ru, сохраняет ее в файл и позволяет работать с ней: добавлять, фильтровать, удалять.

## Описание проекта

   Проект включает модули

 - Модуль (vacancy) - служит для работы с вакансиями, поддерживает метод сравнения вакансий между собой по зарплате
 - Модуль (vacancy_api) - служит для работы с платформой hh.ru. Реализованные в нем классы умеют подключаться к API и получать вакансии
 - Модуль (vacancy_storage) - содержит методы для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях.


## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/Tooxa85/Project2/feature/coursework2
```
2. Установите зависимости:
```
poetry install
```
## Использование:

Проект содержит модуль main, служащий для взаимодействовать с пользователем через консоль

## Тесты:
 - Для тестирования используются Mock и patch