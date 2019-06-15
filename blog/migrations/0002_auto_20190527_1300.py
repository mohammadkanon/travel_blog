# Generated by Django 2.2.1 on 2019-05-27 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commoninfo',
            name='author_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='commoninfo',
            name='author_status',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='commoninfo',
            name='author_twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='commoninfo',
            name='author_youtube_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commoninfo',
            name='author_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='commoninfo',
            name='author_fb_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commoninfo',
            name='author_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
