# Generated by Django 2.2.1 on 2019-05-30 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SinglePage',
        ),
    ]
