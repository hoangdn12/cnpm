# Generated by Django 3.0.4 on 2020-04-02 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_myuser_make_varify_email_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='make_varify_email_at',
            new_name='make_verify_email_at',
        ),
    ]
