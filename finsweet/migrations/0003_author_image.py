# Generated by Django 4.2 on 2025-01-06 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finsweet', '0002_alter_post_options_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='authors'),
        ),
    ]
