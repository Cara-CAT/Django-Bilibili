# Generated by Django 2.2.5 on 2020-12-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('passingcode', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
