# Generated by Django 2.2.3 on 2020-02-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_subdata_distribution'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdata',
            name='average_degree',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subdata',
            name='max_degree',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subdata',
            name='min_degree',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
