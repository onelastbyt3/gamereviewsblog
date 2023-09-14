# GameReviewsBlog




## Overview
This is a Django web app where users can write a video game review and be able to discuss them with others via comments. Users can also submit requests for other reviewers to write a review, and can view every post associated with a specific reviewer. It uses simple HTML templates to render the frontend, with Django on the backend. 

## Screenshots

<img src="https://github.com/onelastbyt3/gamereviewsblog/blob/main/blog/static/screenshots/01.png" width="700" height="450">

<img src="https://github.com/onelastbyt3/gamereviewsblog/blob/main/blog/static/screenshots/02.png" height="450">


## Installation

1. Clone this repository to your local machine using the command:
```
https://github.com/onelastbyt3/gamereviewsblog.git
```

2. Ensure you have Python installed (ver.3.9.9) and Django

3. Install the required dependencies using the command: 
```
pip install -r requirements.txt
```

4. Configure your secret key and database in the source code on the settings.py file located inside the gamereviewsblog folder:
```
SECRET_KEY = config('DJANGO_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

5. Migrate the database
```
py manage.py makemigrations
py manage.py migrate
```

6. Run the application from the main.py file located on the root folder which will generate a local URI link where the app will run.
```
py manage.py runserver
```
## Development Notes



## Contributions
Contributions to this project are welcome, as this was a simple project with many features/design elements still lacking mainly in CSS styling and overall page aesthetic. Any frontend developers looking to contribute are welcome to submit a pull request for review! 
