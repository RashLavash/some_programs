# Generated by Django 5.0.2 on 2024-02-17 17:02

import posts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(validators=[posts.validators.validate_long_value]),
        ),
    ]