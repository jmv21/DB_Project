from django.db.models import Sum,Q, Count, Max, Case, When, F

from django.template import loader

from django.http import HttpResponse, Http404

from Monster_Hunter.models.Others import Inventory, Reward_object, Recipes
from Monster_Hunter.models.Object import Object, Armor, Merchantable_Object, Collected_object, Weapon
from Monster_Hunter.models.Palico import Palico, Palico_lent
from Monster_Hunter.models.Hunter import Hunter
from Monster_Hunter.models.Monster import Monster
from Monster_Hunter.models.Element import Element, Elemental_defense


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
    monsters = Monster.objects.all()
    template = loader.get_template('Views_test/monsters.html')
    context = {
        'monsters': monsters
    }
    return HttpResponse(template.render(context, request))


def inventory(request, number):
    inventory = Inventory.objects.all()
    p_inventory = inventory.filter(hunter_id=number)
    hunter = Hunter.objects.get(id=number)
    ids = list(p_inventory.values_list("object_id", flat=True))
    objects = Object.objects.filter(id__in=ids)
    template = loader.get_template('Views_test/inventory.html')
    r_objects = []
    for i in range(len(ids)):
        r_objects.append((objects[i], p_inventory[i]))
    context = {
        'inventory': r_objects,
        'hunter': hunter
    }
    return HttpResponse(template.render(context, request))


def objects(request):
    objects = Object.objects.all()
    template = loader.get_template('Views_test/objects.html')
    context = {
        'objects': objects
    }
    return HttpResponse(template.render(context, request))


def object_details(request, obj_id):
    objects = Object.objects.all()
    object = objects.get(id=obj_id)
    type = 'Plain_object'
    object_info = []
    object_resistance = []
    if (Reward_object.objects.filter(object_id=obj_id).exists()):
        type = 'Reward_object'
        object_info = Reward_object.objects.get(object_id=obj_id)
    elif (Armor.objects.filter(object_id=obj_id).exists()):
        type = 'Armor'
        object_info = Armor.objects.get(object_id=obj_id)
        object_resistance = Elemental_defense.objects.filter(armor=Armor.objects.get(object_id=obj_id).id)
        if(object_resistance.count() > 0):
            object_resistance = object_resistance.get(armor=Armor.objects.get(object_id=obj_id).id)
        else:
            object_resistance = None
    elif (Weapon.objects.filter(object_id=obj_id).exists()):
        type = 'Weapon'
        object_info = Weapon.objects.get(object_id=obj_id)
    elif (Collected_object.objects.filter(object_id=obj_id).exists()):
        type = 'Collected_object'
        object_info = Collected_object.objects.get(object_id=obj_id)
    elif (Merchantable_Object.objects.filter(object_id=obj_id).exists()):
        type = 'Merchantable_Object'
        object_info = Merchantable_Object.objects.get(object_id=obj_id)
    # elif (Reward_object.objects.get(object_id=id_obj).quantity > 0):
    template = loader.get_template('Views_test/object_detail.html')
    context = {
        'object': object,
        'object_info': object_info,
        type: type,
        'type': type,
        'object_resistance': object_resistance
    }
    return HttpResponse(template.render(context, request))


def elements(request):
    elements = Element.objects.all()
    template = loader.get_template('Views_test/elements.html')
    context = {
        'elements': elements
    }
    return HttpResponse(template.render(context, request))


def home(request):
    template = loader.get_template('Views_test/home.html')
    return HttpResponse(template.render(None, request))


def elemental_resistant_armorset(request, elements):
    template = loader.get_template('Views_test/armor_set.html')
    line = ' '.join(elements.split())
    tokens = line.split(',')
    elem = Element.objects.all()
    # get the elements list to the armors be resistant to
    list_elem = list(elem.filter(name__in=tokens).values_list("id", flat=True))
    elem_def = Elemental_defense.objects.all()
    # get the armors resistant to at least one element listed
    armor = Armor.objects.all()
    # get the armors
    list_armor = list(armor.values_list("object", flat=True))
    inv = Inventory.objects.all()
    # get the armors that are actually, in the inventory of some hunter
    armor_inv = inv.filter(object__in=list_armor)
    # get the hunters that own those armors
    list_hunters = list(armor_inv.values_list("hunter", flat=True).distinct())
    result = []
    armorsets = []
    for i in list_hunters:
        aux = list(armor_inv.filter(hunter=i).values_list("object", flat=True))
        armorset = armor.filter(id__in=aux)
        armorset_resistance = list(
            elem_def.filter(armor__in=aux).filter(element__in=list_elem).values_list("element").distinct())
        pieces = armorset.values_list("armor_type", flat=True).distinct()
        if (len(armorset) >= 5 and len(armorset_resistance) >= len(list_elem)):
            result.append(i)
    hunters_owners = Hunter.objects.all().filter(id__in=result)
    context = {
        'hunters': hunters_owners,
        'armorsets': armorset
    }
    return HttpResponse(template.render(context, request))


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
    quantity_list = list(query1.values_list('q', flat=True))[:min(number, length)]
    r_objects = []
    for i in range(len(quantity_list)):
        r_objects.append((result[i], quantity_list[i]))
    context = {
        'rarest_items': r_objects
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


def most_popular_monster_equipment(request):
    armor_or_weapon = Q(object__armor__armor_type__isnull=False) | Q(object__weapon__damage__isnull=False)

    objects_in_inventory = Inventory.objects.values('object_id').filter(armor_or_weapon).values_list('object_id')
    popular_monster = Recipes.objects.values('object2__reward_object__monster_id').filter(
        object1_id__in=objects_in_inventory).annotate(q=Count('object2__reward_object__monster_id')).order_by(
        '-q').values_list('object2__reward_object__monster_id', flat=True)[:1]


    monster = Monster.objects.filter(id__in=popular_monster)

    template = loader.get_template('Views_test/most_used_monster.html')
    context = {
        'monster': monster
    }
    return HttpResponse(template.render(context, request))

