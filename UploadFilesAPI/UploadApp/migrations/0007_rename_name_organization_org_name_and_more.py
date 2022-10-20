# Generated by Django 4.0.4 on 2022-05-05 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadApp', '0006_alter_bills_bill_number_alter_organization_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='name',
            new_name='org_name',
        ),
        migrations.AlterField(
            model_name='bills',
            name='bill_number',
            field=models.IntegerField(verbose_name='Номер счета клиента'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='bill_sum',
            field=models.IntegerField(null=True, verbose_name='Сумма на счете'),
        ),
        migrations.AlterUniqueTogether(
            name='organization',
            unique_together={('org_name', 'client_name')},
        ),
    ]
