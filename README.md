# DockerSetUp
#### Create clone:

```
https://github.com/vladislin/coi_test.git
```

#### Create at the root of the project file `.env`, example:

```
SECRET_KEY=change_me
DEBUG=True
MYSQL_DATABASE=hello_db
MYSQL_USER=hello_db
MYSQL_PASSWORD=root
MYSQL_HOST=db
MYSQL_PORT=3306
```

#### Create at the root of the project file `.env.db`, example:

```
MYSQL_DATABASE=hello_db
MYSQL_USER=hello_db
MYSQL_PASSWORD=root
MYSQL_ROOT_PASSWORD=root
```

#### Up docker-compose:

```
docker-compose up
```

#### To view endpoints go to: http://localhost:8000/api/swagger/

#### Create superuser:

```
docker-compose run web python manage.py createsuperuser
```


