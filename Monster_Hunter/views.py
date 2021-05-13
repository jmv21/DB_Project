from django.db.models import Sum, Q, Count, Max, Case, When, F

from django.template import loader
from math import ceil

from django.http import HttpResponse, Http404

from Monster_Hunter.models.Others import Inventory, Reward_object, Recipes
from Monster_Hunter.models.Object import Object, Armor, Merchantable_Object, Collected_object, Weapon
from Monster_Hunter.models.Palico import Palico, Palico_lent
from Monster_Hunter.models.Hunter import Hunter
from Monster_Hunter.models.Monster import Monster
from Monster_Hunter.models.Element import Element, Elemental_defense, Elemental_use


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
        if (object_resistance.count() > 0):
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
    elem_def = Elemental_defense.objects.filter(element__in=list_elem)

    # get the hunters with at least a piece of armor resistant to at least one element listed
    list_hunters = list(Armor.objects.filter(pk__in=elem_def.values_list('armor', flat=True)).values_list(
        'object__inventory__hunter_id', flat=True).distinct())
    list_armors = list(Armor.objects.values_list('object', flat=True))

    # get the armors
    inv = Inventory.objects.all()
    # get the armors that are actually, in the inventory of some hunter
    armor_inv = inv.filter(object__in=list_armors, hunter__in=list_hunters)

    result = []
    armorsets = []

    for i in list_hunters:
        aux = list(armor_inv.filter(hunter=i).values_list('object__armor', flat=True))
        armorset = Armor.objects.filter(id__in=aux)

        if (armorset.count() < 5):
            continue
        # get the pieces that resist different elements
        armorset_resistance = elem_def.filter(armor__in=aux).filter(element__in=list_elem)

        found = False
        for e in list_elem:
            if (armorset_resistance.filter(element=e).count() == 0):
                found = False
                break
            found = True
        if (not found):
            continue
        pieces = Armor.objects.filter(
            id__in=list(armorset.values("armor_type").distinct()[:5].values_list('id', flat=True)))

        if (len(armorset_resistance) >= len(list_elem)):
            result.append((Hunter.objects.all().get(id=i), pieces))

    context = {
        'result': result,
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
    chosen_p = palico.values_list('palico_id', flat=True)
    result = Palico.objects.filter(id__in=chosen_p)

    context = {
        'result': (result, palico.values('q')[0])

    }

    return HttpResponse(template.render(context, request))


def most_popular_monster_equipment(request):
    armor_or_weapon = Q(object__armor__armor_type__isnull=False) | Q(object__weapon__damage__isnull=False)

    # get all the equipment in the global inventory
    objects_in_inventory = Inventory.objects.values('object_id').filter(armor_or_weapon)
    # get most used monster to make equipment
    popular_monster = objects_in_inventory.values(
        'object__recipes__object2__reward_object__monster_id').annotate(
        q=Count('object__recipes__object2__reward_object__monster_id')).order_by('-q').values_list(
        'object__recipes__object2__reward_object__monster_id', flat=True)[:1]

    monster = Monster.objects.filter(id__in=popular_monster)

    template = loader.get_template('Views_test/most_used_monster.html')
    context = {
        'monster': monster
    }
    return HttpResponse(template.render(context, request))


def resistent_armor(request, monster):
    template = loader.get_template('Views_test/resistent_armor.html')

    sel_elements = Elemental_use.objects.values('element__name').filter(monster=monster).values_list('element__name',
                                                                                                     flat=True)

    filter_query = Q(element_id__name="")

    for element in sel_elements:
        filter_query = filter_query | Q(element_id__name=element)

    helmet = Elemental_defense.objects.values('armor').filter(filter_query, armor__armor_type=1).annotate(
        q=Sum('value') + F('armor__defense')).order_by('-q')[:1]
    helmet2 = Armor.objects.filter(armor_type=1).annotate(q=Max(F('defense'))).order_by('-q')[:1]
    if (helmet.values().count() == 0):
        helmet = list(helmet2.values_list()[0])
    elif (helmet.values().values_list('q', flat=True)[0] < helmet2.values().values_list('q', flat=True)[0]):
        helmet = list(helmet2.values_list()[0])
    else:
        # add some valuable information
        helmet3 = list(helmet.values_list()[0])
        armor = Armor.objects.get(id=helmet.values_list('armor', flat=True))
        helmet3[1] = armor.object_id
        helmet3[2] = armor.armor_type
        helmet = helmet3

    chest = Elemental_defense.objects.values('armor').filter(filter_query, armor__armor_type=2).annotate(
        q=Sum('value') + F('armor__defense')).order_by('-q')[:1]
    chest2 = Armor.objects.filter(armor_type=2).annotate(q=Max(F('defense'))).order_by('-q')[:1]
    if (chest.values().count() == 0):
        chest = list(chest2.values_list()[0])
    elif (chest.values().values_list('q', flat=True)[0] < chest2.values().values_list('q', flat=True)[0]):
        chest = list(chest2.values_list()[0])
    else:
        chest3 = list(chest.values_list()[0])
        armor = Armor.objects.get(id=chest.values_list('armor', flat=True))
        chest3[1] = armor.object_id
        chest3[2] = armor.armor_type
        chest = chest3

    waist = Elemental_defense.objects.values('armor').filter(filter_query, armor__armor_type=3).annotate(
        q=Sum('value') + F('armor__defense')).order_by('-q')[:1]
    waist2 = Armor.objects.filter(armor_type=3).annotate(q=Max(F('defense'))).order_by('-q')[:1]
    if (waist.values().count() == 0):
        waist = list(waist2.values_list()[0])
    elif (waist.values().values_list('q', flat=True)[0] < waist2.values().values_list('q', flat=True)[0]):
        waist = list(waist2.values_list()[0])
    else:
        waist3 = list(waist.values_list()[0])
        armor = Armor.objects.get(id=waist.values_list('armor', flat=True))
        waist3[1] = armor.object_id
        waist3[2] = armor.armor_type
        waist = waist3

    gauntlets = Elemental_defense.objects.values('armor').filter(filter_query, armor__armor_type=4).annotate(
        q=Sum('value') + F('armor__defense')).order_by('-q')[:1]
    gauntlets2 = Armor.objects.filter(armor_type=4).annotate(q=Max(F('defense'))).order_by('-q')[:1]
    if (gauntlets.values().count() == 0):
        gauntlets = list(gauntlets2.values_list()[0])
    elif (gauntlets.values().values_list('q', flat=True)[0] < gauntlets2.values().values_list('q', flat=True)[0]):
        gauntlets = list(gauntlets2.values_list()[0])
    else:
        gauntlets3 = list(gauntlets.values_list()[0])
        armor = Armor.objects.get(id=gauntlets.values_list('armor', flat=True))
        gauntlets3[1] = armor.object_id
        gauntlets3[2] = armor.armor_type
        gauntlets = gauntlets3

    boots = Elemental_defense.objects.values('armor').filter(filter_query, armor__armor_type=5).annotate(
        q=Sum('value') + F('armor__defense')).order_by('-q')[:1]
    boots2 = Armor.objects.filter(armor_type=5).annotate(q=Max(F('defense'))).order_by('-q')[:1]
    if (boots.values().count() == 0):
        boots = list(boots2.values_list()[0])
    elif (boots.values().values_list('q', flat=True)[0] < boots2.values().values_list('q', flat=True)[0]):
        boots = list(boots2.values_list()[0])
    else:
        boots3 = list(boots.values_list()[0])
        armor = Armor.objects.get(id=boots.values_list('armor', flat=True))
        boots3[1] = armor.object_id
        boots3[2] = armor.armor_type
        boots = boots3

    armor_set = [helmet, chest, waist, gauntlets, boots]

    context = {
        'armor_set': armor_set
    }
    return HttpResponse(template.render(context, request))


def monsters_to_kill(request, equipment_id):
    # template = loader.get_template('Views_test/resistent_armor.html')

    # We select the monster who drops the material and the highest value of the amount_needed/amount_rewarded and group by monster_id
    query = Object.objects.filter(id=equipment_id).values('recipes__object2__reward_object__monster_id').annotate(
        q=(1.0 * F('recipes__quantity') / F('recipes__object2__reward_object__quantity')), piece_id=F('recipes__object2')
        , monster_id='recipes__object2__reward_object__monster_id').order_by('q')

    monster_id = list(query.values_list('recipes__object2__reward_object__monster_id', flat=True))

    q = list(query.values_list('q', flat=True))

    object2 = list(query.values_list('recipes__object2', flat=True))

    for i in range(len(object2) - 1):

        if object2[i] == object2[i + 1]:
            object2.pop(i + 1)
            q.pop(i + 1)
            monster_id.pop(i + 1)

    actual_m = {}

    for i in range(len(monster_id)):

        if monster_id[i] in actual_m:
            # Save the largest value on the previous appearance of monster_id
            q[actual_m.get(monster_id[i])] = max(q[i], q[actual_m.get(monster_id[i])])
            # Delete the extra items
            q.pop(i)
            monster_id.pop(i)
            object2.pop(i)
        else:
            # Save the monster with his position on the list
            actual_m[monster_id[i]] = i

    # context= {
    #     "result": final_list
    # }
    for i in range(len(q)):
        q[i] = ceil(q[i])
    result = []
    for i in range(len(monster_id)):
        result.append((Monster.objects.get(id=monster_id[i]), q[i]))


def lend_register(request):
    template = loader.get_template('Views_test/lend_register.html')

    lend_register_table = Palico_lent.objects.all()

    context = {
        'lend_register': lend_register_table
    }
    return HttpResponse(template.render(context, request))
