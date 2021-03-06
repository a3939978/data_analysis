# Generated by Django 2.2.3 on 2020-03-10 12:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_auto_20200210_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='otherData',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Nodes', models.IntegerField(default=0)),
                ('Temporal_Edges', models.IntegerField(default=0)),
                ('Static_Edges', models.IntegerField(default=0)),
                ('TimeSpan', models.IntegerField(default=0)),
                ('min_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('max_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('max_degree', models.IntegerField()),
                ('min_degree', models.IntegerField()),
                ('average_degree', models.IntegerField()),
                ('heatmap', models.TextField()),
                ('dataspace', models.TextField()),
                ('total_communities', models.TextField()),
                ('force_nodes', models.TextField()),
                ('force_links', models.TextField()),
                ('communities', models.TextField()),
                ('size', models.IntegerField(default=0)),
                ('distribution', models.TextField()),
            ],
        ),
    ]
