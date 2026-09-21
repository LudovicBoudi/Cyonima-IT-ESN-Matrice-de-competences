#!/bin/sh
set -e

# Attente de la base PostgreSQL le cas échéant
if [ "$DB_ENGINE" = "postgres" ]; then
    python - <<'PY'
import os, time
import psycopg

host = os.environ.get("POSTGRES_HOST", "db")
port = os.environ.get("POSTGRES_PORT", "5432")
user = os.environ.get("POSTGRES_USER", "gpec")
password = os.environ.get("POSTGRES_PASSWORD", "gpec")
dbname = os.environ.get("POSTGRES_DB", "gpec_it")

for _ in range(30):
    try:
        psycopg.connect(host=host, port=port, user=user, password=password, dbname=dbname)
        break
    except psycopg.OperationalError:
        time.sleep(1)
else:
    raise SystemExit("Base de données indisponible.")
PY
fi

python manage.py migrate --noinput
python manage.py seed_skills

# Création du superutilisateur initial (si configuré)
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
    python manage.py shell -c "
from accounts.models import User
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser(
        username='$DJANGO_SUPERUSER_USERNAME',
        email='${DJANGO_SUPERUSER_EMAIL:-admin@example.com}',
        password='$DJANGO_SUPERUSER_PASSWORD',
        role='admin',
    )
    print('Superutilisateur créé.')
else:
    print('Superutilisateur déjà présent.')
"
fi

exec "$@"
