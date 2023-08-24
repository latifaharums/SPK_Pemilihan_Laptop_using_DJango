from django.shortcuts import render, redirect
from django.db.models import Max, Min, F, Value, FloatField
from django.db.models.functions import Round
from django.db.models.expressions import ExpressionWrapper
from alternatif.models import alternatif, normalisasi
from django.db.models.functions import Cast
from alternatif.table import formtabel
from django.db import models
from decimal import Decimal, ROUND_DOWN

def index(request):
    form_input = alternatif.objects.all()
    minc1 = alternatif.objects.aggregate(Min('c1')).get('c1__min')
    maxc2 = alternatif.objects.aggregate(Max('c2')).get('c2__max')
    maxc3 = alternatif.objects.aggregate(Max('c3')).get('c3__max')
    maxc4 = alternatif.objects.aggregate(Max('c4')).get('c4__max')
    maxc5 = alternatif.objects.aggregate(Max('c5')).get('c5__max')
    maxc6 = alternatif.objects.aggregate(Max('c6')).get('c6__max')
    maxc7 = alternatif.objects.aggregate(Max('c7')).get('c7__max')

    c1norm = [round(minc1 / c1_val, 4) for c1_val in alternatif.objects.values_list('c1', flat=True)]
    c2norm = [round(c2_val / maxc2, 4) for c2_val in alternatif.objects.values_list('c2', flat=True)]
    c3norm = [round(c3_val / maxc3, 4) for c3_val in alternatif.objects.values_list('c3', flat=True)]
    c4norm = [round(c4_val / maxc4, 4) for c4_val in alternatif.objects.values_list('c4', flat=True)]
    c5norm = [round(c5_val / maxc5, 4) for c5_val in alternatif.objects.values_list('c5', flat=True)]
    c6norm = [round(c6_val / maxc6, 4) for c6_val in alternatif.objects.values_list('c6', flat=True)]
    c7norm = [round(c7_val / maxc7, 4) for c7_val in alternatif.objects.values_list('c7', flat=True)]

    c1normbobot = [Decimal(minc1 * 0.1612903226 / c1_val).quantize(Decimal('0.0001')) for c1_val in alternatif.objects.values_list('c1', flat=True)]
    c2normbobot = [Decimal(c2_val / maxc2 * 0.1612903226).quantize(Decimal('0.0001')) for c2_val in alternatif.objects.values_list('c2', flat=True)]
    c3normbobot = [Decimal(c3_val / maxc3 * 0.09677419355).quantize(Decimal('0.0001')) for c3_val in alternatif.objects.values_list('c3', flat=True)]
    c4normbobot = [Decimal(c4_val / maxc4 * 0.129032258064516).quantize(Decimal('0.0001')) for c4_val in alternatif.objects.values_list('c4', flat=True)]
    c5normbobot = [Decimal(c5_val / maxc5 * 0.129032258064516).quantize(Decimal('0.0001')) for c5_val in alternatif.objects.values_list('c5', flat=True)]
    c6normbobot = [Decimal(c6_val / maxc6 * 0.1612903226).quantize(Decimal('0.0001')) for c6_val in alternatif.objects.values_list('c6', flat=True)]
    c7normbobot = [Decimal(c7_val / maxc7 * 0.1612903226).quantize(Decimal('0.0001')) for c7_val in alternatif.objects.values_list('c7', flat=True)]

    result = alternatif.objects.all().annotate(
        prod=Round(
            minc1 * 0.1612903226 / F('c1') +
            F('c2') / maxc2 * 0.1612903226 +
            F('c3') / maxc3 * 0.09677419355 +
            F('c4') / maxc4 * 0.129032258064516 +
            F('c5') / maxc5 * 0.129032258064516 +
            F('c6') / maxc6 * 0.1612903226 +
            F('c7') / maxc7 * 0.1612903226,
        )
    )

    result2 = alternatif.objects.all().values_list(
            minc1 * 0.1612903226 / F('c1') +
            F('c2') / maxc2 * 0.1612903226 +
            F('c3') / maxc3 * 0.09677419355 +
            F('c4') / maxc4 * 0.129032258064516 +
            F('c5') / maxc5 * 0.129032258064516 +
            F('c6') / maxc6 * 0.1612903226 +
            F('c7') / maxc7 * 0.1612903226,
    )

    context = {
        'title':'PERHITUNGAN',
        'table':form_input,
        'normc1':c1norm,
        'normc2':c2norm,
        'normc3':c3norm,
        'normc4':c4norm,
        'normc5':c5norm,
        'normc6':c6norm,
        'normc7':c7norm,

        'botc1':c1normbobot,
        'botc2':c2normbobot,
        'botc3':c3normbobot,
        'botc4':c4normbobot,
        'botc5':c5normbobot,
        'botc6':c6normbobot,
        'botc7':c7normbobot,
        'hasil':result,
        'hasil2':result2,
   
    }
    return render(request, 'perhitungan/index.html', context)
def hapus(request, kode):
    tables = alternatif.objects.filter(kodealternatif=kode).delete()
    return redirect('perhitungan:index')
def edit(request, kode):
    editakun = alternatif.objects.get(kodealternatif=kode)
    data={
        'kodealternatif':editakun.kodealternatif,
        'namaalternatif':editakun.namaalternatif,
        'c1':editakun.c1,
        'c2':editakun.c2,
        'c3':editakun.c3,
        'c4':editakun.c4,
        'c5':editakun.c5,
        'c6':editakun.c6,
        'c7':editakun.c7,
    }
    form_input = formtabel(request.POST or None, initial=data, instance=editakun)
    if request.method == "POST":
        if form_input.is_valid():
            form_input.save()
            return redirect('perhitungan:index')
    context={
        'title':'AKUN|UPDATE',
        'table':form_input,
        'tombol':'Edit',
    }
    return render(request, 'alternatif/index.html', context)
