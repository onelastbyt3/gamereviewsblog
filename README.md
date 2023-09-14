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
As a backend dev, my primary focus was to ensure the functionality of backend views/models, and that all data was retrieved and displayed without any issues. To achieve this, I started by creating data models that accurately represented the core elements of the application, including Review, Game, Genre, Reviewer, and ReviewRequest. Using Django's Object-Relational Mapping (ORM), I established relationships between each models and set up the database schema.

For the frontend, I designed and implemented various views and templates. This involved creating both functional and class views for displaying lists of reviews, detailed review views, game details, reviewer profiles, review request forms, and so forth. To enhance user experience and aesthetics, I integrated clean and responsive HTML templates using Django's templating engine. Additionally, static files, including images and a small portion of CSS, were integrated to ensure a polished user interface.

To allow users to navigate the application smoothly, I configured URL patterns that mapped specific URLs to their corresponding views. This routing system ensured that users could access various sections of the application with ease. For data input and validation, I implemented simple forms that allowed users to create and edit reviews and submit review requests.

In terms of testing, I developed unit tests for views and models to verify their proper functionality. These tests covered a range of scenarios, including edge cases and input validation. During development, I actively used Django's built-in debugging tools and error messages to identify and address issues promptly.

Overall, this was a very fun project to tackle. I hope this app can bring you some joy in reading about what others think about a particular game, and maybe help you in your purchasing decision. As the app is designed to scale, meaning more functionality such as user private messaging, or consuming game information from another API such as HowLongToBeat's, can be implemented to further enhance the user experience some time in the future if I want to develop this further. However, as this was a passion project and a dive into Django development overall, I am content with leaving the project as is for now. 


## Contributions
Contributions to this project are welcome, as this was a simple project with many features/design elements still lacking mainly in CSS styling and overall page aesthetic. Any frontend developers looking to contribute are welcome to submit a pull request for review! 
