from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_cliente_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='vertical',
            field=models.CharField(blank=True, max_length=255, verbose_name='Vertical'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='industria',
            field=models.CharField(
                blank=True,
                choices=[
                    ('tecnologia', 'Tecnología'),
                    ('salud', 'Salud'),
                    ('finanzas', 'Finanzas'),
                    ('educacion', 'Educación'),
                    ('comercio', 'Comercio'),
                    ('servicios', 'Servicios'),
                    ('otros', 'Otros'),
                ],
                max_length=50,
                verbose_name='Industria',
            ),
        ),
    ]
