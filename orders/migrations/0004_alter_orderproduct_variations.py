# Generated by Django 3.2.2 on 2021-05-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_reviewrating'),
        ('orders', '0003_alter_orderproduct_variations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]