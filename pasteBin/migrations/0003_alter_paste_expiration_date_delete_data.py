# Generated by Django 4.2.4 on 2023-10-30 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasteBin', '0002_paste_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='expiration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]