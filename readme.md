git clone https://github.com/shariqsajad88/crud_drf
cd user_crud
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver