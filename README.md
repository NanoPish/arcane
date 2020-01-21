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

* Containerization through [Docker](https://www.docker.com/) to achieve scalability, standardization, consistency, flexibility, and possibility to update this project to setup an orchestrator to achieve self-healing and auto-scaling architecture

* Two environments, easily reproducible, local and prod
    - A local environment to run the service in a local container, for example a local [mysql](https://www.mysql.com/) database
    - A production environment to run the service in a remote container on an [EC2](https://aws.amazon.com/fr/ec2/) instance, with a [RDC](https://aws.amazon.com/fr/rds/) instance as a database

* TO EDIT: a production API is running on my own AWS, accessible at TO EDIT

* An abstracted and declarative infrastructure as code ([IaC](https://en.wikipedia.org/wiki/Infrastructure_as_code)) production infrastructure leveraging terraform to spin up an EC2 and a RDS, in order to achieve speed, simplicity, consistency of the configuration, risk lessening, easier scaling management

## Microservice dependencies

* [Python3](https://www.python.org/) / [Flask](http://flask.palletsprojects.com/en/1.1.x/)

* [SQLAlchemy ORM](https://www.sqlalchemy.org/) to interact with SQL databases, achieving modularity and reusability of the code, and facilitating the plugging of the service to different database providers

* [pytest](https://docs.pytest.org/en/latest/), for testing

* [Marshmallow](https://marshmallow.readthedocs.io/en/stable/) for data serialization/deserialization and input validation

* [Flask-RESTplus](https://flask-restplus.readthedocs.io/en/stable/) for Swagger documentation

* [flask_accepts](https://github.com/apryor6/flask_accepts), a that marries Marshmallow with Flask-RESTplus, giving you the control of marshmallow with the awesome Swagger documentation from flask-RESTplus

## Microservice design pattern

As it is my first time using Flask and after reading flask frameworks documentations and design patterns from various authors I decided to follow Aj Pryor [Flask best practices](http://alanpryorjr.com/2019-05-20-flask-api-example/)'s patterns for building "testable, scalable, and maintainable APIs".

It is very well explained, and "has been battle-tested (double emphasis on the word “test”!) and works well for a big project with a large team and can easily scale to a project of any size".

## Running the project as a developer

### Running the microservice locally

* To run the microservice locally, with a sqlite DB and with flask development server, which includes code autoreload:
        
        cd app/arcane_real_estate
        pip install -r requirements.txt    
        FLASK_APP=app/__init__.py:create_app FLASK_ENV=development flask run
        
* Access the server on localhost:5000