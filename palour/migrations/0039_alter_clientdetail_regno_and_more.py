# Generated by Django 4.1.7 on 2023-04-24 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palour', '0038_alter_servicemaster_service_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetail',
            name='regno',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='servicemaster',
            name='service_name',
            field=models.CharField(choices=[('Bleach', 'Bleach'), ('Haircuts', 'Haircuts'), ('Manicure', 'Manicure'), ('Hair straightening', 'Hair straightening'), ('Facial', 'Facial'), ('Waxing', 'Waxing'), ('Threading', 'Threading'), ('Makeup', 'Makeup'), ('Hairstyling', 'Hairstyling'), ('Pedicure', 'Pedicure'), ('Hair Spa', 'Hair Spa'), ('Nail art', 'Nail art'), ('Hair coloring/Highlights', 'Hair coloring/Highlights'), ('Hair smoothening', 'Hair smoothening')], max_length=50, unique=True),
        ),
    ]
