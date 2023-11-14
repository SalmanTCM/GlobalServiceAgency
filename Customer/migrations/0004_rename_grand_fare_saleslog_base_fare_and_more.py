# Generated by Django 4.2.5 on 2023-11-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0003_customer_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saleslog',
            old_name='grand_fare',
            new_name='base_fare',
        ),
        migrations.RenameField(
            model_name='saleslog',
            old_name='net_fare',
            new_name='discount',
        ),
        migrations.AddField(
            model_name='saleslog',
            name='tax',
            field=models.CharField(max_length=10, null=True),
        ),
    ]