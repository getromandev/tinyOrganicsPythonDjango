# Generated by Django 3.2.5 on 2021-08-09 04:34

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tinyOrganicApp', '0004_alter_customerformmodel_anyalergies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerformmodel',
            name='anyAlergies',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'milk'), (2, 'eggs'), (3, 'soybean'), (4, 'fish'), (5, 'shellfish'), (6, 'treenuts'), (7, 'peanuts'), (8, 'wheat')], max_length=8),
        ),
    ]
