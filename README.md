# CloudyContacts Web Application

![page](/img_src/index.jpg)

## About
CloudyContacts is a web application built with the Django framework that provides users with tools to manage contacts and notes, upload files to cloud storage, and receive news summaries. The application includes authentication mechanisms to ensure the privacy and security of user data.

## Requirements
...

## Run Locally
```bash
  git clone https://github.com/CodeCraftSerg/CC_V2
```
Install dependencies
```bash
  poetry install
```
Now open the .env.example file and fill in the fields for the variables you need:
* SECRET_KEY=your-django-secret-key
* API_WEATHER_KEY=your-weather-key
* ABSTRACT_API_KEY=your-abstract-key
* CLOUDINARY_NAME=your-cloudinary-name
* CLOUDINARY_API_KEY=your-cloudinary-api-key
* CLOUDINARY_API_SECRET=your-cloudinary-api-secret
* DB_ENGINE=django.db.backends.postgresql_psycopg2
* DB_USER=your-username
* DB_PASSWORD=your-password
* DB_NAME=your-postgresql-name
* DB_HOST=your-local-host
* DB_PORT=your-port

Also use your personal data for email box (it's for recovering password):
* EMAIL_HOST=smtp.mail.net
* EMAIL_PORT=000
* EMAIL_HOST_USER=test@mail.net
* EMAIL_HOST_PASSWORD=password
* DEFAULT_FROM_EMAIL=test@mail.net

After that, save the file as .env

Open the settings.py file and leave the PostgreSQL Database connection uncommented.
Other connections should be commented out.
You can also use the database connection that is more convenient for you.
If you use a cloud database connection, you do not need to run Docker Compose file.

Run Docker Compose file
```bash
  docker compose up
```
Make migrations for your database
```bash 
  python manage.py makemigrations
```
Migrate your database
```bash 
  python manage.py migrate
```
Start the server
```bash
  python manage.py runserver
```
By default, application will run on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)