# Generated by Django 3.0.6 on 2020-05-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileupload',
            old_name='file',
            new_name='myfile',
        ),
        migrations.AddField(
            model_name='fileupload',
            name='title',
            field=models.CharField(default='hello', max_length=100),
        ),
    ]
