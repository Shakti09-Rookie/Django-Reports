# Generated by Django 4.1.1 on 2022-09-20 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_alter_sale_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
