# Generated by Django 4.1 on 2022-10-01 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YuGiOh', '0003_spellcard_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spellcard',
            name='type',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Equip', 'Equip'), ('Continuous', 'Continuous'), ('Quick-Play', 'Quick-Play'), ('Field', 'Field'), ('Ritual', 'Ritual')], max_length=10),
        ),
    ]
