# Generated by Django 4.2.13 on 2024-08-04 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_approach_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approach',
            new_name='approved',
        ),
    ]