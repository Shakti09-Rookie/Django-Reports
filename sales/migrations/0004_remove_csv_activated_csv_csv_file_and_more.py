# Generated by Django 4.1.1 on 2022-09-20 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_position_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csv',
            name='activated',
        ),
        migrations.AddField(
            model_name='csv',
            name='csv_file',
            field=models.FileField(null=True, upload_to='csvs'),
        ),
        migrations.AlterField(
            model_name='csv',
            name='file_name',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
