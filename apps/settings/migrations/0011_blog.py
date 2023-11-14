# Generated by Django 4.2.6 on 2023-11-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0010_alter_experience_description2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=255, verbose_name='фото')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('description', models.CharField(max_length=255, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]