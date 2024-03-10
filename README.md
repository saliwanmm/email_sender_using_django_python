# Email Sender 

## Description

**This project allows automatic sending of messages to site subscribers**

## Technologies used in the project
- Python
- Django
- MySQL
- Docker
- Docker-compose
- Git

## Local setup

**Create python environment**

```
$ python3 -m venv venv
```

**Activate python environment**

```
$ source venv/bin/activate
```

**Install dependencies**

```
$ pip install -r requirements.txt
```

**Create .env file and insert there all code from .envexample file**

```
$ touch .env
```

**Open .env file and insert your data to EMAIL SETTINGS:**

```
$ .env / EMAIL_HOST_USER='' and .env / EMAIL_HOST_PASSWORD=''
```

**Build web and database containers**

```
$ sudo docker-compose build
```

**Run web and database containers**

```
$ sudo docker-compose up
```

**Superuser: username - admin, password - admin.**
**You must be logged in as an administrator to send automatic newsletters** 