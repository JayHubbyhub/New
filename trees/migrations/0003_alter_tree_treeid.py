# Generated by Django 4.2 on 2023-04-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0002_tree_treeid_alter_tree_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='treeID',
            field=models.IntegerField(null=True),
        ),
    ]
