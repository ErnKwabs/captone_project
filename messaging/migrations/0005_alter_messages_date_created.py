# Generated by Django 4.2.6 on 2023-10-25 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("messaging", "0004_messages_user_id_alter_messages_date_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="messages",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 10, 25, 15, 26, 2, 656751, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]