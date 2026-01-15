from django.shortcuts import render
from .models import GroupChat

# Список городов России (можно добавить больше)
CITIES = [
    'Москва', 'Санкт-Петербург', 'Казань', 'Новосибирск', 'Екатеринбург',
    'Нижний Новгород', 'Самара', 'Омск', 'Ростов-на-Дону', 'Краснодар',
    'Волгоград', 'Пермь', 'Уфа', 'Оренбург', 'Тюмень', 'Сочи'
]

# Список видов деятельности
ACTIVITIES = [
    'Бег', 'Йога', 'Турники', 'Спортзал', 'Единоборства',
    'Велосипед', 'Скалолазание', 'Плавание'
]

def cities(request):
    return render(request, 'coop/coop-cities.html', {'cities': CITIES})

def sport(request):
    city = request.GET.get('city', '')
    return render(request, 'coop/coop-sport.html', {'activities': ACTIVITIES, 'city': city})

def groups(request):
    city = request.GET.get('city', '')
    activity = request.GET.get('activity', '')
    groups = GroupChat.objects.filter(city=city, activity=activity)
    return render(request, 'coop/coop-groups.html', {'groups': groups, 'city': city, 'activity': activity})

def groupsex(request):
    group_id = request.GET.get('group_id')
    group = GroupChat.objects.filter(id=group_id).first()
    return render(request, 'coop/coop-groupsex.html', {'group': group})