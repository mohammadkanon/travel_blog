# Generated by Django 2.2.1 on 2019-05-29 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_tour'),
    ]

    operations = [
        migrations.CreateModel(
            name='SinglePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_title', models.CharField(max_length=200)),
                ('single_content', models.TextField(blank=True, null=True)),
                ('single_pic', models.ImageField(blank=True, null=True, upload_to='single')),
            ],
        ),
    ]
