# Generated by Django 2.1.4 on 2018-12-16 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_holder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='holder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
