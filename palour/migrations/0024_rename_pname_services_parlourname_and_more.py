# Generated by Django 4.1.7 on 2023-04-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palour', '0023_alter_servicemaster_service_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='pname',
            new_name='parlourname',
        ),
        migrations.AlterField(
            model_name='servicemaster',
            name='service_name',
            field=models.CharField(choices=[('Hair Straiting', 'Hair Straiting'), ('Manicure', 'Manicure'), ('Hair Spa', 'Hair Spa'), ('Pedicure', 'Pedicure'), ('Threading', 'Threading'), ('facial', 'facial'), ('makeup', 'makeup')], max_length=20),
        ),
    ]
