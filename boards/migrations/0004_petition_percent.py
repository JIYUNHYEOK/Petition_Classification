# Generated by Django 3.2.12 on 2023-05-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_staticdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='percent',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
