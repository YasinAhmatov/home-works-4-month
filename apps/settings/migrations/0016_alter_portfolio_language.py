# Generated by Django 4.2.6 on 2023-11-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0015_rename_title_portfolio_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='language',
            field=models.CharField(max_length=255, verbose_name='язык'),
        ),
    ]