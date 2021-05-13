# Generated by Django 3.2.2 on 2021-05-10 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-date_joined_for_format',), 'verbose_name_plural': 'Products'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='created',
            new_name='date_joined_for_format',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='updated',
            new_name='last_login_for_format',
        ),
    ]