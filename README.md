1. Clone or download this repo
2. Activate the Virtual Environment:
  env/bin/activate
3. Install Dependencies
    pip install django
    pip install djangorestframework
    pip install pdfplumber
    pip install python-docx
    pip install psycopg2-binary
4. Configure PostgreSQL:
   Create a PostgreSQL database and user.
Update settings.py with your PostgreSQL database settings:
     DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
5. Apply Migrations
   python manage.py makemigrations
   python manage.py migrate
6. Run the server
   python manage.py runserver 
7. Pase URL in post man and add file as value and 'file' as key
   http://localhost:8000/api/create/

