# Generated by Django 4.2 on 2023-04-11 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_owner_groups_owner_user_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holidayhome',
            name='owner',
        ),
        migrations.AddField(
            model_name='owner',
            name='homes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owners', to='base.holidayhome'),
        ),
    ]
