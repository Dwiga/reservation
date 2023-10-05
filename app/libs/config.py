from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


def database():
    return "{}://{}:{}@{}:{}/{}".format(
        os.getenv("DB_ENGINE"),
        os.getenv("DB_USER"),
        os.getenv("DB_PASSWORD"),
        os.getenv("DB_HOST"),
        os.getenv("DB_PORT"),
        os.getenv("DB_NAME"),
    )


def telegram_token():
    return os.getenv("TELEGRAM_TOKEN")
