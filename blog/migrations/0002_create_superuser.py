from django.contrib.auth.models import User
from django.db import migrations


def create_superuser(apps, schema_editor):
    superuser = User.objects.create(
        is_active=True,
        is_superuser=True,
        is_staff=True,
        username='admin',
        password='mmusic123')

    superuser.set_password(superuser.password)
    superuser.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
