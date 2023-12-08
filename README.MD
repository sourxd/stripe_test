### Тестовое задание для ООО Простые Решения

Задача

- Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:

- Django Модель Item с полями (name, description, price)

- API с двумя методами:

- GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item.
  При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос
  stripe.checkout.Session.create(...)и полученный session.id выдаваться в результате запроса

- GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет
  информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id},
  получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму
  stripe.redirectToCheckout(sessionId=session_id)

Бонусные задачи

	Запуск используя Docker
	Использование environment variables
	Просмотр Django Моделей в Django Admin панели
	Запуск приложения на удаленном сервере, доступном для тестирования

Запуск в Docker

	Первый запуск:
	 1. docker-compose build
	 2. python manage.py migrate
	 3. python manage.py loaddata product.json
	 4. python manage.py createsuperuser /// создайте суперпользователя
	 5. docker-compose up

	Последующие запуски:
	 1. docker-compose up

P.S. В базе 2 тестовых объекта. Обращение по /item/1 и /item/2