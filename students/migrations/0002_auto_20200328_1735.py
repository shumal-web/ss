# Generated by Django 2.2.3 on 2020-03-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='racks',
        ),
    ]
