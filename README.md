# API для управления списком задач
Учебный проект - создание приложения на Django
## Навигация
- [Установка](#установка)
  - [Клонирование репозитория](#клонирование-репозитория)
- [Панель администратора](#панель-администратора)
  - [Адрес](#адрес)
  - [Креды суперпользователя](#креды-суперпользователя)
  - [Возможные операции в алминке](#возможные-операции-в-админке)
- [Api](#api)
  - [Создание задачи](#создание-задачи)
  - [Получение всех задач](#получение-всех-задач)
  - [Получение задачи по ID](#получение-задачи-по-id)
  - [Обновление задачи по ID](#обновление-задачи-по-id)
  - [Удаление задачи по ID](#удаление-задачи-по-id)
  - [Фильтрация](#фильтрация)
  - [Сортировка](#сортировка)
- [Особенности](#особенности)
  - [Обработка возможных ошибок](#обработка-возможных-ошибок)
  - [Serializers](#serializers)
  - [Обработка API](#обработка-api)
  - [Стиль кода](#стиль-кода)
- [Структура проекта](#структура-проекта)      


## Установка
Предварительно установите Docker с официального репозитория [https://docker.qubitpi.org/desktop/install/windows-install/](https://docker.qubitpi.org/desktop/install/windows-install/)
### Клонирование репозитория
```bash
git clone https://github.com/AlexOsipenko/todoapi.git
cd todoapi
cd todo_project
```
### Создание и запуск Docker-контейнера
Используйте Docker Compose для создания контейнера и запуска приложения:
```bash
docker-compose up --build
```
### Доступ к приложению
После успешного запуска приложение будет доступно по адресу:
`http://127.0.0.1:8000/`

## Панель администратора

<p align="center">
 <img src="https://github.com/user-attachments/assets/f730c318-6c8c-4212-a31e-06934d82ca2d" alt="admin">
</p>

### Адрес
`http://127.0.0.1:8000/admin/`
### Креды суперпользователя
user: `admin`
password: `admin`
### Возможные операции в админке
**Список тасков**
- Выберите "Tasks" На главной странице админ-панели
- Вы увидите таблицу со списком всех задач, которые имеют поля Tttle, Description и Status.
 
![image](https://github.com/user-attachments/assets/a380569f-ad78-461d-8c37-ef15f8f3b1de)


**Добавление новой задачи**
- На странице списка задач нажмите кнопку "Add Task" в верхней правой части экрана.

- Заполните поля: Введите необходимые данные:

Title: Обязательное поле.
Description: Необязательное поле.
Status: Выберите один из трех вариантов: "in_process" (в процессе), "completed" (завершено), "canceled" (отменено).
- Сохраните задачу: После заполнения всех необходимых полей нажмите кнопку "Save" в нижней части страницы.

![image](https://github.com/user-attachments/assets/26983e80-3ea0-435d-9e83-1b2818ccfccf)

**Редактирование существующей задачи**
- На странице списка задач щелкните на названии задачи, которую хотите изменить.

- Отредактируйте поля по мере необходимости.

- Нажмите кнопку "Save" для обновления информации о задаче.

**Удаление задачи**
- На странице списка задач щелкните на названии задачи, которую хотите удалить.

- На странице редактирования задачи прокрутите вниз и найдите кнопку "Delete" в правом нижнем углу.

- Подтвердите удаление, нажав на кнопку "Yes, I'm sure" на открывшейся странице.
## API
Для отправки запросов, мною было выбрано приложение Postman 
<img src="https://github.com/user-attachments/assets/71dca4a1-7847-4417-b458-ba392b09afc2" width="20" alt="postman">

### **Создание задачи**
- URL: [http://127.0.0.1:8000/api/tasks/](http://127.0.0.1:8000/api/tasks/)
- Метод: `POST`
- Пример body:

![image](https://github.com/user-attachments/assets/2a477af0-2df8-4429-a5fa-96fdffc28717)

- Ответ: `201 Created`

![image](https://github.com/user-attachments/assets/fb94e478-45f6-4b67-aa58-ba2a9d434166)

### **Получение всех задач**
- URL: [http://127.0.0.1:8000/api/tasks/](http://127.0.0.1:8000/api/tasks/)
- Метод: `GET`
- Ответ: `200 OK`

![image](https://github.com/user-attachments/assets/e97f9094-69e9-428b-887f-0db202e4e8b6)


### **Получение задачи по ID**
- URL: [http://127.0.0.1:8000/api/tasks/{id}/](http://127.0.0.1:8000/api/tasks/2/)
- Метод: `GET`
- Пример URL: `http://127.0.0.1:8000/api/tasks/2/`
- Ответ: `200 OK` или `404 Not Found`, если задача не найдена

 
![image](https://github.com/user-attachments/assets/9f5d336f-46f3-4954-9576-04b7036bfb39)

### **Обновление задачи по ID**
- URL: [http://127.0.0.1:8000/api/tasks/{id}/](http://127.0.0.1:8000/api/tasks/3/)
- Метод: `PATCH`
- Пример URL: `http://127.0.0.1:8000/api/tasks/3/`
- Пример body:

![image](https://github.com/user-attachments/assets/e609af06-f948-4104-861d-ca3f8f092c0d)

- Ответ: `200 OK` или `404 Not Found`, если задача не найдена. Если обновление невозможно, то `400 Bad Request`

![image](https://github.com/user-attachments/assets/4f15f80f-4f21-4576-8dc8-9dddcd559070)

### **Удаление задачи по ID**
- URL: [http://127.0.0.1:8000/api/tasks/{id}/](http://127.0.0.1:8000/api/tasks/4/)
- Метод: `DELETE`
- Пример URL: `http://127.0.0.1:8000/api/tasks/4/`
- Ответ: `204 No Content` или `404 Not Found`, если задача не найдена. Если удаление невозможно, то `400 Bad Request`

![image](https://github.com/user-attachments/assets/812748e9-dcbb-4cee-a24d-f7ba215f9beb)

### **Фильтрация**
- URL: [http://127.0.0.1:8000/api/tasks/?status={status_choice}](http://127.0.0.1:8000/api/tasks/?status=completed)
- Поле Фильтрации `status`
- Метод `Get`
- Пример запроса для фильтрации(выдать ответ, где статус = completed) `http://127.0.0.1:8000/api/tasks/?status=completed`
- Ответ

![image](https://github.com/user-attachments/assets/fa662d60-a23d-4d3a-a135-1cf48505d40f)

### Сортировка
- URL: [http://127.0.0.1:8000/api/tasks/?ordering={ordering_field}](http://127.0.0.1:8000/api/tasks/?ordering=title)
- Поля сортировки `title` `status`
- Метод `Get`
- Пример запроса для сортировки(выдать отсортированные по статусу задачи) `http://127.0.0.1:8000/api/tasks/?ordering=status`
- Ответ

![image](https://github.com/user-attachments/assets/831b7ab2-6a74-44e1-8983-b5e17e203895)


## Особенности
### Обработка возможных ошибок
Если задача имеет статус "completed", ее нельзя удалить, и при попытке удаления возвращается ошибка с кодом `400 Bad Request`

![image](https://github.com/user-attachments/assets/5ea36441-6b0f-4b50-9dbc-96992f5cf803)

Если задача имеет статус, отличный от "in_process", "completed", "canceled", то при попытке записать таск возвращается ошибка с кодом `400 Bad Request`

![image](https://github.com/user-attachments/assets/24824d75-0adf-44a9-b0f6-32205b263b55)

### Serializers
Для валидации статуса был использовал сериализатор, который находится на пути: `todo_progect/tasks/serializers.py`

```python
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def validate_status(self, value):
        if value not in ["in_process", "completed", "cancelled"]:
            raise serializers.ValidationError("status not found")
        return value
```
### Обработка api
Для создания api были использованы `rest_framework` и входящий в него `viewsets`, который предоставляет стандартные CRUD операции (создание, чтение, обновление, удаление). 
### Стиль кода
Для правильной оптимизации кода, а также его читаемости были соблюдены принципы ООП, а также произведено оформление кода при помощи библиотеки `Black`

## Структура проекта
```bash
todoapi/                 # Общая github папка
todo_project/            # Главная директория проекта
├── tasks/               # Приложение Django для работы с задачами
│   ├── migrations/      
│   ├── __init__.py      
│   ├── admin.py         # Регистрация моделей в админ-панели
│   ├── apps.py          
│   ├── models.py        # Определение модели Task
│   ├── serializers.py   # Сериализаторы для преобразования данных в API и валидация статуса
│   ├── urls.py          # Маршруты  для API приложения
│   ├── views.py         # Логика обработки запросов API
├── todo_project/        # Главная конфигурация проекта
│   ├── __init__.py      
│   ├── asgi.py          
│   ├── settings.py      # Из нестандартного привязали rest_framework и приложение tasks
│   ├── urls.py          # Основные маршруты проекта
│   ├── wsgi.py          
├── manage.py            # Основной файл для управления проектом
├── db.sqlite3           # Файл базы данных
├── Dockerfile           # Docker-инструкция для создания образа приложения
├── docker-compose.yml   # Конфигурация Docker Compose для контейнеризации проекта
├── requirements.txt     # Список зависимостей Python (библиотеки, которые необходимо установить)
README.md                # Файл документации проекта
```
