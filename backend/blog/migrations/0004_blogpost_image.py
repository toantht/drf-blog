# Generated by Django 4.2.5 on 2023-09-06 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_remove_blogpost_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="image",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
