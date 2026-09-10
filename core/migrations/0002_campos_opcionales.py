from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='razon_social',
            field=models.CharField(blank=True, max_length=255, verbose_name='Razón Social'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre_comercial',
            field=models.CharField(blank=True, max_length=255, verbose_name='Nombre Comercial'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nif',
            field=models.CharField(blank=True, max_length=50, verbose_name='NIF / VAT Number'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tamano_empresa',
            field=models.CharField(blank=True, choices=[('micro', 'Microempresa'), ('pequena', 'Pequeña'), ('mediana', 'Mediana'), ('grande', 'Grande')], max_length=20, verbose_name='Tamaño Empresa'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='industria',
            field=models.CharField(blank=True, choices=[('tecnologia', 'Tecnología'), ('salud', 'Salud'), ('finanzas', 'Finanzas'), ('educacion', 'Educación'), ('comercio', 'Comercio'), ('otros', 'Otros')], max_length=50, verbose_name='Industria/Vertical'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='pais',
            field=models.CharField(blank=True, max_length=100, verbose_name='País/Región'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sitio_web',
            field=models.URLField(blank=True, verbose_name='Sitio web'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numero_contacto',
            field=models.CharField(blank=True, max_length=50, verbose_name='No. Contacto'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_primer_contacto',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha 1er contacto'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_firma_contrato',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha firma contrato'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='estado_cliente',
            field=models.CharField(blank=True, choices=[('', '---------'), ('prospecto', 'Prospecto'), ('activo', 'Activo'), ('inactivo', 'Inactivo')], max_length=20, verbose_name='Estado de cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='herramienta',
            field=models.CharField(blank=True, help_text='Herramienta utilizada (opcional)', max_length=100, verbose_name='Herramienta'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proyectos', to='core.cliente'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion',
            field=models.TextField(blank=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='url',
            field=models.URLField(blank=True, verbose_name='URL del proyecto'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='repo_url',
            field=models.URLField(blank=True, verbose_name='URL del repositorio'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='contrato',
            field=models.FileField(blank=True, null=True, upload_to='contratos/', verbose_name='Contrato (PDF)'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='proceso',
            field=models.CharField(choices=[('activo', 'Activo'), ('terminado', 'Terminado'), ('entregado', 'Entregado'), ('inactivo', 'Inactivo')], default='activo', max_length=20, verbose_name='Proceso'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='facturacion_estado',
            field=models.CharField(choices=[('no_aplica', 'No aplica'), ('por_pagar', 'Por pagar'), ('pagado', 'Pagado')], default='no_aplica', max_length=20, verbose_name='Facturación'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='facturacion_valor',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='titulo',
            field=models.CharField(blank=True, max_length=255, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(blank=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='categoria',
            field=models.CharField(choices=[('actols', 'Actols'), ('andres', 'Andrés'), ('camilo', 'Camilo')], default='actols', max_length=20),
        ),
        migrations.AlterField(
            model_name='enlace',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='enlace',
            name='url',
            field=models.URLField(blank=True, verbose_name='URL'),
        ),
    ]
