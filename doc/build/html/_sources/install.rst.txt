Installation du projet localement
=================================

Prérequis
---------
- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Installation
------------

Cloner le dépôt
~~~~~~~~~~~~~~~
Pour débuter l'installation, vous devez commencer par cloner le dépôt. Pour cela, vous devez effectuer les commandes suivantes :

.. code-block:: bash

   cd /path/to/put/project/in
   git clone https://github.com/Fibuc/OC-Lettings

Créer votre environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensuite vous devrez créer un environnement virtuel. Pour cela, suivez les étapes ci-dessous.

.. code-block:: bash

   cd /path/to/OC-Lettings
   python -m venv venv

.. note::

   Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur ``Ubuntu``, effectuez cette commande.

   .. code-block:: bash

      apt-get install python3-venv

   
Activez votre environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Linux / macOS
^^^^^^^^^^^^^

.. code-block:: bash

   source venv/bin/activate

Windows
^^^^^^^

*Via CMD*
*********

.. code-block:: bash

   venv/Scripts/activate.bat

*Via PowerShell*
****************

.. code-block:: bash

   venv/Scripts/activate.ps1

Préparer l'environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour que le projet fonctionne correctement, vous aurez besoin d'installer les packages nécessaires à son fonctionnement.

.. code-block:: bash

   pip install --requirement requirements.txt

Voilà maintenant que notre environnement est préparé, nous pouvons passer au lancement du projet en local.
