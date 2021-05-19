from django.db.models import Sum
from django.db.models import Case, When
from django.db.models import F

from django.template import loader

from django.http import HttpResponse
from django.http import Http404

from Monster_Hunter.models.Others import Inventory
from Monster_Hunter.models.Object import Object
from Monster_Hunter.models.Palico import Palico
from Monster_Hunter.models.Palico import Palico_lent
from Monster_Hunter.models.Hunter import Hunter


# Create your views here.

def rarest_objects(request, number):
    if number < 0:
        raise Http404("Number must be nonnegative")
    template = loader.get_template('Views_test/rarest_objects.html')
    inv = Inventory.objects.all()
    query1 = inv.values('object_id').annotate(q=Sum('quantity')). \
        order_by('q')  # hacemos un query para determinar la cantidad de objetos de manera global
    length = query1.count()
    object_ids = list(query1.values_list('object_id', flat=True).distinct())[:min(number, length)]
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(object_ids)])
    result = Object.objects.filter(id__in=object_ids).order_by(preserved)
    quantity_list = list(query1.values_list('q', flat=True).distinct())
    context = {
        'rarest_items': result,
        'quantity_items': quantity_list
    }
    return HttpResponse(template.render(context, request))


def solidariest_palico(request):
    palico = Palico_lent.objects.values('palico_id').annotate(q=Sum(F('return_date') - F('delivery_date'))).order_by(
        '-q')[:1]
    template = loader.get_template('Views_test/solidariest_palico.html')
    chosen_p = list(palico.values_list('palico_id', flat=True))
    result = Palico.objects.filter(id__in=chosen_p)
    context = {
        'solidariest_palico': result
    }
    return HttpResponse(template.render(context, request))


def hunters(request):
    hunters = Hunter.objects.all()
    template = loader.get_template('Views_test/hunters.html')
    context = {
        'hunters': hunters
    }
    return HttpResponse(template.render(context, request))


def palicos(request):
    palicos = Palico.objects.all()
    template = loader.get_template('Views_test/palicos.html')
    context = {
        'palicos': palicos
    }
    return HttpResponse(template.render(context, request))


def monsters(request):
    monsters = Palico.objects.all()
    template = loader.get_template('Views_test/monsters.html')
    context = {
        'monsters': monsters
    }
    return HttpResponse(template.render(context, request))


def objects(request):
    objects = Object.objects.all()
    template = loader.get_template('Views_test/objects.html')
    context = {
        'objects': objects
    }
    return HttpResponse(template.render(context, request))


def home(request):
    template = loader.get_template('Views_test/home.html')
    return HttpResponse(template.render(None, request))
