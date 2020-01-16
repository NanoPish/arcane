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

## Technologies choices

* Python3 / Flask microservice for CRUD real estate management and authentication

* Server: Maximizing Flask performance leveraging Meinheld serving through Gunicorn, to have multiple worker forks and threads serving, also making the app more resistant (no service loss if a worker crashes)

* Containerization through Docker to achieve scalability, standardization, consistency, flexibility, and possibility to update this project to setup an orchestrator to achieve self-healing and auto-scaling architecture

* Two environments, easily reproducible, local and prod
    - A local environment to run the service in a local container, with a local mysql database
    - A production environment to run the service in a remote container on an EC2 instance, with a RDC instance as a database

* An abstracted and declarative infrastructure as code (IaC) production infrastructure leveraging terraform to spin up an EC2 and a RDS, in order to achieve speed, simplicity, consistency of the configuration, less risk, easier scaling management

* Use of SQLAlchemy toolkit and ORM to interact with SQL databases, achieving modularity and reusability of the code, and facilitating the plugging of the service to different database providers
