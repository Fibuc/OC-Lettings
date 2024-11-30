La base de données
==================

SQLite 3
--------

La base de données est gérée via SQLite3, ce qui permet d'avoir une base de données légère et rapide. De plus, celle-ci permet d'être stockée dans les Images Docker.

Connexion à la base de données
------------------------------

.. important::

   Pour lancer un shell ``SQLite3``, il doit être préalablement installé. Si ce n'est pas fait, vous pouvez le télécharger via `ce lien <https://www.sqlite.org/download.html>`_ et l'installer selon votre système d'exploitation.

Premièrement, rendez-vous dans le dossier de l'application.

.. code-block:: bash

    cd /path/to/OC-Lettings

Ensuite, ouvrez une session shell ``sqlite3`` connectez-vous via :

.. code-block:: bash

    sqlite3 oc-lettings-site.sqlite3

À partir de là, vous pouvez afficher les tables en tapant ``.tables``.

Pour afficher les colonnes, vous pouvez effectuer la commande suivante (ici on prendra les profils en exemple) :

.. code-block:: bash

    pragma table_info('profiles_profile');

Lancez une requête sur la table des profils :

.. code-block:: bash

    select user_id, favorite_city from profiles_profile where favorite_city like 'B%';

Vous pouvez quitter à tout moment la session SQLite3 en saisissant ``.quit``

Structure de la base de données
-------------------------------

.. image:: _static/img/db_diagram.png
   :align: center
   :width: 70%

