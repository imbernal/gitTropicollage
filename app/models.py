from django.db import models
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField

# Create your models here.

class Gallery(models.Model):
    class Meta:
        verbose_name_plural = 'Galleries'

    title = models.CharField('Title', max_length=20)

    def __str__(self):
        return self.title


class Image(models.Model):
    file = VersatileImageField('Image', upload_to='imagenes/')
    gallery = models.ForeignKey('Gallery', related_name='images', blank=True, null=True)

    def __str__(self):
        return self.filename

    @property
    def filename(self):
        return self.file.name.rsplit('/')[-1]


CHOICES = (
    (None, "All"),
    (True, "Yes"),
)

class Casa(models.Model):
    nombre = models.CharField(max_length=255, default="")
    direccion_postal = models.CharField(max_length=255, default="")
    municipio = models.CharField(max_length=255, default="")
    provincia = models.CharField(max_length=255, default="")
    pais = models.CharField(max_length=255, default="")
    polo_turistico = models.CharField(max_length=255, default="")
    cant_habitaciones = models.PositiveIntegerField()
    ninos_enCasa = models.BooleanField(default=False)
    mascotas_enCasa = models.BooleanField(default=False)
    mensaje_promocional = models.TextField(max_length=600)
    foto_principal = VersatileImageField('Image', upload_to='imagenes')
    desayuno = models.BooleanField(default=False)
    meriendas = models.BooleanField(default=False)
    cena = models.BooleanField(default=False)
    bebidas_bar = models.BooleanField(default=False)
    slug = models.CharField(max_length=255, default="")
        
    #servicios
    telefono = models.NullBooleanField(choices = CHOICES)
    garaje = models.BooleanField(choices = CHOICES)
    jacuzzi = models.BooleanField(choices = CHOICES)
    piscina = models.BooleanField(choices = CHOICES)
    cuidador_Nino = models.BooleanField(choices = CHOICES)
    gimnasio = models.BooleanField(choices = CHOICES)
    internet = models.BooleanField(choices = CHOICES)
    parqueo = models.BooleanField(choices = CHOICES)
    clase_baile = models.BooleanField(choices = CHOICES)
    lavanderia = models.BooleanField(choices = CHOICES)
    comida_vegetariana = models.BooleanField(choices = CHOICES)
    pantry = models.BooleanField(choices = CHOICES)

    #datos de contacto

    nombre_dueno = models.CharField(max_length=255)
    correo = models.CharField(max_length=255, default="")
    telf = models.CharField(max_length=255)
    celular = models.CharField(max_length=255)
    foto_dueno = VersatileImageField('Image', upload_to='imagenes')

    
    superhost = models.BooleanField(choices = CHOICES)
    categoria = models.PositiveIntegerField(null=True, blank=True)

    gallery = models.OneToOneField(Gallery)

    #idiomas
    ingles = models.BooleanField(choices = CHOICES)
    frances = models.BooleanField(choices = CHOICES)
    aleman = models.BooleanField(choices = CHOICES)
    italiano = models.BooleanField(choices = CHOICES)
    portugues = models.BooleanField(choices = CHOICES)

    otra_informacion = models.TextField(max_length=600)

    permiten_ninos = models.BooleanField(choices = CHOICES)
    permiten_mascotas = models.BooleanField(choices = CHOICES)

    #ubicacion
    ciudad = models.BooleanField(choices = CHOICES)
    campo  = models.BooleanField(choices = CHOICES)
    playa = models.BooleanField(choices = CHOICES)

    # temporadas
    tempBajaIni = models.DateField(null = True)
    tempBajaFin = models.DateField(null = True)
    tempAltaIni = models.DateField(null = True)
    tempAltaFin = models.DateField(null = True)

    precio_alta = models.FloatField(null = True , default = 0)
    precio_baja = models.FloatField(null = True , default = 0)

    #datos para buscar
    filter_agua_caliente = models.BooleanField(choices = CHOICES , default=False)
    filter_bano_privado = models.BooleanField(choices = CHOICES,default=False)
    filter_caja_fuerte = models.BooleanField(choices = CHOICES,default=False)

    def __str__(self):
        return self.nombre

    def full_address(self):
        return self.direccion_postal + " 20100 " + self.municipio

class Habitacion(models.Model):

    precio_alta = models.FloatField(default=0)
    precio_baja = models.FloatField(default=0)

    cama_personal = models.PositiveIntegerField(default = 0)
    cama_doble = models.PositiveIntegerField(default = 0)

    primer_piso = models.BooleanField(choices = CHOICES)
    segundo_piso = models.BooleanField(choices = CHOICES)
    superior = models.BooleanField(choices = CHOICES)


    caja_fuerte = models.BooleanField(choices = CHOICES)
    ventilador = models.BooleanField(choices = CHOICES)
    aire_acondicionado = models.BooleanField(choices = CHOICES)
    agua_caliente = models.BooleanField(choices = CHOICES)
    secador = models.BooleanField(choices = CHOICES)
    minibar = models.BooleanField(choices = CHOICES)
    corriente_110 = models.BooleanField(choices = CHOICES)
    corriente_220 = models.BooleanField(choices = CHOICES)
    balcon = models.BooleanField(choices = CHOICES)
    terraza = models.BooleanField(choices = CHOICES)
    bano_privado = models.BooleanField(choices = CHOICES)
    TV = models.BooleanField(choices = CHOICES)

    casa = models.ForeignKey(Casa)

class Reservacion(models.Model):
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    phone_nombre = models.IntegerField(default=0)
    country = models.CharField(max_length=50, default="")
    city_town = models.CharField(max_length=50 , default="")
    cant_habitacion = models.IntegerField(default=0)
    hab_simples = models.CharField(max_length=50, default="")
    hab_dobles = models.CharField(max_length=50, default="")
    hab_triples = models.CharField(max_length=50, default="")
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()
    forma_llegada = models.CharField(max_length=50, default="")
    hora_estimada = models.CharField(max_length=255, default=None)
    comment = models.TextField(max_length=600, default="")
    casa = models.ForeignKey(Casa)



class FeedBack(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    ip_address = models.GenericIPAddressField(default=None)
    pub_date = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=600)
    casa = models.ForeignKey(Casa)

    def __str__(self):
        return self.full_name + '\' comment' 
