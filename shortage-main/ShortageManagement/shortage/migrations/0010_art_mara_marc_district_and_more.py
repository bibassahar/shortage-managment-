# Generated by Django 4.0.2 on 2022-05-19 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortage', '0009_remove_mb52_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='art_mara_marc',
            name='district',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='art_mara_marc',
            name='profit_center_designation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='art_mara_marc',
            name='scope_allocation',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
