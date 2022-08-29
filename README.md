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

- `$ python manage.py db init` 
- `$ python manage.py db migrate` 
- `$ python manage.py db upgrade` 

### Endpoints

- #### User endpoints

- Create User - POST `api/v1/users`
- Login User - POST `api/v1/users/login`
- Get A User Info - GET `api/v1/users/<int:user_id>`
- Get All users - GET `api/v1/users`
- Get My Info - GET `api/v1/users/me`
- Edit My Info - PUT `api/v1/users/me`
- DELETE My Account - DELETE `api/v1/users/me`

- #### Blogposts endpoints

- Create a Blogpost - POST `api/v1/blogposts`
- Get All Blogposts - GET `api/v1/blogposts`
- Get A Blogposts - GET `api/v1/blogposts/<int:blogpost_id>`
- Update A Blogpost - PUT `api/v1/blogposts/<int:blogpost_id>`
- Delete A Blogpost - DELETE `api/v1/blogposts/<int:blogpost_id>`


