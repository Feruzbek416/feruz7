# Generated by Django 4.1.3 on 2022-12-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dars', '0002_news1_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Python',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=100)),
                ('year', models.IntegerField()),
                ('kurs', models.CharField(blank=True, choices=[('Python', 'Python'), ('Java', 'Java'), ('Javascript', 'Javascript')], max_length=10)),
            ],
        ),
    ]
