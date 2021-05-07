from django.db.models import Sum
from django.db.models import F
from Monster_Hunter.models.Others import Palico_lent
from Monster_Hunter.models.Palico import Palico


def Solidary_palico_query():

    palico = Palico_lent.objects.values('palico_id').annotate(q=Sum(F('return_date')-F('delivery_date'))).order_by('-q')[:1]

    chosen_p = palico.values_list('palico_id', flat=True)
    result = list(chosen_p)

    return Palico.objects.filter(palico_id=result[0])
