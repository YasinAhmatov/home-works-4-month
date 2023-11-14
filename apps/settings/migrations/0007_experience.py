# Generated by Django 4.2.6 on 2023-11-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=255, verbose_name='год')),
                ('profession', models.CharField(max_length=255, verbose_name='профессия')),
                ('description', models.CharField(max_length=255, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'стаж',
                'verbose_name_plural': 'стажи',
            },
        ),
    ]