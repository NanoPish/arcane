# arcane
### An exercise for Arcane internship interview
Dans le cadre d'un projet de création d'une application web de gestion immobilière, on nous demande de créer un ensemble de microservices. Ces microservices doivent permettre à un utilisateur de renseigner un bien immobilier avec les caractéristiques suivantes : nom, description, type de bien, ville, pièces, caractéristiques des pièces, propriétaire) et de consulter les autres biens disponibles sur la plateforme. 

Nous souhaitons proposer aux utilisateurs les fonctionnalités suivantes :
    Un utilisateur peut modifier les caractéristiques d'un bien (changer le nom, ajouter une pièce, etc… )
    Les utilisateurs peuvent renseigner/ modifier leurs informations personnelles sur la plateforme (nom, prénom, date de naissance)
    Les utilisateurs peuvent consulter uniquement les biens d'une ville particulière
    Fonctionnalité bonus : Un propriétaire ne peut modifier que les caractéristiques de son bien sans avoir accès à l'édition des autres biens.

Objectif : 

Créer un microservice avec une API REST qui permet aux utilisateurs de réaliser toutes les fonctionnalités citées ci-dessus. Il n'est pas demandé de développer l’interface.

Choix technologiques :

    Langage : Python

    Framework : Flask

    Base de données : Choix libre

    Pas de Front

Livrable: Transmettre le code sous la forme d’un repository git (sur github par exemple), le Readme contiendra toutes les instructions pour pouvoir le faire tourner en local.

Critères d’évaluation:
- Méthodologie de gestion de projet, cela devra être reflété dans l'historique Git
- Modèle de données utilisé
- Structuration/ Architecture du code python

## Environment and infrastructure

* Server: Maximizing Flask performance leveraging [Meinheld](https://meinheld.org/) serving through [Gunicorn](https://gunicorn.org/), to have multiple worker forks and threads serving, also making the app more resistant (no service loss if a worker crashes) following tiangolo's [meinheld-gunicorn-docker](https://github.com/tiangolo/meinheld-gunicorn-docker)

* Containerization through [Docker](https://www.docker.com/)

* Two environments, easily reproducible, local and prod
    - A local environment to run the service in a local container, for example with the bundled sqlite database
    - A production environment to run the service in a remote container on an [EC2](https://aws.amazon.com/fr/ec2/) instance, with a [RDC](https://aws.amazon.com/fr/rds/) instance as a database

* TO DO: deploy on aws

* An abstracted and declarative infrastructure as code ([IaC](https://en.wikipedia.org/wiki/Infrastructure_as_code)) production infrastructure leveraging terraform to spin up an EC2 and a RDS, in order to achieve speed, simplicity, consistency of the configuration, risk lessening, easier scaling management

## Microservice dependencies

* [Python3](https://www.python.org/) / [Flask](http://flask.palletsprojects.com/en/1.1.x/)

* [SQLAlchemy ORM](https://www.sqlalchemy.org/) to interact with SQL databases, achieving modularity and reusability of the code, and facilitating the plugging of the service to different database providers

* [pytest](https://docs.pytest.org/en/latest/), for testing

* [Marshmallow](https://marshmallow.readthedocs.io/en/stable/) for data serialization/deserialization and input validation

* [Flask-RESTplus](https://flask-restplus.readthedocs.io/en/stable/) for Swagger documentation

* [flask_accepts](https://github.com/apryor6/flask_accepts), a that marries Marshmallow with Flask-RESTplus, giving you the control of marshmallow with the awesome Swagger documentation from flask-RESTplus

## Microservice design pattern

As it is my first time using Flask and after reading flask frameworks documentations and design patterns from various authors I decided to follow Aj Pryor's [Flask best practices](http://alanpryorjr.com/2019-05-20-flask-api-example/) patterns for building "testable, scalable, and maintainable APIs".

"In a nutshell, Flask requests are routed using RESTplus Resources, input data is validated with a Marshmallow schema, some data processing occurs via a service interacting with a model, and then the output is serialized back to JSON on the way out, again using Marshmallow. All of this is documented via interactive Swagger docs, and flask_accepts serves as glue that under-the-hood maps each Marshmallow schema into an equivalent Flask-RESTplus API model so that these two amazing-but-somewhat-incompatible technologies can happily be used together."

## The Arcanific project overview

* 4 functional sectors / entities that can be CRUD managed in a RESTful way
    - Property: a real estate commodity possed by a user
    - User: a real estate owner
    - Type: types of property (e.g. house, flat...)
    - Rooms: property can have rooms attached to them

* Each entity is composed of a folder containing:

    - Model: Python representation of entities
    - Interface: Defines types that make an entity
    - Controller: Orchestrates routes, services, schemas for entities
    - Schema: Serialization/deserialization of entities
    - Service: Performs CRUD and manipulation of entities
    
* And the corresponding .test files

### Running the microservice locally

* Install python 3.7+ and docker

* To run the microservice locally, with a sqlite DB and with flask development server, which includes code autoreload:
        
        cd app/arcane_real_estate
        python3.7 -m pip install -r requirements.txt    
        FLASK_APP=app/__init__.py:create_app FLASK_ENV=development flask run
        
* Access the swagger / server on localhost:5000

### Run the tests

        cd app/arcane_real_estate
        pytest
        
### Authentication

* Authorization: Bearer ... model, using [flask-jwt-extended](https://flask-jwt-extended.readthedocs.io/en/stable/)

* Hashing using [passlib](https://passlib.readthedocs.io/en/stable/)

* Authentication and authorization using @jwt_required decorators and verifying user identity when required

### How to use

* Navigate the microservice using swagger at localhost:5000
* First create an user, by posting to /users, then auth at /user/auth
* Then create properties and rooms
* Users can only delete, modify, add rooms, remove rooms, update rooms for properties that belong to them

### Cool features

* Wire any SQL database local or remote by modiying config.py thanks to SQLAlchemy agnosticism
* Seed the DB using python manage.py seed.db
* Swagger doc. semi automated using flask-restplus
* Swagger doc. configured to let user enter it's auth token to test more easily
* Different configs to compartment test, dev, prod DBs
* Tests
* Modularity / reusable code thanks to design pattern and encapsulated app / components

### Unfinished things
* I did not add the location header to the api responses because of a problem I did not manage to fix with flask_accepts
* I did not finish the testing as it is very long to do
* Lot of tests failing as I did not rewrite them all after refactoring
        
 ### run in docker on localhost:5222
* build and run


    docker build .
    docker run -p 5222:80 -e APP_MODULE=arcane_real_estate.wsgi:app -it test
