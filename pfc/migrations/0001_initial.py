# Generated by Django 3.1.2 on 2021-03-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pfc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pfc_name', models.CharField(default='-', max_length=100)),
            ],
        ),
    ]
