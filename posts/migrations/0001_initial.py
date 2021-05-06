# Generated by Django 3.1.7 on 2021-05-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(choices=[('Data', 'Data'), ('Business', 'Business'), ('Engineering', 'Engineering'), ('Random', 'Random')])),
                ('name', models.TextField()),
                ('time_posted', models.DateField()),
                ('content', models.TextField()),
            ],
        ),
    ]
