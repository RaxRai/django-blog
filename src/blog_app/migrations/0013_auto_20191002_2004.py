# Generated by Django 2.2 on 2019-10-02 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0012_searchquery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image/'),
        ),
    ]
