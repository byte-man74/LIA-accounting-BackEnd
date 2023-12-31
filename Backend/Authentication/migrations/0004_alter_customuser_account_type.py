# Generated by Django 4.2.5 on 2023-09-27 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0003_alter_customuser_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='account_type',
            field=models.CharField(choices=[('OPERATIONS', 'OPERATIONS'), ('ACCOUNTANT', 'ACCOUNTANT'), ('PRINCIPAL', 'PRINCIPAL'), ('DIRECTOR', 'DIRECTOR')], default='Free Account', max_length=50, verbose_name='Account Type'),
        ),
    ]
