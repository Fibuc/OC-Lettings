Démarrage rapide
================

Ajout du fichier d'environnement
--------------------------------

Pour lancer localement notre projet, nous allons devoir paramétrer le fichier d'environnement. Renommez le fichier ``base.env`` en ``.env`` puis remplissez les données nécessaires.

.. code-block:: text

   SECRET_KEY=#Insérer votre clé secrète du projet Django.
   SENTRY_DSN=#Insérer votre URL de votre Sentry.
   DEBUG_STATUS=True #Utilisation de l'application en mode Debug (True ou False). Défaut True.
   PORT=8000 #Port externe souhaité pour l'accès en local (utilisation pour Docker). Défaut 8000.

Lancement du serveur via Python
-------------------------------

.. code-block:: bash

   python manage.py runserver

Lorsque le serveur est lancé, allez sur `http://localhost:8000/ <http://localhost:8000/>`_ dans un navigateur.

Lancement du serveur via Docker
-------------------------------

.. code-block:: bash

   docker compose up

Lorsque le serveur est lancé, allez sur `http://localhost:8000/ <http://localhost:8000/>`_ dans un navigateur.

.. note::

   Si vous avez configuré un autre port dans votre fichier ``.env``, le lien doit être modifié avec le nouveau port.

   Exemple ``.env``:

   .. code-block:: text

      ...
      PORT=4000
   
   Lien d'accès: `http://localhost:4000/ <http://localhost:4000/>`_


Panel d'administration
----------------------

Pour accéder au panel d'administration, rendez-vous sur `http://localhost:8000/admin <http://localhost:8000/admin>`_.
 
Connectez-vous avec l'utilisateur ``admin``, mot de passe ``Abc1234!``
