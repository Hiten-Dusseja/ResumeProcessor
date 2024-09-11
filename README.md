1. Clone or download this repo
2. Activate the Virtual Environment:
  env/bin/activate
4. Configure PostgreSQL:
   Create a PostgreSQL database and user.
    psql -U postgres
    
    CREATE DATABASE my_database;

    CREATE USER my_user WITH PASSWORD 'my_password';

    GRANT ALL PRIVILEGES ON DATABASE my_database TO my_user;

   ALTER DATABASE <db_name> OWNER TO <db_user>;

    \q

Update settings.py with your PostgreSQL database settings:
             ![image](https://github.com/user-attachments/assets/3ab7b12e-4f5c-48d8-902a-f76a1eb7b110)

6. Apply Migrations
   python manage.py makemigrations
   python manage.py migrate
7. Run the server
   python manage.py runserver 
8. Pase URL in post man and add file as value and 'file' as key
   http://localhost:8000/api/create/

