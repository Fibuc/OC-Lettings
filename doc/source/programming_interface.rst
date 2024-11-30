Interfaces de programmation
===========================

Les différents points d'accès
-----------------------------

L'application couvre différents points d'accès qui sont les suivants :

- ``/``: Correspond à la page principale du site.
- ``/profiles/``: Correspond à tous les profils existants qui seront affichés en format de liste.
- ``/profiles/<str:username>``: Correspond à l'affichage du profil détaillé de l'utilisateur via son ``username``.
- ``/lettings/``: Correspond à toutes les locations existantes qui seront affichées en format de liste.
- ``/lettings/<int:letting_id>``: Correspond à l'affichage de la location détaillée de l'utilisateur via son ``letting_id``.
- ``/admin/``: Correspond à l'accès à l'interface administrateur de l'application.

.. important::

   Seule la méthode ``GET`` est possible sur le site, aucune autre méthode n'est acceptée.

Les différents retours
----------------------

- Statut ``200 OK``: Requête réussie, vous accédez à la page désirée.
- Statut ``404 Not Found``: Requête échouée, la page désirée n'existe pas ou n'est pas accessible. La page d'erreur 404 s'affichera.
- Statut ``500 Internal Server Error``: Requête échouée, il y a un problème interne avec le serveur. La page d'erreur 500 s'affichera.

Les langages utilisés
---------------------

Il est impératif d'utiliser les langages de programmation spécifiés pour le bon fonctionnement de l'application.

- Python pour la gestion de l'ensemble de l'application (routes, URLs, configuration, etc...)
- HTML pour la réalisation des templates.
- CSS pour les styles utilisés dans l'affichage utilisateur.
- Markdown pour le fichier README.
- reStructuredText pour la documentation de l'application.
- YAML pour le pipeline.

Structure de l'application
--------------------------

Il est également important de maintenir la structure de l'application.

Actuellement, l'application est possède une architecture en MVT *(Models, Views, Templates)* de par l'utilisation de Django. De plus, celle-ci est
compartimentée en plusieurs applications :

- L'application ``oc-lettings-site`` : Application principale qui gère les paramètres et les routes principales de l'application.
- L'application ``profiles`` : Application qui gère tous les éléments relatifs aux profils (modèles, vues, templates, interface administrateur, etc...).
- L'application ``lettings`` : Application qui gère tous les éléments relatifs aux locations (modèles, vues, templates, interface administrateur, etc...).

Contrôles et vérification
-------------------------

Pour contrôler la syntaxe et le fonctionnement, nous utilisons les packages ``Pytest`` et ``Flake8``

Pytest
******

Pour lancer les différents tests du code, vous devez utiliser la commande suivante à la racine du projet :

.. code-block:: bash

   pytest

Le code effectuera tous les tests créés. Il va également créer un rapport de test au format ``HTML``. Celui-ci prendra comme nom ``coverage_html_report``.

Les paramètres de lancement de ``Pytest`` sont disponibles dans le fichier ``setup.cfg`` dans la rubrique ``[tool:pytest]``.

Concernant les paramètres de couverture et de rapport ``HTML``, ceux-ci sont disponibles dans le fichier ``.coveragerc``.

Flake8
******

Pour lancer le linter pour la syntaxe du code, vous devez vous rendre à la racine du projet et effectuer la commande suivante :

.. code-block:: bash

   flake8

Cela affichera toutes les erreurs de syntaxe présentes dans votre code.

.. note::

   Si l'exécution du code ne retourne rien, bonne nouvelle ! Cela veut dire que ``Flake8`` ne détecte aucune erreur de syntaxe.

Les paramètres de ``Flake8`` sont disponibles dans le fichier ``setup.cfg`` dans la rubrique ``[flake8]``.
