# Generated by Django 5.0.3 on 2024-05-03 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0006_remove_blogpost_author_delete_faq_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('Crypto', 'crypto'), ('etf', 'ETF'), ('stocks', 'Stocks')], default='buy', max_length=10),
        ),
    ]
