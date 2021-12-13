
# Discount microservice

Billogram technical Interview task.

## Getting started

### DB Setup
1. Create Database using **schema.sql** in the repository.
2. Update `DATABASE_URL` environment variable in **development_config.json**

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

## Tests

Standalone unit tests run with:

```shell
pip install pytest pytest-cov pytest-flask
pytest --cov=web/ --ignore=tests/integration tests
```
## Environment Variables

To run this project, you will need to add the following environment variables

`DATABASE_URL`


## Endpoints

```
/discount_code/merchant/create/ [GET, POST]
```
`GET` `POST`Request headers:
```
Content-Type
Authorization
```

`POST` Request body:
```
{
    "discount_code_config": {
        "discount_type_id": 1, 'type: int'
        "number_of_codes": 10 'type: int'
    }
}
```

```
/discount_code/user/<int:merchant_id>/ [GET]
```
`GET` Request headers:
```
Content-Type
Authorization
```