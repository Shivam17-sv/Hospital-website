# Generated by Django 5.0.6 on 2024-07-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Subject', models.CharField(max_length=50)),
                ('Phone', models.IntegerField()),
                ('Message', models.TextField()),
            ],
        ),
    ]