# Generated by Django 4.1.3 on 2022-11-18 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
            ],
        ),
    ]
