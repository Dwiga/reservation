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

# Application docs
## Buy a ticket
    - I assume that every table has 2 seats.
    - Once customer buy a ticket, they will have random seat (using numpy library to make this happen)
    - I assume customer only eat 1 our, so when another customer buy a ticket in different hour, the previous customer's seat will be available
    - I assume they come in a fix hour, (1-24)
    - I assume, the price of the ticket is only 50% (cheaper) than 1 table
    - I assume there'are 3 types of user, 0. admin, 1. waiter, 3. customer
    - this functionality belongs to type: 0, whic is `buy ticket`

## Book a table
    - I assume that every table has 2 seats.
    - Customer freely choose an empty table (showing available table should be in different task, for now customer only input selected table)
    - I assume admin approval also should be in different task, as you mention i only create 2 API buy and booking table
    - I assume they come in a fix hour, (1-24)
    - I assume there'are 3 types of user, 0. admin, 1. waiter, 3. customer
    - this functionality belongs to type: 1, whic is `book table`

## Bad connection problem
    - I assume that the internet problem only happens to restaurant's intenet cable
    - if that happens, I suggest to use 3rd parti API (i.e Telegram API)
    - this Telegram API also supported python library, so we can put the hook inside this app
    - using this approach, we can use mobile connection to access or send data with minimum ammount of data (only text data, no UI needed)
    - `python bot.py` to run the bot
    