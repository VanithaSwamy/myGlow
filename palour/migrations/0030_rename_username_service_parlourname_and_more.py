# Generated by Django 4.1.7 on 2023-04-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palour', '0029_alter_servicemaster_service_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='username',
            new_name='parlourname',
        ),
        migrations.AlterField(
            model_name='servicemaster',
            name='service_name',
            field=models.CharField(choices=[('Hair Spa', 'Hair Spa'), ('Manicure', 'Manicure'), ('Hair Straiting', 'Hair Straiting'), ('facial', 'facial'), ('Threading', 'Threading'), ('Pedicure', 'Pedicure'), ('makeup', 'makeup')], max_length=20),
        ),
    ]
