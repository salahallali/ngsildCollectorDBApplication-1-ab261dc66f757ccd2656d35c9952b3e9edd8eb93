# Generated by Django 3.1.3 on 2021-07-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notifications_Reciver', '0003_service_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='name',
            field=models.CharField(default='serv', max_length=100),
            preserve_default=False,
        ),
    ]