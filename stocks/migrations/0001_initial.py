# Generated by Django 3.1.7 on 2022-03-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stockval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('open', models.CharField(max_length=20)),
                ('high', models.CharField(max_length=20)),
                ('low', models.CharField(max_length=20)),
                ('close', models.CharField(max_length=20)),
                ('adj_close', models.CharField(max_length=20)),
                ('volume', models.CharField(max_length=20)),
            ],
        ),
    ]
