# Generated by Django 2.1.4 on 2018-12-16 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contacts',
            field=models.ManyToManyField(blank=True, to='contacts.Contact'),
        ),
    ]
