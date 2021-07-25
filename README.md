# Asset Management Project

## Prerequisites

**Python 3.0+**

======================================

To run the project, do the following

**1. Install all requirements**
```sh
pip install -r requirements.txt
```
**2. Run migrate file**
```sh
python manage.py migrate
```

**3. Create Superuser/ Admin user**
```sh
python manage.py createsuperuser --username Admin --email admin@exmaple.com
```

**4. Run project**
```sh
python manage.py runserver
```

**5. Login into admin panel to create user with URL 127.0.0.1:8000/admin**

**6. Visit authenticated API endpoints as mentioned below.**
```sh
GET 127.0.0.1:8000/fixed_deposit/
POST 127.0.0.1:8000/fixed_deposit/
PUT 127.0.0.1:8000/fixed_deposit/{id}
DELETE 127.0.0.1:8000/fixed_deposit/{id}

GET 127.0.0.1:8000/bullion/
POST 127.0.0.1:8000/bullion/
PUT 127.0.0.1:8000/bullion/{id}
DELETE 127.0.0.1:8000/bullion/{id}

GET 127.0.0.1:8000/current_eval
```

***Please remember, for bullion, current rate of Gold and Silver is hardcoded as Rs.4925/- and Rs.67/- respectively.***

