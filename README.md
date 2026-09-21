# GPEC-IT — Matrice de compétences

Application web de gestion des compétences pour les managers d'ESN/SSII/ICT.
Elle permet aux employés de **s'auto-évaluer** sur leurs compétences, et aux
managers de consulter et gérer les profils de leurs collaborateurs.


---

## Fonctionnalités

- **Compétences organisées par catégories**, toutes deux administrables
  (ajout / modification / suppression).
- **Auto-évaluation** : l'employé sélectionne ses compétences dans chaque
  catégorie et leur attribue un niveau de **1 à 5 étoiles** (1 étoile minimum
  pour qu'une compétence soit conservée sur le profil).
- **Profil** : seules les compétences réellement sélectionnées par l'employé
  sont affichées (navigation par catégorie via un menu déroulant).
- **Managers** : consultation/édition des profils de leurs collaborateurs et
  **auto-assignation des employés sans manager** (sans solliciter les admins).
- **Interface sombre** (pas de thème clair) avec **menu latéral gauche**.
- **Administration** complète : comptes, catégories, compétences, assignations.

## Rôles et permissions

| Profil | Droits |
|---|---|
| **Administrateur** | Accès total, administration des comptes et assignation des utilisateurs à un manager. |
| **Manager** | Lecture/écriture sur les profils de ses collaborateurs + auto-assignation d'employés. |
| **Utilisateur** | Lecture/écriture sur son propre profil uniquement. |

## Stack technique

- Python 3.12, Django 6.1
- Base de données : SQLite (développement) ou PostgreSQL (production)
- Gunicorn (serveur WSGI), WhiteNoise (fichiers statiques)
- Conteneurisation : Docker + GitHub Actions (build & push GHCR)

## Modèle de données

| Modèle | Champs clés | Description |
|---|---|---|
| `accounts.User` | `role` (`admin`/`manager`/`user`), `manager` (FK self) | Utilisateur avec rôle et manager assigné. |
| `skills.Category` | `name`, `slug` | Catégorie de compétences. |
| `skills.Skill` | `name`, `category` (FK) | Compétence rattachée à une catégorie. |
| `skills.SkillLevel` | `user` (FK), `skill` (FK), `level` (0–5) | Auto-évaluation d'un utilisateur sur une compétence. |

> Une compétence est considérée comme « sélectionnée » sur le profil lorsque
> son niveau est ≥ 1. Un niveau à 0 ou une suppression retire la compétence du profil.

---

## Installation (développement)

```bash
# Créer l'environnement virtuel et installer les dépendances
python3 -m venv .venv            # ou : virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate

# Charger les catégories/compétences depuis le CCTP
python manage.py seed_skills

# Créer un superutilisateur
python manage.py createsuperuser

# Lancer le serveur de développement (port 8080)
python manage.py runserver 0.0.0.0:8080
```

L'application est alors accessible sur <http://localhost:8080>.

### Comptes de démonstration

| Rôle | Identifiant | Mot de passe |
|---|---|---|
| Administrateur | `admin` | `admin` |
| Manager | `manager` | `manager` |
| Utilisateur | `employe` | `employe` |

> Ces comptes sont créés à des fins de test local (voir
> `docker/entrypoint.sh` pour la création automatique du superutilisateur en
> conteneur).

---

## Déploiement Docker

### Avec Docker Compose (recommandé)

```bash
docker compose up --build
```

L'application est servie sur <http://localhost:8080> (PostgreSQL en base de
données, migrations et seed exécutés automatiquement au démarrage).

Un superutilisateur est créé automatiquement si les variables
`DJANGO_SUPERUSER_USERNAME` / `DJANGO_SUPERUSER_PASSWORD` sont définies.

### Image seule

```bash
docker build -t gpec-it .
docker run -p 8080:8000 \
  -e DJANGO_SECRET_KEY=change-me \
  -e DJANGO_ALLOWED_HOSTS="*" \
  -e DJANGO_SUPERUSER_USERNAME=admin \
  -e DJANGO_SUPERUSER_PASSWORD=admin \
  gpec-it
```

## Variables d'environnement

| Variable | Défaut | Description |
|---|---|---|
| `DJANGO_SECRET_KEY` | clé dev | Clé secrète Django (obligatoire en production). |
| `DJANGO_DEBUG` | `True` | Active le mode debug (`True`/`False`). |
| `DJANGO_ALLOWED_HOSTS` | `*` | Hôtes autorisés (séparés par des virgules). |
| `DB_ENGINE` | `sqlite` | `sqlite` ou `postgres`. |
| `SQLITE_PATH` | `db.sqlite3` | Chemin du fichier SQLite (si `DB_ENGINE=sqlite`). |
| `POSTGRES_DB` / `POSTGRES_USER` / `POSTGRES_PASSWORD` | `gpec_it` / `gpec` / `gpec` | Accès PostgreSQL. |
| `POSTGRES_HOST` / `POSTGRES_PORT` | `db` / `5432` | Hôte et port PostgreSQL. |
| `DJANGO_SUPERUSER_USERNAME` / `_PASSWORD` / `_EMAIL` | — | Création du superutilisateur initial (conteneur). |

---

## Intégration continue (GitHub Actions)

Le workflow `.github/workflows/docker-build.yml` :

1. **Tests** — installe les dépendances et exécute `python manage.py test`.
2. **Build & push** — construit l'image Docker et la publie sur **GitHub
   Container Registry** (`ghcr.io/<org>/<repo>`) à chaque push sur `main` et
   sur les tags `v*`.

Aucun secret à configurer : le token `GITHUB_TOKEN` fourni par GitHub suffit.

---

## Commandes utiles

```bash
python manage.py test            # Lancer les tests
python manage.py seed_skills      # (Re)charger les données du CCTP
python manage.py seed_skills --purge   # Supprimer puis recharger
python manage.py makemigrations   # Générer les migrations
python manage.py migrate          # Appliquer les migrations
python manage.py collectstatic    # Rassembler les fichiers statiques
```

## Structure du projet

```
.
├── CCTP/                      # Cahier des charges (source du seed)
├── docker/entrypoint.sh       # Script d'entrée du conteneur
├── gpec_it/                   # Configuration du projet (settings, urls)
├── accounts/                  # Utilisateurs, rôles, assignations
├── skills/                    # Catégories, compétences, niveaux
│   └── management/commands/seed_skills.py
├── templates/                 # Templates HTML (thème sombre)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .github/workflows/docker-build.yml
```

## Licence

Projet interne — Cyonima IT.
