
# Discount microservice

Billogram technical Interview task.

## Setup
1. Run MySQL Server.
3. Create Database using **schema.sql** in the repository.
4. Update `DATABASE_URL` environment variable in **config.json**


## Getting started



Intall required dependencies and run the app:

```shell
pip install -r requirements.txt
python app.py
```

Visit [http://localhost:8080](http://localhost:8080)

## Tests

Standalone unit tests run with:

```shell
pip install pytest pytest-cov pytest-flask
pytest --cov=web/ --ignore=tests/integration tests
```
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`

