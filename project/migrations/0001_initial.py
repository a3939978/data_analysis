# Generated by Django 2.2.3 on 2019-07-24 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datainfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Type', models.CharField(max_length=200)),
                ('Nodes', models.IntegerField(default=0)),
                ('Temporal_Edges', models.IntegerField(default=0)),
                ('Static_Edges', models.IntegerField(default=0)),
                ('Description', models.CharField(max_length=200)),
            ],
        ),
    ]
