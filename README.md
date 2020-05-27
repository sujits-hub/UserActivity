# UserActivity

## Table of Contents

* [About the Project](#about-the-project)
* [Deploy](#Deploy)
* [Getting Started](#instructions-to-run)
* [Api](#Api-end-points)
* [Populate](#Populate)
* [Author](#author)

## About the Project 

A Basic Django application to track User Activities with User and ActivityPeriod models.


## Deploy

The project has been deployed. [Click](https://user-activity-periods.herokuapp.com/) here to check.


## Getting Started

Setup project environment with virtualenv and pip.


```sh
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```


Instructions to run.


```sh
cd UserActivity
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Api end points

1. / - api for documentation page for the project
2. /activity/get-all-details/ - api to serve data in the required [format](https://drive.google.com/open?id=1xZa3UoXZ3uj2j0Q7653iBp1NrT0gKj0Y).
3. /activity/user_list/ - api to see the user list
4. /activity/user_list/<user_id>/ - api to see the details of particular user


## Populate

Custom Management command to populate the database with dummy data has been implemented. Run the following command to populate the database.


```sh
python manage.py commands
```
