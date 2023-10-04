install:
	@poetry self update
	@poetry install

start:
	@. $(shell poetry env info --path)/bin/activate && uvicorn main:app --reload

gunicorn:
	@. $(shell poetry env info --path)/bin/activate && gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

pip-freeze:
	@pip list --format=freeze > requirements.txt

pip-install:
	@pip install -r requirements.txt

poetry-export:
	@poetry export --without-hashes --format=requirements.txt > requirements.txt
