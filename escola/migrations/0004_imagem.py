# Generated by Django 4.2.2 on 2023-06-18 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_aluno_celular'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
    ]