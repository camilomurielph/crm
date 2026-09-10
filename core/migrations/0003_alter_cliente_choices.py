from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_campos_opcionales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tamano_empresa',
            field=models.CharField(
                blank=True,
                choices=[
                    ('independiente', 'Independiente'),
                    ('micro', 'Microempresa'),
                    ('pequena', 'Pequeña'),
                    ('mediana', 'Mediana'),
                    ('grande', 'Grande'),
                ],
                max_length=20,
                verbose_name='Tamaño Empresa',
            ),
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
                verbose_name='Industria/Vertical',
            ),
        ),
    ]
