## Résumé
Projet OC d'entraînement à l'intégration continue et au déploiement continu avec:

- Django
- CircleCI
- Heroku
- Docker

### Site web d'Orange County Lettings

(Pas de mise en forme demandée, seulement la transmission des staticfiles
vers le site web, notamment sur django admin.)

## Développement local

### Prérequis indiqués pour réaliser le projet
- Interpréteur Python, version 3.6 ou supérieure
- Compte GitHub
- Git CLI
- SQLite3 CLI

Ajouter :
- créer un compte Heroku (gratuit)
- installer Heroku CLI
- créer un compte CircleCI
- créer un compte Docker
- installer Docker Desktop et/ou docker daemon


#### Pour cloner le repository de open classroom avant modifications :
(La consigne était de corriger le linting, la pluralisation de adress et 
refactoriser pour séparer les éléments de lettings et profiles en deux
applications django distinctes)

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel
##### MAC / LINUX

- `cd /path/to/Python-OC-Lettings-FR`
(ou dans un autre dossier à condition de l'activer depuis le bon dossier)
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site localement

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer
(vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires
( A ajouter si vous utilisez le repository de OC.
La consigne était: ajouter des tests unitaires pour chaque vue,
les tests doivent être dans leur app respective

NB : sachant que Pytest est utilisé, il aurait été normal de mettre tous les tests
dans le dossier test à la racine du projet pour que conftest.py
soit plus facilement utilisé, notamment. )

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données
Warning : le nom de la table exemple donnée par OC n'est pas bonne,
il faut donner le bon nom, récupéré grace à .tables
Par ailleurs : il semblerait que la méthode voulue pour le transfert de données
soit les migrations django, les manipulations indiquées ici ne sont là que
pour information.
Enfin, sur windows, même pour les utilisateurs de wsl,
il faut télécharger sqlite.exe, l'ajouter au path via les paramètres systèmes
et le lancer depuis le dossier où se trouve la base de donnée, dans powershell.

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- exemple de requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

##### WINDOWS

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`
- sqlite : cf "BASE DE DONNEES"

### Déploiement

Pour créer une nouvelle application sur Heroku en utilisant le pipeline Circleci
(développé dans cicleci/config.yml au moyen de l'orb heroku
officiel fourni par circleci):

- sur le site Heroku.com : "new" -> "create new app":
  saisir le nom de l'app et bien choisir la region europe
(risque de changement de paramètres sinon?)
- bien être connecté avec `heroku : login` et `heroku container:login`
  - vérifier les settings de la nouvelle app :
  si stack est sur heroku-20 (default) on peut changer le reglage avec `heroku stack:set container`
  - APP_NAME doit être correct dans les variables d'environnement de circleci, de même que
  - HEROKU_API_KEY, que l'on peut obtenir ou renouveler avec `heroku auth:token`
  - on peut spécifier à circleci la branche github à utiliser pour le déploiement
  avec la variable d'environnement CIRCLE_BRANCH, ici master

Ensuite il suffit de faire un commit sur la branche master,
ce qui déclenchera le pipeline avec le job build-lint-tests puis le job déploiement
avec les modifications si les premières étapes
(linting avec flake8 puis tests avec pytest) ont été passées avec succès.