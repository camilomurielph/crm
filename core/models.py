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
        ('prospecto', 'Prospecto'),
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    razon_social = models.CharField(max_length=255)
    nombre_comercial = models.CharField(max_length=255, blank=True)
    nif = models.CharField(max_length=50, blank=True, verbose_name="NIF / VAT Number")
    tamano_empresa = models.CharField(max_length=20, choices=TAMANO_EMPRESA_CHOICES, blank=True)
    industria = models.CharField(max_length=50, choices=INDUSTRIA_CHOICES, blank=True)
    pais = models.CharField(max_length=100, blank=True)
    sitio_web = models.URLField(blank=True)
    numero_contacto = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    fecha_primer_contacto = models.DateField(null=True, blank=True)
    fecha_firma_contrato = models.DateField(null=True, blank=True)
    estado_cliente = models.CharField(max_length=20, choices=ESTADO_CLIENTE_CHOICES, default='prospecto')
    herramienta = models.CharField(max_length=100, blank=True, help_text="Herramienta utilizada (opcional)")

    def __str__(self):
        return self.razon_social

class Proyecto(models.Model):
    PROCESO_CHOICES = [
        ('activo', 'Activo'),
        ('terminado', 'Terminado'),
        ('entregado', 'Entregado'),
        ('inactivo', 'Inactivo'),
    ]
    FACTURACION_CHOICES = [
        ('por_pagar', 'Por pagar'),
        ('pagado', 'Pagado'),
        ('no_aplica', 'No aplica'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='proyectos')
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    url = models.URLField(blank=True, verbose_name="URL del proyecto")
    repo_url = models.URLField(blank=True, verbose_name="URL del repositorio")
    contrato = models.FileField(upload_to='contratos/', blank=True, null=True, verbose_name="Contrato (PDF)")
    proceso = models.CharField(max_length=20, choices=PROCESO_CHOICES, default='activo')
    facturacion_estado = models.CharField(max_length=20, choices=FACTURACION_CHOICES, default='no_aplica')
    facturacion_valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    CATEGORIA_CHOICES = [
        ('actols', 'Actols'),
        ('andres', 'Andrés'),
        ('camilo', 'Camilo'),
    ]
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    completada = models.BooleanField(default=False)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    creada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Enlace(models.Model):
    nombre = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.nombre
