# Generated by Django 3.0.5 on 2020-04-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email_id', models.EmailField(max_length=50)),
                ('contact_no', models.CharField(max_length=50)),
            ],
        ),
    ]
