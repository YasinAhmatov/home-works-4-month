# Generated by Django 4.2.6 on 2023-11-03 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_user/')),
                ('name', models.CharField(max_length=100)),
                ('work', models.CharField(max_length=50)),
                ('descriptions', models.TextField()),
            ],
        ),
    ]