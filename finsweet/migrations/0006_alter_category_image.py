# Generated by Django 4.2 on 2025-01-06 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finsweet', '0005_alter_about_us_options_alter_our_mission_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(
                blank=True, null=True,
                upload_to='categories'),
        ),
    ]
