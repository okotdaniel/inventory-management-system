# Generated by Django 3.1.4 on 2021-01-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_auto_20210105_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronics',
            name='Brand',
            field=models.CharField(choices=[('Dell', 'Dell'), ('Hp', 'Hp'), ('Lenovo', 'Lenovo'), ('Acer', 'Acer'), ('Others', 'Others')], max_length=200, null=True),
        ),
    ]
