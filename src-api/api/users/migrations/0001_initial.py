# Generated by Django 3.0.6 on 2020-05-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=45, unique=True)),
                ('first_name', models.CharField(default=None, max_length=45, null=True)),
                ('last_name', models.CharField(default=None, max_length=45, null=True)),
                ('email', models.CharField(default=None, max_length=128, null=True)),
                ('password', models.CharField(max_length=128, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('dt_last_login', models.DateTimeField(default=None, null=True)),
                ('dt_created', models.DateTimeField()),
                ('dt_modified', models.DateTimeField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
