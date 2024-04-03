# Offer Me platform

Technologies: `Python 3.12 Django 5.0`
Platform used to post job offers

### Preparing project

- Copy `.env.dev` to `.env` (and change configuration if necessary)
- Execute `docker-compose build`
- Execute `docker-compose up -d`

**Webapp is available at http://localhost:8000**

#### Example data

To populate database with example data execute command
- ```docker-compose exec app ./manage.py create_example_data```

It will create offers (http://localhost:8000/offers) and users
Login at http://localhost:8000/login


Credentials:

User 1 `Username: testuser1 Password: test_password`

User 2 `Username: testuser2 Password: second_password`

### Testing

* Use `docker-compose exec app pytest` to run the tests.
