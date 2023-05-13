FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements /code/requirements/

RUN pip install -r requirements/development.txt

COPY ./ /code/

# Run Django migrations to create database tables
RUN python manage.py migrate

# Expose port 8000 to the outside world
EXPOSE 8000

# Start the application server using the Django "runserver" command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]