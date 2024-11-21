Déploiement
===========

Le déploiement du projet se fait sur la plateforme AWS.
Le projet est configuré pour être déployé automatiquement grâce à un pipeline CI/CD.
Ce déploiement se déclenche uniquement dans certaines conditions et suit des étapes précises pour garantir que tout fonctionne correctement.

Prérequis
---------

Accès Docker Hub
****************

- Un compte Docker Hub.
- Le compte Docker Hub doit avoir les permissions nécessaires pour ``push`` des images.

Un projet Sentry
****************

- Un projet Sentry configuré.
- Une adresse DSN accessible.

Une instance AWS
****************

- Un compte AWS.
- Une instance de AWS EC2 bien paramétrée.

.. note::

   Pour configurer l'instance EC2, vous pouvez consulter `notre tutoriel <create_instance.html>`_
   ou bien regarder cette `vidéo YouTube <https://www.youtube.com/watch?v=eQ6i-Ftx9hw&list=PLqoUmUbJ_zDHPwK-ZWATXiYrUXwWkLY65&index=2>`_ explicative.

Secrets GitHub configurés
*************************

Les variables suivantes doivent être définies dans les *secrets* GitHub:

- ``AWS_HOST`` : Adresse IP publique de l'instance AWS.
- ``AWS_TOKEN`` : Clé SSH privée d'accès ``.pem`` liée à l'instance.
- ``AWS_USERNAME`` : Nom d'utilisateur lié à l'instance AWS (par défaut laissez ``ec2-user``).
- ``DEBUG_STATUS`` : Statut de débug de l'application (Mettre ``False``).
- ``DJANGO_SECRET_KEY`` : Clé secrète de l'application Django.
- ``DOCKERHUB_USERNAME`` : Nom d'utilisateur de votre Docker Hub.
- ``DOCKERHUB_TOKEN`` : Clé d'accès de Docker Hub.
- ``SENTRY_DSN`` : Lien du DSN de Sentry.

.. warning::

   Si ces variables sont absentes ou incorrectes, le pipeline risque d'échouer.

Un ``push`` ou un ``pull request`` sur la branche ``main`` 
**********************************************************

Le déploiement s'effectue uniquement lorsqu'un ``push`` ou une ``pull request`` est effectué sur la branche ``main``.

Si une action est effectuée sur une autre branche que la branche main, alors cela effectuera uniquement les tests unitaires, d'intégration et le linter.

.. tip::

   Avant d'effectuer une action sur la branche main, testez le code avec ``Flake8`` et ``Pytest`` localement afin de limiter les erreurs sur le pipeline.
   De plus, assurez-vous que les variables d'environnement sont correctement définies dans les *Secrets* GitHub.

Étapes du pipeline
-----------

1. Tests et linter
******************

   - Test de la syntaxe du code avec ``Flake8``
   - Test des fonctions avec ``Pytest``.

.. warning::

   La converture des tests via ``Pytest`` doit être **au minimum** de 80% pour que les tests soient considérés comme valides.

   La réussite des tests unitaires, d'intégration et de syntaxe est une **condition obligatoire** pour la suite de l'exécution du pipeline.

   Si ces étapes échouent, alors le pipeline s'arrêtera.

2. Build de l’Image Docker
**************************

   - Une image Docker est construite à partir du projet.
   - L'image Docker est tag ``DOCKERHUB_USERNAME/oc-lettings:ID_du_commit`` et ``DOCKERHUB_USERNAME/oc-lettings:latest``
   - L'image est ``push`` dans le Docker Hub.

.. warning::

   La réussite du ``build`` et du ``push`` de l'image Docker est une **condition obligatoire** pour la suite de l'exécution du pipeline.

   Si ces étapes échouent, alors le pipeline s'arrêtera.

3. Déploiement automatique
**************************

   - Connexion à l'instance via SSH.
   - Arrêt et suppression du conteneur de l'image Docker déployée.
   - Téléchargement de la dernière version de l'image présente dans le Docker Hub.
   - Création du fichier d'environnement.
   - Démarrage de la dernière image Docker ``pull``.

Vérification du déploiement
---------------------------

Pour vérifier que le pipeline s'est déroulé correctement, regardez dans l'onglet ``Actions`` du dépôt GitHub. Normalement, vous devriez avoir la
validation de toutes les étapes.

.. image:: _static/img/success_pipeline.jpg
   :align: center

Maintenant que le pipeline est validé, pour s'assurer que le déploiement est un succès, allez voir le lien de votre instance ``http://<ip_publique_de_l'instance>/``.
