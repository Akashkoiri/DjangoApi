# Generated by Django 4.1.1 on 2022-12-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_color_color_color_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('car', models.CharField(max_length=30)),
                ('finish_time', models.IntegerField()),
            ],
        ),
    ]
