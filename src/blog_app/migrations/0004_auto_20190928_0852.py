# Generated by Django 2.2 on 2019-09-28 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20190925_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.TextField(max_length=120),
        ),
    ]
