# Generated by Django 2.2.1 on 2019-05-29 06:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_singlepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='tour_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
