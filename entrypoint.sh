#!/bin/sh

mkdir -p /app/data
chmod 777 /app/data

# Generar migraciones (por si no existen o hay cambios nuevos)
python manage.py makemigrations core --noinput

# Aplicar migraciones
python manage.py migrate --noinput

# Crear usuarios si no existen
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
for username, password in [('camilomuriel', 'b55f86bd4c353'), ('andresfel', 'BDA98@')]:
    user, created = User.objects.get_or_create(username=username)
    if created:
        user.set_password(password)
        user.save()
        print(f'Usuario {username} creado.')
    else:
        print(f'Usuario {username} ya existe.')
"

exec gunicorn --bind 0.0.0.0:8000 actols_crm.wsgi:application
