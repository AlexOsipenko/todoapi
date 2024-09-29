# API для управления списком задач
Учебный проект - создание приложения на Django

## Установка приложения

## Админ панель
![image](https://github.com/user-attachments/assets/b729887f-654f-462f-af56-c0d1e203da2f)

### Адрес
`http://127.0.0.1:8000/admin/`
### Креды суперпользователя
user: `admin`
password: `admin`
### Возможные операции в админке
**Список тасков**
- Выберите "Tasks" На главной странице админ-панели/
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
**Создание задачи**
- URL: [/api/tasks/http://127.0.0.1:8000/api/tasks/](/api/tasks/http://127.0.0.1:8000/api/tasks/)
- Метод: POST
- Пример body:

![image](https://github.com/user-attachments/assets/2a477af0-2df8-4429-a5fa-96fdffc28717)
- Ответ: `201 Created`
![image](https://github.com/user-attachments/assets/fb94e478-45f6-4b67-aa58-ba2a9d434166)

2. Получение всех задач
URL: /api/tasks/
Метод: GET
Ответ:
json
Копировать код
[
  {
    "id": 1,
    "title": "Новая задача",
    "description": "Описание задачи",
    "status": "in_progress"
  },
  {
    "id": 2,
    "title": "Вторая задача",
    "description": "Описание второй задачи",
    "status": "completed"
  }
]
3. Получение задачи по ID
URL: /api/tasks/{id}/
Метод: GET
Ответ:
json
Копировать код
{
  "id": 1,
  "title": "Новая задача",
  "description": "Описание задачи",
  "status": "in_progress"
}
4. Обновление задачи по ID
URL: /api/tasks/{id}/
Метод: PATCH
Тело запроса:
json
Копировать код
{
  "title": "Обновлённая задача",
  "status": "completed"
}
Ответ (200 OK):
json
Копировать код
{
  "id": 1,
  "title": "Обновлённая задача",
  "description": "Описание задачи",
  "status": "completed"
}
5. Удаление задачи по ID
URL: /api/tasks/{id}/
Метод: DELETE
Ответ (204 No Content) при успешном удалении.


