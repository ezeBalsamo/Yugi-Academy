# Generated by Django 4.1 on 2022-09-04 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoosterPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('code', models.CharField(max_length=10)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MonsterCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=8000)),
                ('type', models.CharField(choices=[('Normal', 'Normal'), ('Effect', 'Effect'), ('Ritual', 'Ritual'), ('Fusion', 'Fusion'), ('Synchro', 'Synchro'), ('Xyz', 'Xyz'), ('Pendulum', 'Pendulum'), ('Link', 'Link'), ('Token', 'Token')], max_length=10)),
                ('race', models.CharField(max_length=20)),
                ('attribute', models.CharField(choices=[('Dark', 'Dark'), ('Divine', 'Divine'), ('Earth', 'Earth'), ('Fire', 'Fire'), ('Light', 'Light'), ('Water', 'Water'), ('Wind', 'Wind')], max_length=10)),
                ('level', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpellCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=8000)),
                ('type', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrapCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=8000)),
                ('type', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BoosterPackCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=20, unique=True)),
                ('rarity', models.CharField(max_length=20)),
                ('card_id', models.PositiveIntegerField()),
                ('booster_pack', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='YuGiOh.boosterpack')),
                ('card_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.contenttype')),
            ],
        ),
    ]