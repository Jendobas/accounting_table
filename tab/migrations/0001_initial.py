# Generated by Django 4.2.5 on 2023-09-21 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=80)),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(blank=True, max_length=20)),
                ('structure', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
