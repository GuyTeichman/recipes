# Generated by Django 3.0.7 on 2020-09-22 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0082_auto_20200922_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default', max_length=128)),
                ('message', models.CharField(default='', max_length=512)),
            ],
        ),
    ]
