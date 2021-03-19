# administrators-test

-clone proyect

-cd administrators-test

-python3 -m ven .env 

-source .env/bin/activate

-pip3 install -r requisitions.text

-python3 manage.py makemigrations

-python3 manage.py migrate 

-python3 manage.py createsuperuser

*** Open Other Terminal

-cd /administrators-test/ui

-npm install

-npm run serve

*** Return previous terminal

-python3 manage.py runserver 

-with super user access to http://127.0.0.1:8000/admin/login/ and create some roles

-go to http://127.0.0.1:8000/ to show administrators CRUD

