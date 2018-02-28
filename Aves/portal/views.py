from django.shortcuts import render, render_to_response, redirect

from django.http import HttpResponse
from django.http import Http404
# necesario para el AJAX
from django.views.decorators.csrf import csrf_exempt
# Resultado de AJAX en formato JSON
from django.core import serializers
from django.http import JsonResponse

# TIPOS de respesta a VISTAS---
from django.template import RequestContext, loader
# importamos el modelo BD
from portal.models import *

# PAGINACION
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Sirven para enviar en FORMATO JSON
import json
# para generar colores
import random


def mapa_view(request):
    datosblugares = []
    lugares = []
    listalugares = LocalidadesAves.objects.distinct().all()  # 683
    for lugar in listalugares:
        ilugar = lugar.idlocal
        latitud = lugar.latitud
        longitud = lugar.longitud
        ecosistema = lugar.ecosistema
        topomin = lugar.toponim
        altitud = lugar.altitud
        fkpro = ""
        nlugar = ""
        print ilugar
        if ilugar > 683:
            print "No hay relacion"
        else:
            localidad = Localidades.objects.filter(idlocalidad=ilugar).all()[0]
            fkpro = localidad.idpro
            nlugar = localidad.nombre
        # pro = Provincias.objects.filter(idpro=fkpro)
        # nombpro = pro.nombprovincia
        # print pro
        # idp = pro.idpais
        nombpro = ""
        idp = 1
        conteo = LocalidadesAves.objects.filter(
            idlocal=localidad.idlocalidad).count()

        def r(): return random.randint(0, 255)
        colores = ('#%02X%02X%02X' % (r(), r(), r()))
        datosblugares.append((colores, idp, nombpro, conteo))
        lugares.append((idp, nombpro, ilugar, nlugar, latitud,
                        longitud, ecosistema, topomin, altitud))

    # provincias = Provincias.objects.all()
    # for pro in provincias:
    #     idpro = pro.idpro
    #     print idpro
    #     nombpro = pro.nombprovincia
    #     idp = pro.idpais
    #     localidad = ""
    #     if idpro != 15:
    #         localidad = Localidades.objects.filter(idpro=idpro).all()[0]
    #         conteo = LocalidadesAves.objects.filter(
    #         idlocal=localidad.idlocalidad).count()
    #         nlugar = localidad.nombre
    #         ilugar = localidad.idlocalidad
    #     lugar = LocalidadesAves.objects.filter(idlocal=ilugar).all()[0]
    #     latitud = lugar.latitud
    #     longitud = lugar.longitud
    #     ecosistema = lugar.ecosistema
    #     topomin = lugar.toponim
    #     altitud = lugar.altitud

    #     def r(): return random.randint(0, 255)
    #     colores = ('#%02X%02X%02X' % (r(), r(), r()))
    #     datosblugares.append((colores, idp, nombpro, conteo))
    #     lugares.append((idp, nombpro, ilugar, nlugar, latitud,
    #                     longitud, ecosistema, topomin, altitud))

    dicmapa = {
        'datosblugares': datosblugares,
        'lugares': lugares,
    }
    return render(request, 'mapa.html', dicmapa)


"""
def autores(request):
    listaA = []
    estudios = Autores.objects.all()
    tuplas = ()
    for x in estudios:
        iautor = x.idautor
        autor = x.autor
        contador = Autores.objects.filter(
            autoresaves__idautor=iautor).all().count()
        ave = Aves.objects.filter(autoresaves__idautor=iautor).all()[0]
        ave = ave.namebird
        tuplas = (autor, contador, ave)
        listaA.append(tuplas)
    return render(request, 'autores.html')
"""


def proconteo(request):
    contEc = []
    contPe = []
    lisp = []
    dicConteo = {}
    paises = Paises.objects.all()
    paisymas = []
    #----------------------Empiezo yo--------------_#
    listapais = []
    listaprov = []
    listalocalidades = []
    acum = ''
    for pais in paises:
        provincias = Provincias.objects.filter(idpais=pais.pk)
        for provinca in provincias:
            lugares = Localidades.objects.filter(idpro=provinca.pk)
            for x in lugares:
                nombre = x.nombre
                nombre = unicode(nombre)
                cont = LocalidadesAves.objects.filter(idlocalidad=x.pk).count()
                cont = str(cont)
                acum = acum + '{' +nombre + ',' + cont +'},' 
                listalocalidades.append((nombre, cont))
            listaprov.append((provinca, listalocalidades))
        listapais.append((pais, listaprov))
    print acum
    #----------------------Termino yo--------------_#



    # para el conteo por provinca
    for pais in paises:
        idp = pais.idpais
        npais = pais.nombpais
        provincias = Provincias.objects.filter(idpais=idp)
        for marcador in provincias:
            idpro = marcador.idpro
            nombpro = marcador.nombprovincia
            lisp.append((idpro, nombpro))
            listalugares = ""
            caves = 0
            if 'EC' in idp:
                listalugares = Localidades.objects.filter(idpro=idpro)
                for x in listalugares:
                    ilugar = x.idlocalidad
                    conteo = LocalidadesAves.objects.filter(
                        idlocal=ilugar).count()
                    localidades = LocalidadesAves.objects.filter(
                        idlocal=ilugar)
                    caves += conteo
                contEc.append((idpro, nombpro, caves))
                # print "pais\t",pais
            else:
                listalugares = Localidades.objects.filter(idpro=idpro)
                for x in listalugares:
                    ilugar = x.idlocalidad
                    conteo = LocalidadesAves.objects.filter(
                        idlocal=ilugar).count()
                    localidades = LocalidadesAves.objects.filter(
                        idlocal=ilugar)
                    caves += conteo
                contPe.append((idpro, nombpro, caves))

    # Para el conteo por localidad
    for pais in paises:
        idp = pais.idpais
        provincias = Provincias.objects.filter(idpais=idp)
        for provincia in provincias:
            idpro = provincia.idpro
            nombpro = provincia.nombprovincia
            listalugares = Localidades.objects.filter(idpro=idpro)
            caves = 0
            for x in listalugares:
                ilugar = x.idlocalidad
                conteo = LocalidadesAves.objects.filter(idlocal=ilugar).count()
                caves += conteo
                paisymas.append((pais, provincia, x, caves))

    lisp = contEc + contPe
    dicConteo['lisp'] = lisp
    dicConteo['contEc'] = contEc
    dicConteo['contPe'] = contPe
    dicConteo['paisymas'] = paisymas
    dicConteo['listapais'] = listapais
    return render(request, "conteo.html", dicConteo)


def amenazas_view(request):
    datosamenaza = []
    dicamenazas = {}
    if request.method == "POST" and 'amenazas' in request.POST:
        datosamenaza = []
        print "-->" + request.POST["tipoamenaza"]
        idamenaza = request.POST["tipoamenaza"]
        idamenaza = int(idamenaza)
        detalle = ""
        if idamenaza > 0:
            detalle = Aves.objects.filter(amenaza=idamenaza).count()
            detalleave = Aves.objects.filter(amenaza=idamenaza)[:detalle]
        else:
            idna = Amenazas.objects.filter(clasificacion='N/A')
            detalle = Aves.objects.exclude(amenaza=idamenaza).count()
            detalleave = Aves.objects.filter(amenaza=idamenaza)[:detalle]
        dicamenazas['avesbajoamenaza'] = detalle
        dicamenazas['detalleave'] = detalleave

    listamenazas = Amenazas.objects.all()
    for amenaza in listamenazas:
        idamenaza = amenaza.idamenaza
        nombamenza = amenaza.clasificacion
        numAvesAmenazadas = Aves.objects.filter(amenaza=idamenaza).count()
        datosamenaza.append((idamenaza, nombamenza, numAvesAmenazadas))

    dicamenazas['listamenazas'] = listamenazas
    dicamenazas['datosamenaza'] = datosamenaza

    return render(request, "amenazas.html", dicamenazas)


def clasificacion(request):
    datosclasifica = []
    categoria = []
    datospromedio = []
    promedio = 0
    suma = 0
    c = 0
    listclasificacion = []
    listafamilias = Familias.objects.all()[:10]
    for x in listafamilias:
        c += 1
        ifamilia = x.idfamilia
        familia = x.nombfamilia
        print "........." + familia
        contEspecie = Especies.objects.filter(idfamilia=ifamilia).count()
        suma += contEspecie
        listaespecies = Especies.objects.filter(idfamilia=ifamilia).all()[0]
        especie = listaespecies.nombespecie
        categoria.append(familia)
        datosclasifica.append((especie, contEspecie))
        promedio = suma / c
    datospromedio.append(promedio)

    listordenes = Denominacion.objects.all()
    for orden in listordenes:
        iorden = orden.iddenominacion
        listafamilias = Familias.objects.filter(iddenominacion= iorden)
        contFamilias = Familias.objects.filter(iddenominacion= iorden).count()
        for familia in listafamilias:
            ifamilia = familia.idfamilia
            listaespecies = Especies.objects.filter(idfamilia= ifamilia)
            contEspecie = Especies.objects.filter(idfamilia= ifamilia).count()

    dicinfo = {
        'datosclasifica': datosclasifica,
        'categoria': categoria,
    }

    #, context_instance=RequestContext(request)
    return render(request, "clasificacion.html", dicinfo)


def index(request):
    totales = []
    mejoresautores = []
    numAves = Aves.objects.all().count()
    numAmenazas = Amenazas.objects.all().count()
    numOrden = Denominacion.objects.all().count()
    numFamilias = Familias.objects.all().count()
    numEspecies = Especies.objects.all().count()
    numAutores = Autores.objects.all().count()
    listautores = Autores.objects.all()
    for autor in listautores:
        iautor = autor.idautor
        nombre = autor.autor
        contautor = AutoresAves.objects.filter(idautor=iautor).count()
        # if contautor > 10:
        mejoresautores.append((nombre, contautor))
    totales.append(("Aves", numAves))
    totales.append(("Amenazas", numAmenazas))
    totales.append(("Orden", numOrden))
    totales.append(("Familias", numFamilias))
    totales.append(("Especies", numEspecies))
    totales.append(("Autores", numAutores))

    dicinfo = {
        'totales': totales,
        'listautores': listautores,
        'mejoresautores': mejoresautores,
    }

    #, context_instance=RequestContext(request)
    return render(request, "index.html", dicinfo)


def fotos(request):
    urlfotos = Urls.objects.all()[:20]
    # Muestra 12 fotos por pagina (multiplos de 4 por el responsive)
    paginator = Paginator(urlfotos, 8)
    page = request.GET.get('page')
    try:
        imagenes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        imagenes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        imagenes = paginator.page(paginator.num_pages)

    cntxtFoto = {
        'paginas': imagenes
    }
    return render(request, "galeria.html", cntxtFoto)


# AJAX
@csrf_exempt
def ajax_familia(request):
    if request.is_ajax() == True:
        print "entra ajax"
        req = {}
        idorde = request.POST.getlist('idorden')[0]
        print "idorden:\t", idorde
        listafamilias = Familias.objects.filter(iddenominacion=idorde).all()
        print "-->", listafamilias
        filtrofamilias = json.dumps(
            [{'idfamilia': f.idfamilia, 'nombfamilia': f.nombfamilia, 'idorden': f.iddenominacion} for f in listafamilias])
        req['mensaje'] = 'Correcto... datos familia'
        req['filtrofamilias'] = filtrofamilias
        print "fin_entra ajax"
        return JsonResponse(req, safe=False)


# return render_to_response('index.html', context_instance=RequestContext(request))
"""
#AKI ver como s implementan los SELECTs para lo d LUGAREs#


@csrf_exempt
def ajaxlocalidades(request):
    if request.is_ajax() == True:
        req = {}
        idlugar = request.POST.getlist('idlugar')[0]
        lugares = Localidades.objects.filter(
            provincias__idpro__idlocalidad=idlugar).all()
        lugares = json.dumps([
            {'idlugar': l.idlocalidad,
            'nombre': l.nombre,
            'idpro': l.idpro}
            for l in lugares])
        req['lugares'] = lugares
        return JsonResponse(req, safe=False)


@csrf_exempt
def ajax_lugares(request):
    if request.is_ajax() == True:
        req = {}
        idpr = request.POST.getlist('idpro')[0]
        # el lugar|localidad se filtra por la provincia (, idlocalidad=lugar)
        listalugares = Localidades.objects.filter(idpro=idpr)
        listalugares = json.dumps([
            {'idlocalidad': l.idlocalidad,
             'nombre': l.nombre,
             'idpro': l.idpro} for l in listalugares])

        req['mensaje'] = 'Correcto.... buscando ajax'
        req['listalugares'] = listalugares
        return JsonResponse(req, safe=False)
"""
