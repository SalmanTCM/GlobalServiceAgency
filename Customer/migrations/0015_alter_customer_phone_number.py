# Generated by Django 4.2.5 on 2024-02-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0014_alter_customer_booking_type_alter_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]