# Generated by Django 2.2.3 on 2020-03-21 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_otherdata_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherdata',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
    ]