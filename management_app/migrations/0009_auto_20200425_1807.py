# Generated by Django 3.0.5 on 2020-04-25 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_app', '0008_auto_20200425_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='selected_season',
            field=models.CharField(max_length=2),
        ),
    ]
