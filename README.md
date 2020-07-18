# Shore2RL
A Self-Hostable URL shortener

**To Run:**

 - Clone repository
 - Run `pipenv install`
 - Setup PSQL database
 - Create config.json with database credentials
 - Run `pipenv run python manage.py makemigrations`
 - Run `pipenv run python manage.py migrate`
 - Run `pipenv run python manage.py runserver`
