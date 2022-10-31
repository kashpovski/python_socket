# Homework_25

# Домашнее задание
***
### Echo сервер 
***
### Цели занятия:
Попрактиковаться с использованием модуля socket и сетевым взаимодействием по протоколу HTTP
***
Описание/Пошаговая инструкция выполнения домашнего задания:

В этом задании реализуем собственный echo-сервер с использованием библиотеки socket.
Для выполнения задания использовать только модули стандартной библиотеки.
Ваш сервер должен принимать запрос от клиента и отправлять ему: 
1. заголовки, которые получил в запросе
2. метод, которым был сделан запрос
3. выставлять статус, который передал клиент в GET параметре status (т.е. если передали /?status=404 то ответ будет со статусом 404) если параметр не передан или не валидный то отдавать 200, если значение
4. (опционально) сервер не должен прекращать работу после ответа клиенту, а продолжать ожидать следующего соединения

Заголовки должны отображаться на странице в виде строк текста:
- Request Method: GET
- Request Source: ('127.0.0.1', 47296)
- Response Status: 200 OK
- header-name: header-value
- header-name: header-value
- ...

Для того чтобы правильно выставить значение статуса нужно отправить числовое значение и фразу например 200 OK, 404 Not Found и т.д. самый оптимальный способ для поиска нужной фразы статуса это воспользоваться модулем http из стандартной библиотеки python https://docs.python.org/3/library/http.html

Критерии:
1. Задание сдано в формате pull-request
2. В репозитории отсутствуют лишние файлы
3. Сервер возвращает все заголовки присланные ему клиентом в виде валидного HTTP ответа
4. Сервер обрабатывает параметр status корректно и не падает при невалидных значениях
5. (Опционально) сервер не отключается после обработки соединения