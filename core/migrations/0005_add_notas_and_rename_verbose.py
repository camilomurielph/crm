from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_add_vertical_field'),
    ]

    operations = [
        # Añadir campo notas a Cliente
        migrations.AddField(
            model_name='cliente',
            name='notas',
            field=models.TextField(blank=True, verbose_name='Notas'),
        ),
        # Añadir campo notas a Proyecto
        migrations.AddField(
            model_name='proyecto',
            name='notas',
            field=models.TextField(blank=True, verbose_name='Notas'),
        ),
        # Renombrar etiquetas (verbose_name)
        migrations.AlterField(
            model_name='cliente',
            name='razon_social',
            field=models.CharField(blank=True, max_length=255, verbose_name='Razón Social/Nombre Comercial'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre_comercial',
            field=models.CharField(blank=True, max_length=255, verbose_name='Nombre de contacto'),
        ),
        # Cambiar on_delete de Proyecto.cliente a CASCADE
        migrations.AlterField(
            model_name='proyecto',
            name='cliente',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='proyectos',
                to='core.cliente',
            ),
        ),
    ]
