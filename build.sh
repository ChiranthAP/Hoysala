#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Create static directory if it doesn't exist
mkdir -p staticfiles

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Create a superuser if it doesn't exist
python manage.py shell << END
from django.contrib.auth import get_user_model
import os
User = get_user_model()
if not User.objects.filter(username=os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')).exists():
    User.objects.create_superuser(
        os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin'),
        os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com'),
        os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin')
    )
END