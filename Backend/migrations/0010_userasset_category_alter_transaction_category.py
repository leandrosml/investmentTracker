# Generated by Django 5.0.3 on 2024-05-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0009_alter_transaction_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userasset',
            name='category',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(default='', max_length=10),
        ),
    ]