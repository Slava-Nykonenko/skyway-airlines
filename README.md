![Logo of the project](static/images/logo.png)

# SkyWay Airlines

    Effortless Airline Management, Elevated.
    Manage flights, staff, and aircraft with precision and ease

SkyWay Airlines is a Django-powered web application that helps airlines 
manage their operations—from scheduling flights to assigning crew and 
tracking aircraft maintenance. Built with Python, Django, HTML, CSS, 
and JavaScript, it offers a clean interface and robust backend logic 
to simplify complex aviation workflows

## Installing / Getting Started

Follow these steps to get your local development environment set up and running.

1.  **Clone the repository:**
    ```shell
    git clone [https://github.com/Slava-Nykonenko/skyway-airlines.git](https://github.com/Slava-Nykonenko/skyway-airlines.git)
    cd skyway-airlines/
    ```

2.  **Set up the Python virtual environment:**
    ```shell
    # Create the virtual environment
    python -m venv venv

    # Activate it
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    # venv\Scripts\activate
    ```

3.  **Install dependencies and set up the database:**
    ```shell
    # Install required packages
    pip install -r requirements.txt

    # Run database migrations
    python manage.py migrate

    # Create an admin account to log in
    python manage.py createsuperuser
    ```

4.  **Run the development server:**
    ```shell
    python manage.py runserver
    ```

Once executed, your local server will launch the SkyWay Airlines dashboard at 
http://127.0.0.1:8000/. You can log in with the superuser credentials you just 
created.

### Initial Configuration

Before running the application, you need to set up your environment variables.

1.  Create a file named `.env` in the root directory of the project. A good way 
to do this is to copy the example file:
    ```shell
    cp .env.example .env
    ```
2.  Open the `.env` file and add your configuration settings. At a minimum, 
you will need:
    ```env
    # A strong, unique secret key
    SECRET_KEY='your_secret_key_here'

    # Set to False in production
    DEBUG=True

    # Database URL (SQLite is the default)
    DATABASE_URL='sqlite:///db.sqlite3'

    # Optional: Email settings for notifications
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # EMAIL_HOST = 'smtp.example.com'
    # EMAIL_PORT = 587
    # EMAIL_USE_TLS = True
    # EMAIL_HOST_USER = 'your-email@example.com'
    # EMAIL_HOST_PASSWORD = 'your-email-password'
    ```
    
### Deploying / Publishing

This is a basic guide for deploying the application on a server using Gunicorn.

**Important**: For a production environment, ensure you set `DEBUG=False` in 
your environment variables and configure a robust web server like Nginx or 
Apache to act as a reverse proxy.

On your local machine
```shell
git push origin main
```

On the server
```shell
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn --workers 3 skyway_airlines.wsgi:application
```

## Features

- 🛫 Flight scheduling
- 👨‍✈️ Staff management with and licensing checks
- ✈️ Aircraft tracking including maintenance logs and flight hours
- 🌍 Airport database
- 🔍 Search forms for quick access to flights, staff, planes, and airports
- ✅ Form validation for flight eligibility and licensing standard

## Contributing

We welcome contributions from fellow developers and aviation enthusiasts!
If you'd like to contribute:
- Fork the repository
- Create a feature branch
- Submit a pull request

## Links

- Project homepage: https://skyway-airlines-9o8x.onrender.com/
  - To use the functionality sign in with this data:
    ```
    login: user
    password: test@123
    ```
- Repository: https://github.com/Slava-Nykonenko/skyway-airlines
- Issue tracker: https://github.com/Slava-Nykonenko/skyway-airlines/issues. 
  - In case of sensitive bugs like security vulnerabilities, please contact 
  [slava.nykon@gmail.com](mailto:slava.nykon@gmail.com) directly instead of using 
  issue tracker. We value your effort to improve the security and privacy of this 
  project!