# Generated by Django 2.2.3 on 2019-10-24 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20191023_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heatmap', models.TextField()),
                ('dataspace', models.TextField()),
            ],
        ),
    ]