import datetime
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext

from django.http.response import HttpResponse, JsonResponse, HttpResponseRedirect

from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib import messages
from django.core.mail import send_mail
from app.filter import *


from .forms import UploadFileForm
from .utils import handle_uploaded_file


# Create your views here.

def home_page(request):
    casas = Casa.objects.all()[:8]
    feedbacks = FeedBack.objects.all()[:3]
    reservaciones = Reservacion.objects.all()[:5]
    return render(request, 'home_page/index.html', {'feedbacks': feedbacks, 'casas': casas , 'reservaciones':reservaciones})

def homeList(request):

    if request.POST:
        destination = request.POST['destination']
        filter = CasaFilter(request.GET, queryset=Casa.objects.filter(polo_turistico = destination))

    else:
        filter = CasaFilter(request.GET, queryset=Casa.objects.all())

    return render(request, 'casas/index.html', {"filter": filter})


def homeDetails(request, home_id):
    entity = get_object_or_404(Casa, pk=home_id)
    feedbacks = FeedBack.objects.filter(casa=entity).order_by('-pub_date')
    cant_camas_simples = 0
    cant_camas_dobles = 0

    for item in entity.habitacion_set.all():
        cant_camas_simples += item.cama_personal
        cant_camas_dobles += item.cama_doble

    cant_total_personas = 2 * cant_camas_dobles + cant_camas_simples

    pictures_list = get_pictures_from_gallery(entity.gallery)

    return render(request, 'casas/details.html', {'entity': entity,
                                                  'cant_camas_simples': cant_camas_simples,
                                                  'cant_camas_dobles': cant_camas_dobles,
                                                  'cant_total_personas': cant_total_personas,
                                                  'feedbacks': feedbacks,
                                                  'pictures': pictures_list
                                                  },
                  context_instance=RequestContext(request))

def reservar(request, home_id):

    casa = Casa.objects.get(pk = home_id)

    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    wphone = request.POST['wphone']
    country = request.POST['country']
    city = request.POST['city']
    cant_habitaciones = request.POST['cantHabitaciones']
    hab_simple =request.POST['cantSimples']
    hab_doble=request.POST['cantDobles']
    hab_triple =request.POST['cantTriples']
    desde =request.POST['desde']
    hasta =request.POST['hasta']
    transport = request.POST['medioLlegada']
    hora_estimada = request.POST['horaLLegada']
    imformacionCliente = request.POST['imformacionCliente']

    reservacion = Reservacion()
    reservacion.cant_habitacion = cant_habitaciones
    reservacion.casa = casa
    reservacion.city_town = city
    reservacion.comment = imformacionCliente
    reservacion.country = country
    reservacion.email = email
    reservacion.first_name  = fname
    reservacion.last_name = lname
    reservacion.phone_nombre = wphone
    reservacion.hab_simples = hab_simple
    reservacion.hab_dobles  = hab_doble
    reservacion.hab_triples = hab_triple
    reservacion.fecha_ini = desde
    reservacion.fecha_fin = hasta
    reservacion.forma_llegada = transport
    reservacion.hora_estimada = hora_estimada

    reservacion.save()


def fecha_search(request):
    start_date = request.POST['in-date']
    end_date = request.POST['out-date']

    home_list = Casa.objects.all()

    reservaciones = Reservacion.objects.filter(fecha_ini__range=[start_date, end_date],
                                               fecha_fin__range=[start_date, end_date])
    casas_reservadas = []
    for item in reservaciones:
        casas_reservadas.append(item.casa)
    result_list = list_difference(list(home_list), casas_reservadas)

    return render(request, 'casas/index.html', {'entities': result_list})



@login_required(login_url='/admin/login/')
def uploadJson(request):
    form = UploadFileForm()
    return render(request, 'upload/index.html', {'form': form})


def upload(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid:
        handle_uploaded_file(request.FILES['file'].read().decode('utf-8'))
        return HttpResponse("obj")
    else:
        return HttpResponseRedirect('/')



def contact(request):
    username = request.POST['username']
    email = request.POST['email']
    message = request.POST['message']

    send_mail(username, message, email,
              ['imbernal92@nauta.cu'], fail_silently=False)


def register(request):
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid:
            register_form.save()
            return HttpResponseRedirect('/')
    else:
        register_form = UserCreationForm()
    return render_to_response('account/register.html', {'form': register_form},
                              context_instance=RequestContext(request))


def login_action(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            access = authenticate(username=username, password=password)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return HttpResponse('/')
                else:
                    messages.add_message()
            else:
                render_to_response('account/no_user.html', context_instance=RequestContext(request))
    else:
        form = AuthenticationForm()
    return render_to_response('account/login.html', {'form': form}, context_instance=RequestContext(request))


def list_difference(b, a):
    c = list(b)
    for item in a:
        try:
            c.remove(item)
        except ValueError:
            pass  # or maybe you want to keep a values here
    return c


def get_pictures_from_gallery(gallery_param):
    result = []
    pictures = Image.objects.filter(gallery=gallery_param)
    for item in pictures:
        result.append(item.filename)
    return result


@csrf_exempt
def get_pictures_from_home(request):
    home_id = request.POST['home_id']
    entity = Casa.objects.filter(pk=home_id)
    pictures_list = get_pictures_from_gallery(entity.first().gallery)
    return JsonResponse({'pictures_list': pictures_list})

@csrf_exempt
def comment(request):
    full_name = request.POST['full_name']
    email = request.POST['email']
    body = request.POST['body']
    foreign_home = Casa.objects.filter(pk = request.POST['home_id'])
    client_ip = request.META['REMOTE_ADDR']
    comment = FeedBack()
    comment.full_name = full_name
    comment.email = email
    comment.body = body
    comment.ip_address = client_ip
    comment.casa = foreign_home.first()
    comment.save()

    return HttpResponse(200)


from .serializers import *
from rest_framework import viewsets


class CasaViewSet(viewsets.ModelViewSet):
    queryset = Casa.objects.all()
    serializer_class = CasaSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImagesSerializer
