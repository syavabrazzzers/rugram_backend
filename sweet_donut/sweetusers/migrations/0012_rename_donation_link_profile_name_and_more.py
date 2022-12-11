# Generated by Django 4.1.3 on 2022-12-08 16:31

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweetusers', '0011_rename_user_id_profile_user_alter_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='donation_link',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='widget_token',
            new_name='site',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='donutions_count',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='donutions_total',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='User1670517070', error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
