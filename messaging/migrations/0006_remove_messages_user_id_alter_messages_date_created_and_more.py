# Generated by Django 4.2.6 on 2023-10-25 18:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("messaging", "0005_alter_messages_date_created"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="messages",
            name="user_id",
        ),
        migrations.AlterField(
            model_name="messages",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 10, 25, 18, 54, 52, 711798, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
