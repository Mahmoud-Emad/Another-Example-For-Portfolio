# Generated by Django 3.1.1 on 2020-10-19 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250, verbose_name='Name Of User')),
                ('Subject', models.CharField(max_length=350, verbose_name='Subject Of User')),
                ('Email', models.EmailField(max_length=350, verbose_name='Email Of User')),
                ('Message', models.TextField(max_length=1000, verbose_name='Message Of User')),
            ],
        ),
    ]