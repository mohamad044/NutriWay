# Generated by Django 5.1.7 on 2025-04-30 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_payment_general_plan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='selected_duration',
            field=models.CharField(blank=True, choices=[('1_month', '1 Month'), ('3_months', '3 Months'), ('6_months', '6 Months'), ('12_months', '12 Months')], max_length=20, null=True),
        ),
    ]
