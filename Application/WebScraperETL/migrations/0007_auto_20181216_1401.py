# Generated by Django 2.1.3 on 2018-12-16 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebScraperETL', '0006_opinion_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebScraperETL.Product'),
        ),
    ]
