# Generated by Django 3.0.3 on 2020-09-16 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginProfessor', models.CharField(max_length=15)),
                ('nomeProfessor', models.CharField(max_length=50)),
                ('emailProfessor', models.CharField(max_length=40)),
            ],
        ),
    ]
