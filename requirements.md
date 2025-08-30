# Installation Instructions

## Explanation of Versions and Choices:

**Django~=5.0.0** : Django 5.0 is the latest stable release at the time of this query and supports current Python versions. Using ~= (compatible release) ensures that pip will install versions like 5.0.1, 5.0.2, etc., but not 5.1.0, which might introduce breaking changes.

**djangorestframework~=3.15.0** : This aligns with the latest stable versions of DRF, which offer good compatibility with Django 5.0.

**drf-yasg~=1.21.0** : A recent stable version of drf-yasg for Swagger integration.

**django-cors-headers~=4.7.0** : The latest stable version for handling CORS.

**django-environ~=0.11.0** : A current stable version for managing environment variables.

**mysqlclient~=2.2.0** : This is the official and recommended MySQL adapter for Django. You need a database driver to connect Django to MySQL.

**celery~=5.3.0** : A stable version of Celery for asynchronous task queuing.

**pika~=1.3.2** : While the prompt mentions rabbitmq, rabbitmq itself is the message broker software (like a server), not a Python package. For Python to communicate with RabbitMQ, you need a client library. Pika is the official and widely recommended pure-Python client library for RabbitMQ. Celery uses a concept of "brokers," and pika (or kombu, which Pika builds upon) is used to connect to RabbitMQ as a broker.

## How to use this file:

Save the content above into a file named requirements.txt in the root of your project directory.

Before installing, it's highly recommended to create and activate a Python virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Then, install the dependencies using pip:
Bash

```bash
pip install -r requirements.txt
```