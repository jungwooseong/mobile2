# Generated by Django 4.2.6 on 2023-10-09 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='intruder_image/%Y/%m/%d/'),
        ),
    ]