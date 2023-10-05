# Environment Setup
## Python version in .tool-versions

## Using poetry
    - `poetry install`
    - `poetry env use 3.10.5`
    - `poetry shell`
## Not using poetry
    - pip install -r requirements.txt
        - if you're using makefile, `make pip-install`

# Database setup
## Create database with name as you desired
    - copy `.env.example` to `.env`
    - change `DB_NAME` to your just created database name
    - change `DB_USER` to your database username
    - change `DB_PASSWORD` to your database password
    - change `DB_HOST` to your database host
    - change `DB_PORT` to your database port
## Migrate database
    - `alembic upgrade head`

## Seed database
    - `python tools.py seed users`
    - `python tools.py seed tables`

# Run the application
    - `uvicorn main:app --reload`
        - if you'r using Makefile, `make run`
    