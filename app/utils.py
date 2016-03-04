import json
import os
from .models import *
from app import from_base64_to_picture
from tropicollage import settings
from django.utils.text import slugify

def handle_uploaded_file(cad):
	data = json.loads(cad)
	casa = Casa()
	casa.nombre = data['Name']
	casa.direccion_postal = data['Address']
	casa.municipio  = data['Town']
	casa.provincia = data['City']
	casa.pais = data['Country']
	from_base64_to_picture.to_picture(str(data['MainPicture']).encode('utf-8'), os.path.join(settings.MEDIA_ROOT, 'imagenes/'+data['Name']+'.jpg'))
	casa.foto_principal = 'imagenes/'+data['Name']+'.jpg'
	casa.mensaje_promocional = data['PromoMessage']
	casa.cant_habitaciones = data['RoomsCount']
	casa.ninos_enCasa = data['Kids']
	casa.mascotas_enCasa = data['Pets']
	casa.desayuno = data['Breakfast']
	casa.meriendas = data['Snacks']
	casa.cena = data['Dinner']
	casa.bebidas_bar = data['Drinks']
	from_base64_to_picture.to_picture(str(data['OwnerPicture']).encode('utf-8'), os.path.join(settings.MEDIA_ROOT, 'imagenes/'+data['Name']+'_'+data['OwnerName']+'.jpg'))
	casa.foto_dueno = 'imagenes/' + data['Name']+'_'+data['OwnerName']+'.jpg'
	casa.nombre_dueno = data['OwnerName']
	casa.correo = data['Email']
	casa.telf = data['PhoneNumber']
	casa.celular = data['CellPhone']
	casa.ingles = data['Ingles']
	casa.frances = data['Frances']
	casa.aleman = data['Aleman']
	casa.italiano = data['Italiano']
	casa.portugues = data['Portugues']
	casa.otra_informacion = data['AdditionalInfo']
	casa.telefono = data['Phone']
	casa.garaje = data['Garage']
	casa.piscina = data['Pool']
	casa.jacuzzi = data['Jacuzzi']
	casa.gimnasio = data['Gym']
	casa.internet = data['Internet']
	casa.parqueo = data['Parking']
	casa.ciudad = data['Urban']
	casa.campo = data['Rural']
	casa.playa = data['Beach']
	casa.polo_turistico = data['PoloTuristico']
	casa.cuidador_Nino = data['BabySitter']
	casa.clase_baile = data['DanceTeaching']
	casa.lavanderia = data['Laundry']
	casa.comida_vegetariana = data['VegetarianDinner']
	casa.pantry = data['ClientUsageKitchen']
	casa.permiten_ninos = data['ChildAllowed']
	casa.permiten_mascotas = data['PetsAllowed']
	casa.slug = slugify(casa.nombre)
	gallery_set = data['Gallery']
	gallery = Gallery()
	gallery.title = gallery_set['GalleryName']
	gallery.save()
	count = 0
	for item in gallery_set['Images']:
		count = count + 1
		imagen = Image()
		from_base64_to_picture.to_picture(str(item).encode('utf-8'), os.path.join(settings.MEDIA_ROOT, 'imagenes/'+gallery.title+'_'+str(count)+'.jpg'))
		imagen.gallery = gallery
		imagen.file.name = 'imagenes/'+gallery.title+'_'+str(count)+'.jpg'
		imagen.save()
	casa.gallery = gallery
	casa.superhost = False
	casa.save()
	room_set = data['Rooms']

	menor_precio_baja = 99999999
	menor_precio_alta = 99999999

	for item in room_set:

		habitacion = Habitacion()
		habitacion.primer_piso = item['FirstFloor']
		habitacion.segundo_piso = item['SecondFloor']
		habitacion.superior = item['Superior']
		habitacion.precio_baja = item['PrecioPorNocheTemporadaBaja']
		habitacion.precio_alta = item['PrecioPorNocheTemporadaAlta']

		if habitacion.precio_alta < menor_precio_alta:
			menor_precio_alta = habitacion.precio_alta

		if habitacion.precio_baja < menor_precio_baja:
			menor_precio_baja = habitacion.precio_baja

		habitacion.cama_personal = item['CamaPersonal']
		habitacion.cama_doble = item['CamaDoble']
		habitacion.aire_acondicionado = item['AireAcondicionado']
		habitacion.agua_caliente = item['AguaCaliente']
		habitacion.secador = item['Secador']
		habitacion.minibar = item['Minibar']
		habitacion.cuna = item['Cuna']
		habitacion.corriente_220 = item['Corriente220']
		habitacion.corriente_110 = item['Corriente110']
		habitacion.balcon = item['Balcon']
		habitacion.terraza = item['Terraza']
		habitacion.bano_privado = item['BanoPrivado']
		habitacion.TV = item['TV']
		habitacion.ventilador = item['Ventilador']
		habitacion.caja_fuerte = item['CajaFuerte']
		habitacion.casa = casa
		habitacion.save()

		if habitacion.agua_caliente:
			casa.filter_agua_caliente = habitacion.agua_caliente

		if habitacion.bano_privado:
			casa.filter_bano_privado = habitacion.bano_privado

		if habitacion.caja_fuerte:
			casa.filter_caja_fuerte = habitacion.caja_fuerte

	casa.precio_baja = menor_precio_baja
	casa.precio_alta = menor_precio_alta
	casa.save()

