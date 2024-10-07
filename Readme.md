# SwiftBuy - Django Project

This project uses `pipenv` for dependency management, Docker for containerization, and Celery for task processing. Below are the essential commands you will need to run the project.

---

## Setting Up the Project

### 1. Install Dependencies
To install the project dependencies defined in the `Pipfile`, run the following command:
```bash
pipenv install
```

##### Activate the Virtual Environment
To activate the virtual environment for the project, use the following command:

``` bash
pipenv shell
```
##### Sync Dependencies with Pipfile.lock
To ensure that the installed dependencies exactly match those defined in the Pipfile.lock, run:
``` bash
pipenv sync
```

##### Run the migrations to connect the DB
``` bash
python manage.py migrate
```
##### Run the Server
``` bash
python manage.py runserver
```
##### Config the redis
``` bash 
docker run -p localPort:workingPort redis
```
##### Running a Celery Worker Using Docke

``` bash
docker -A storefront worker
```
##### Run Automation Tests
``` bash
pytest
```
##### Run the Performance Testing
``` bash 
locust -f locustfiles/browse_products.py
```

##### Task Queue Monitoring
``` bash 
celery -A your_project_name flower
```
##### Running the Application with Gunicorn
``` bash
gunicorn storefront.wsgi
```
