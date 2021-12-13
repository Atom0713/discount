
# Discount microservice

Billogram technical Interview task.

## Documentation

[Postman documentation](https://documenter.getpostman.com/view/8678327/UVR5q9DW)

## Getting started

### DB Setup
1. Create Database using **discount_billogram_DB_schema.sql** in the repository.
2. Update `DATABASE_URL` environment variable in **development_config.json**. 
```
"DATABASE_URL": "mysql+mysqlconnector://<user_name>:<password>@localhost:3306/discount_billogram"
```

### Intall required dependencies:

```shell
pip install -r requirements.txt
```

## Run The Application

### CMD
```
> set FLASK_APP=app_dev
> set FLASK_ENV=development
> flask run
```

### BASH

```
$ export FLASK_APP=app_dev.py
$ export FLASK_ENV=development
$ flask run
```

### IDE

Run
```
app_dev.py
```
Visit [http://localhost:5000](http://localhost:5000)


## Environment Variables

To run this project, you will need to add the following environment variables

`DATABASE_URL`
`SECRET_KEY`