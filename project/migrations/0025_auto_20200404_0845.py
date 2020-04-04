# Generated by Django 2.2.3 on 2020-04-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0024_auto_20200404_0732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otherdata',
            name='Edges',
        ),
        migrations.AddField(
            model_name='otherdata',
            name='Static_Edges',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='otherdata',
            name='Temporal_Edges',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='otherdata',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]