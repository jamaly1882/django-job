# Generated by Django 2.0.13 on 2020-09-20 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200920_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='store.Order'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shippingadress',
            name='order',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='store.Order'),
            preserve_default=False,
        ),
    ]
