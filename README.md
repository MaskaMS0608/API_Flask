# API_Flask

Минимальный API сервис, созданный с помощью фреймворка Flask, предоставляющий возможность ведения микроблога.

В микроблоге используются модели:
  пользователь,
  пост.
Пользователь имеет возможность:
  создать,
  прочитать,
  изменить
  удалить пост.
_________________________________________

Для взаимодействия между клиентом и сервером используются методы:

GET — получение информации об объекте (посте).
POST — создание нового объекта (поста).
PUT — обновление, полная замена поста.
DELETE — удаление поста.

Для работы программы потребуется компьютер с операционной системой Windows. 
Программа требует наличия установленного Python 3.11 или более поздней версии.
Сервис написан в приложении PyCharm.

________Порядок запуска сервиса__________

/// Открыть проект в PyCharm

/// Выполнить в командной строке команду: python -m venv <имя виртуального окружения>.

/// Перейти в созданную директорию: cd <имя виртуального окружения>.

/// Активировать окружение: \scripts\activate.

/// Установить фреймворк Flask: pip install flask.

/// Команда для запуска сервиса: flask --app response.py run

_________________________________________

Тестирование приложения:

/// добавление нового поста
```
curl http://127.0.0.1:5000/api/v1/note/ -X POST -d "title|text"
```

### получение всего списка заметок
```
curl http://127.0.0.1:5000/twit/
```

### получение заметки по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/note/1/
```

### обновление текста заметки по идентификатору / ID == 1 /  новый текст == "new text"
```
curl http://127.0.0.1:5000/api/v1/note/1/ -X PUT -d "title|new text"
```

### удаление заметки по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/note/1/ -X DELETE
```


## пример исполнения команд с выводом

```
$ curl http://127.0.0.1:5000/api/v1/note/ -X POST -d "title|text"
new id: 1

$ curl http://127.0.0.1:5000/api/v1/note/
1|title|text

$ curl http://127.0.0.1:5000/api/v1/note/1/
1|title|text

$ curl http://127.0.0.1:5000/api/v1/note/1/ -X PUT -d "title|new text"
updated

$ curl http://127.0.0.1:5000/api/v1/note/1/
1|title|new text

$ curl http://127.0.0.1:5000/api/v1/note/1/ -X PUT -d "title|loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong text"
failed to UPDATE with: text lenght > MAX: 120

$ curl http://127.0.0.1:5000/api/v1/note/1/ -X PUT -d "loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong title|text"
failed to UPDATE with: title lenght > MAX: 60

$ curl http://127.0.0.1:5000/api/v1/note/1/ -X DELETE
deleted

$ curl http://127.0.0.1:5000/api/v1/note/
-- пусто --
```
