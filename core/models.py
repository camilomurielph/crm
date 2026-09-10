from django.db import models

class Cliente(models.Model):
    TAMANO_EMPRESA_CHOICES = [
        ('micro', 'Microempresa'),
        ('pequena', 'Pequeña'),
        ('mediana', 'Mediana'),
        ('grande', 'Grande'),
    ]
    INDUSTRIA_CHOICES = [
        ('tecnologia', 'Tecnología'),
        ('salud', 'Salud'),
        ('finanzas', 'Finanzas'),
        ('educacion', 'Educación'),
        ('comercio', 'Comercio'),
        ('otros', 'Otros'),
    ]
    ESTADO_CLIENTE_CHOICES = [
        ('', '---------'),
        ('prospecto', 'Prospecto'),
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    razon_social = models.CharField(max_length=255, blank=True, verbose_name="Razón Social")
    nombre_comercial = models.CharField(max_length=255, blank=True, verbose_name="Nombre Comercial")
    nif = models.CharField(max_length=50, blank=True, verbose_name="NIF / VAT Number")
    tamano_empresa = models.CharField(max_length=20, choices=TAMANO_EMPRESA_CHOICES, blank=True, verbose_name="Tamaño Empresa")
    industria = models.CharField(max_length=50, choices=INDUSTRIA_CHOICES, blank=True, verbose_name="Industria/Vertical")
    pais = models.CharField(max_length=100, blank=True, verbose_name="País/Región")
    sitio_web = models.URLField(blank=True, verbose_name="Sitio web")
    numero_contacto = models.CharField(max_length=50, blank=True, verbose_name="No. Contacto")
    email = models.EmailField(blank=True, verbose_name="Email")
    fecha_primer_contacto = models.DateField(null=True, blank=True, verbose_name="Fecha 1er contacto")
    fecha_firma_contrato = models.DateField(null=True, blank=True, verbose_name="Fecha firma contrato")
    estado_cliente = models.CharField(max_length=20, choices=ESTADO_CLIENTE_CHOICES, blank=True, verbose_name="Estado de cliente")
    herramienta = models.CharField(max_length=100, blank=True, help_text="Herramienta utilizada (opcional)", verbose_name="Herramienta")

    def __str__(self):
        return self.razon_social or f"Cliente #{self.pk}"

class Proyecto(models.Model):
    PROCESO_CHOICES = [
        ('activo', 'Activo'),
        ('terminado', 'Terminado'),
        ('entregado', 'Entregado'),
        ('inactivo', 'Inactivo'),
    ]
    FACTURACION_CHOICES = [
        ('no_aplica', 'No aplica'),
        ('por_pagar', 'Por pagar'),
        ('pagado', 'Pagado'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, related_name='proyectos', null=True, blank=True)
    nombre = models.CharField(max_length=255, blank=True, verbose_name="Nombre")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    url = models.URLField(blank=True, verbose_name="URL del proyecto")
    repo_url = models.URLField(blank=True, verbose_name="URL del repositorio")
    contrato = models.FileField(upload_to='contratos/', blank=True, null=True, verbose_name="Contrato (PDF)")
    proceso = models.CharField(max_length=20, choices=PROCESO_CHOICES, default='activo', verbose_name="Proceso")
    facturacion_estado = models.CharField(max_length=20, choices=FACTURACION_CHOICES, default='no_aplica', verbose_name="Facturación")
    facturacion_valor = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True, verbose_name="Valor")

    def __str__(self):
        return self.nombre or f"Proyecto #{self.pk}"

class Tarea(models.Model):
    CATEGORIA_CHOICES = [
        ('actols', 'Actols'),
        ('andres', 'Andrés'),
        ('camilo', 'Camilo'),
    ]
    titulo = models.CharField(max_length=255, blank=True, verbose_name="Título")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    completada = models.BooleanField(default=False)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='actols')
    creada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo or f"Tarea #{self.pk}"

class Enlace(models.Model):
    nombre = models.CharField(max_length=255, blank=True, verbose_name="Nombre")
    url = models.URLField(blank=True, verbose_name="URL")

    def __str__(self):
        return self.nombre or f"Enlace #{self.pk}"
