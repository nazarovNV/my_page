from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass

zodiac_dict = {
    'aries': "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    'taurus': "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    'gemini': "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    'cancer': "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    'leo': "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    'virgo': "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    'libra': "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    'scorpio': "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    'sagittarius': "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    'capricorn': "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    'aquarius': "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
    'pisces': "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}
# elements_list = ["Fire", "Earth", "Air", "Water"]
# earth_zodiac_list = ["taurus", "virgo", "capricorn"]
elements_dict = {
    'fire': ["aries", "leo", "sagittarius"],
    'earth': ["taurus", "virgo", "capricorn"],
    'air': ["gemini", "libra", "aquarius"],
    'water': ["cancer", "scorpio", "pisces"],
}


def index(request):
    zodiacs = list(zodiac_dict)
    # f"<li><a href = '{redirect_url}'>{sign}</a></li>"
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'horoscope/index.html', context=context)


def get_types_of_zodiacs(request):
    types = elements_dict.keys()
    li_elements = ''
    for type in types:
        redirect_url = reverse('type-name', args=[type])
        li_elements += f"<li><a href = '{redirect_url}'>{type.title()}</a></li>"
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(li_elements)


def get_info_about_type(request, type_zodiac: str):
    zodiacs_of_type = elements_dict.get(type_zodiac, None)
    if zodiacs_of_type:
        li_elements = ''
        for sign in zodiacs_of_type:
            redirect_url = reverse('horoscope-name', args=[sign])
            li_elements += f"<li><a href = '{redirect_url}'>{sign.title()}</a></li>"
        response = f"""
            <ul>
                {li_elements}
            </ul>
            """
        return HttpResponse(li_elements)
    else:
        return HttpResponseNotFound(f"Неизвестный тип зодиака - {type_zodiac}")


@dataclass
class Person:
    name: str
    age: int

    def __str__(self):
        return f'This is {self.name}'


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {
        "description_zodiac": description,
        "sign": sign_zodiac,
        "my_int": 111,
        "my_float": 111.5,
        "my_list": ["wafawf", 1, 2],
        "my_turple": ("wafawf", 1, 2),
        "my_dict": {"name": "Jack", "age": 20},
        "my_class": Person("Will", 55)
    }
    return render(request, "horoscope/info_zodiac.html", context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Неправильный порядковый номер знака зодиака - {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)
