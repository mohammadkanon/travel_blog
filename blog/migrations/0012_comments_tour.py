# Generated by Django 2.2.1 on 2019-05-30 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_delete_singlepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Tour'),
        ),
    ]