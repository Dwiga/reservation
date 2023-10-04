# Environment Setup
## Python version in .tool-versions

## Using poetry
    - install poetry (https://python-poetry.org/)
    - `poetry install`
    - `poetry shell`
    - `uvicorn main:app --reload`
        - if you're using makefile, `make start`
## Not using poetry
    - pip install -r requirements.txt
        - if you're using makefile, `make pip-install`
    - `uvicorn main:app --reload`
    - if you're using makefile, `make start`

# Database setup
## Create database with name as you desired
    - copy `.env.example` to `.env`
    - change `DB_NAME` to your just created database name
    - change `DB_USER` to your database username
    - change `DB_PASSWORD` to your database password
    - change `DB_HOST` to your database host
    - change `DB_PORT` to your database port
    