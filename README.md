# peAk-backend
peAk-backend Application

# Authors
Team Name: 1260

# Project Manager
- [Jason Burns](https://github.com/jasonb315/)

# Contributors
- [Scott Currie](https://github.com/scott-currie/)
- [Toby Huang](https://github.com/tobyatgithub)
- [Roger Huba](https://github.com/RogerHuba)

# Description
This project will provide RESTful API to serve as a backend for its associated application [peAk](https://github.com/twelve-sixty/peAk). This project and the peAk app are still in early development stages, but their respective teams are collaboating to define an MVP and model relationships between the front end and back end projects.

# Getting Started
- Clone this repo
- Create a virtual environment: `pipenv shell`
- Install dependencies: `pipenv install -r requirement.txt`
- Create a .env file (more details to come)
- Run the development server: `python3 manage.py runserver 0.0.0.0:8000`

# Architecture
-Requires Python >= 3.6, Django, PostgreSQL

# Endpoints
- `api/v1/resort/`: List resorts
- `apt/v1/resort/<id>`: Retrieve a specific resort by id
- `api/v1/user/<id>`: Retrive a specific user by id
- `api/v1/team/<id>`: Retrieve a specific team by id
- `api/v1/resort/<resort_id>/team/`: Retrieve a list of teams at resort with id
- `api/v1/team/`: Retrieve a list of teams

# Changelog

