# Generated by Django 4.2.1 on 2023-10-08 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlist',
            name='end_time',
            field=models.DateTimeField(blank=True, default=45),
            preserve_default=False,
        ),
    ]
