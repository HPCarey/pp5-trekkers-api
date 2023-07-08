# Trekkers API
#
This is the backend api for the trekkers Frontemd React app. It contains the models and logic to allow the frontend application to perform CRUD operations.

#
* [Deployed Back-End page](https://pp5-trekkers-api.herokuapp.com/)
* [Deployed Front-End page](https://trekkers.herokuapp.com/)
* [Frontend repository](https://github.com/HPCarey/trekkers)
#
### Agile Planning
#### **GitHub Project Board**

* This project was made using agile methodologies. Epics, user stories, bugs and issues are recorded on the [Project Board](https://github.com/users/HPCarey/projects/5/views/1)

![Screenshot of project board](/readme/kanban-board.png)

#### **Github Issues**
Here is a [link](https://github.com/HPCarey/trekkers/issues)  to the project issues and labels. 
* A list of Frontend Bugs can be viewed via the Frontend Bug label. 
* A list of backend bugs can be viewed via the Backend bug label.
* A list of all bugs can be viewed via the bugs label.


#### **ERD Plan for backend models**
 * The plan for this project is based on the Code Institute Moments walkthrough project. 
 * Most of the models are the same except for the post model which has been customised to better suit the needs of the site owner and users.
 * Initial plans were to include an event model, but that has been assigned as a future feature to help focus on the minimal viable product of  the site. 

![Database](/readme/trekkers_erd.jpeg)

## Technologies
### **Libraries and packages**
The following libraries and packages were installed using the pip3 install command:
```
'django<4'
dj3-cloudinary-storage
Pillow
djangorestframework
django-filter
dj-rest-auth
'dj-rest-auth[with_social]'
djangorestframework-simplejwt
dj_database_url psycopg2
gunicorn
django-cors-headers
```
## Deployment
### Steps to set up and deploy the project:
#### **Gitpod**
This project was created using the Code Institute
1. Create a repository in github using the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template). 
2. Click Use this Template and add a repository name.
3. Click Create Repository from template
4. Install Django and the rest of the libraries listed in the libraries section. 
5. Freeze requirements using: pip3 freeze --local > requirements.txt
6. TO create the project:(django-admin startproject trekkers .  )
    - Note the '.' at the end to ensure we don't need to cd into the app every time.
7. To create  app: (python3 manage.py startapp posts)
8. Add apps to INSALLED_APPS.
9. Migrate changes and run server locally to check it's working.

[Back to top](#contents)
#
#### **ElephantSQL**
Before deploying to heroku, an external database was created to host the app data.
1. Create an [ElephantSQL](https://www.elephantsql.com/) account. Code Institute provides the steps to do that [here](https://code-institute-students.github.io/deployment-docs/02-elephantsql/elephantsql-01-sign-up).
2. Click the green "Create New Instance" button.
3. Set your plan to Tiny Turtle (Free) and give it a name.
4. Select a data centre near you and click review.
5. Check the details are correct and click create instance.
6. Return to the ElephantSQL dashboard and select the newly created database instance.
7. Copy the database URL using the copy icon. 
8. Add this database url to your env file.
9. Later you will also add this url to your Heroku Config Vars.

[Back to top](#contents)
#

#### **Environemental variables and settings.py**
1. Create the env.py file in the top level directory.
2. Import os library and set the variables accordingly: 
    - The database is your ElephantSQL URL
    - The secret key you can make up or use a [generator](https://djecrety.ir/)
    - I am using cloudinary for image storage so the cloudinary url is my API Environmental variable for my cloudinary account. 
    
env.py for this project: 

```
import os

os.environ['CLOUDINARY_URL'] = 'cloudinary://thisisasecret'
os.environ['DEV'] = '1'
os.environ['SECRET_KEY'] = 'thisisasecret'
os.environ['DATABASE_URL'] = 'postgres://thisisasecret'
```
3. In settings.py, make sure to import dj-database, regular expression and os modules and  use an if statement to get the env.py file.

```
    import dj_database_url
    import re
    import os
    if os.path.exists('env.py')
        import env
```

4. Remove the automtic django secret key and get it from the env.py.
```
SECRET_KEY = os.environ.get('SECRET_KEY')
```
5. Comment out the old DataBase section and replace it with the one below.
```
    if 'DEV' in os.environ:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    else:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }
```
7. Set up Cloudinary to store the static and media files.
9. Add 'cloudinary_storage', to INSTALLED_APPS, in settings.py, above 'django.contrib.staticfiles',.
10. Then add'cloudinary', underneath  'django.contrib.staticfiles',.
     - NB. The order is important:
     ```
        'cloudinary_storage',
        'django.contrib.staticfiles',
        'cloudinary',
     ```
11. In settings.py, add the code to tell Django to use cloudinary to store media and static files. 
    ```
        CLOUDINARY_STORAGE = {
        'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
        }
        MEDIA_URL = '/media/'
        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

    ```

- Below INSTALLED_APPS, set site ID:
```
SITE_ID = 1
```
12. Below BASE_DIR, create the REST_FRAMEWORK, and include page pagination to improve app loading times, pagination count, and date/time format:
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}
```
13. Set the default renderer to JSON:
```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```
14. Beneath that, added the following:
```
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'
```
15. Then added:
```
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'project_name.serializers.CurrentUserSerializer'
}
```
16. Updated DEBUG variable to:
```
DEBUG = 'DEV' in os.environ
```
17. Updated the DATABASES variable to a conditional to either use SQLITE database for developmentand or the ElephantSQL database url from the env file otherwise:
```
if 'DEV' in os.environ:
    DATABASES = {
        'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
         }
     }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
```
18. Get the heroku url from the ALLOWED_HOSTS variable in env file and allow localhost for development:
    - NB: localhost is not working for me so I am using the actual gitpod url.
```

ALLOWED_HOSTS = [
   os.environ.get('ALLOWED_HOST'),
   'localhost',
]
```
19. Add the CORS_ALLOWED variable so that we can connect out frontend app using the CLIENT_ORIGIN and CLIENT_ORIGIN_DEV keys in heroku:
```
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
```
20. Also added to the top of MIDDLEWARE:
```
'corsheaders.middleware.CorsMiddleware',
```


16. Create a Procfile and add web:
```
    release: python manage.py makemigrations && python manage.py migrate
web: gunicorn trekkers.wsgi
```
17. Make sure to freeze all requirements: 
```
pip3 freeze --local > requirements.txt
```
18. Check all migrations have been made:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
19. Git add, commit and push.
20. App is ready for deployment to heroku. 

[Back to top](#contents) 
#

#### **Heroku**
Initial deployment to heroku was done early with the intention of making the final deployment process more smooth.
1. Log in to [Heroku](https://www.heroku.com/).
2. From the dashboard, click the button labelled New in the top right corner and from the drop-down menu select Create New App.
3. Enter a name for the app and select your region.
4. Click Create App.                  
5. Find the Settings Tab and scroll down to Config Vars.
6. Click Reveal Config Vars.
7. Enter the following key-value pairs:
 - Key: SECRET_KEY | Value: YourSecreteKeyValue
 - Key: CLOUDINARY_URL | Value: cloudinary://yourCloudinaryAPIenv
  - Key: DATABASE_URL | Value: postgres://yourElephantSQLDatabasUrl
 - Key: DISABLE_COLLECTSTATIC | Value: 1
 - Key: ALLOWED_HOST | Value: pp5-trekkers-api.herokuapp.com
8. Navigate to the Deployment tab and choose Github as the deployment method.
9. Search for the repo name and connect to the correct repository.
10. Scroll down and deploy branch.
11. Finally click the open app button once the build is finished.

[Back to top](#contents)

###Connet to a Frontend App

#
## **Credits**
### Code Institute

This project is a variation and laregely based on the [Code Institute Moments](https://github.com/Code-Institute-Solutions/drf-api/tree/ed54af9450e64d71bc4ecf16af0c35d00829a106) walkthrough project.
It contains models and logic from that project which have bee modified for the prupose of this one.

### Resources for creating the rating field in post model:
1.	Geeksforgeeks: [Posititive Integer field](https://www.geeksforgeeks.org/positiveintegerfield-django-models/)
2.	Stack overflow: [Set a default min/max value for inetger field](https://stackoverflow.com/questions/42425933/how-do-i-set-a-default-max-and-min-value-for-an-integerfield-django)

### Bug fixes sources:
1.	Application labels aren’t unique error when deploying backend api : [Stack Overflow](https://stackoverflow.com/questions/24319558/how-to-resolve-django-core-exceptions-improperlyconfigured-application-labels)
2. Other bug fix sources are credited in the Project Board under Issues labelled "Backend bug"
