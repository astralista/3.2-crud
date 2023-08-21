### Порядок действий:

в терминале перейти в папку 'stocks_products'
```commandline
cd stocks_products
```
создаем docker-container
```commandline
docker build -t my-django-app .
```
запускаем
```commandline
docker run -p 8000:8000 my-django-app
```
затем можно обращаться по этому адресу:
```commandline
http://localhost:8000/api/v1/
```
