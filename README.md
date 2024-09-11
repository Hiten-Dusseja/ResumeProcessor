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
             ![image](https://github.com/user-attachments/assets/3ab7b12e-4f5c-48d8-902a-f76a1eb7b110)

5. Apply Migrations
   python manage.py makemigrations
   python manage.py migrate
6. Run the server
   python manage.py runserver 
7. Pase URL in post man and add file as value and 'file' as key
   http://localhost:8000/api/create/

