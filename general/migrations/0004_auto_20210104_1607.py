# Generated by Django 3.1.4 on 2021-01-04 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_assignelectroncs'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignElectronics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.CharField(choices=[('cit', 'Computing and Information Tecnology'), ('sba', 'Procurement and Logistics'), ('oasis', 'oasis'), ('lab A', 'lab A'), ('lab B', 'lab B')], max_length=200, null=True)),
                ('Quantity', models.IntegerField(null=True)),
                ('Item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.electronics')),
            ],
        ),
        migrations.DeleteModel(
            name='AssignElectroncs',
        ),
    ]
