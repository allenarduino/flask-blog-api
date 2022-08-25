##  flask-blog-api

### Installation
  - Install [Python](https://www.python.org/downloads/), [Pipenv](https://docs.pipenv.org/) and [MySQL](https://dev.mysql.com/downloads/installer/) on your machine
  - Clone the repository `$ git@github.com:allenarduino/flask-blog-api.git`
  - Change into the directory `$ cd /flask-blog-api`
  - Create the project virtual environment with `$ pipenv --three` command
  - Activate the project virtual environment with `$ pipenv shell` command
  - Install all required dependencies with `$ pipenv install`
  - You can rename and edit  your variables in your .env
      ```
      FLASK_ENV=development
      FLASK_PORT=5000
      DATABASE_URL='mysql+pymysql://username:password@localhost/flask_blog_api'
      JWT_SECRET_KEY=your_secret_key
      ```

### Migrations

- `$ python manage.py db init` command
- `$ python manage.py db migrate` command
- `$ python manage.py db upgrade` command