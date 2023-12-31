# Generated by Django 4.2.5 on 2023-09-23 09:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_initiated', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Success', 'Success'), ('Failed', 'Failed'), ('Reconciliation', 'Reconciliation')], default='Pending', max_length=100)),
                ('staffs', models.JSONField()),
                ('total_amount_for_tax', models.BigIntegerField()),
                ('total_amount_for_salary', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=50)),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Taxroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount_paid_for_tax', models.BigIntegerField()),
                ('date_initiated', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Success', 'Success'), ('Failed', 'Failed'), ('Reconciliation', 'Reconciliation')], max_length=100)),
                ('staffs', models.JSONField()),
                ('payroll', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Main.payroll')),
            ],
        ),
        migrations.CreateModel(
            name='Staff_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_salary', models.BigIntegerField()),
                ('tax', models.BigIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.school')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('account_number', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=40)),
                ('salary_deduction', models.BigIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('tin_number', models.CharField(max_length=50)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.school')),
                ('staff_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Main.staff_type')),
            ],
        ),
        migrations.AddField(
            model_name='payroll',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.school'),
        ),
        migrations.CreateModel(
            name='Particulars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.school')),
            ],
        ),
        migrations.CreateModel(
            name='Operations_account_transaction_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('amount', models.BigIntegerField()),
                ('transaction_type', models.CharField(choices=[('Transfer', 'Transfer'), ('Cash', 'Cash')], max_length=100)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Success', 'Success'), ('Failed', 'Failed'), ('Cancelled', 'Cancelled'), ('Retrying', 'Retrying')], max_length=50)),
                ('transaction_category', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], max_length=50)),
                ('name_of_reciever', models.CharField(max_length=100)),
                ('account_number_of_reciever', models.CharField(max_length=20)),
                ('reciever_bank', models.CharField(blank=True, max_length=50, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('particulars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.particulars')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.school')),
            ],
        ),
        migrations.CreateModel(
            name='Operations_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Bank Account Name')),
                ('account_number', models.CharField(max_length=100, verbose_name='Account Number')),
                ('amount_available_cash', models.BigIntegerField()),
                ('amount_available_transfer', models.BigIntegerField()),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Main.school')),
            ],
        ),
        migrations.CreateModel(
            name='Capital_account_transaction_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('amount', models.BigIntegerField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.school')),
            ],
        ),
        migrations.CreateModel(
            name='Capital_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Bank Account Name')),
                ('account_number', models.CharField(max_length=100, verbose_name='Account Number')),
                ('amount_availabe', models.BigIntegerField()),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Main.school')),
            ],
        ),
    ]
