# Generated by Django 4.0.3 on 2022-03-07 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0008_remove_client_last_login_alter_client_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=500, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='client',
            name='password',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.CharField(max_length=500, unique=True, verbose_name='Username'),
        ),
    ]
