from django.shortcuts import render
from django.http import HttpResponse


def aries(request):
    return HttpResponse("Знак зодиака овен")


def taurus(request):
    return HttpResponse("Знак зодиака телец")


def gemini(request):
    return HttpResponse("Знак зодиака близнецы")


def cancer(request):
    return HttpResponse("Знак зодиака рак")


def leo(request):
    return HttpResponse("Знак зодиака лев")


def virgo(request):
    return HttpResponse("Знак зодиака дева")


def libra(request):
    return HttpResponse("Знак зодиака весы")


def scorpio(request):
    return HttpResponse("Знак зодиака скорпион")


def sagittarius(request):
    return HttpResponse("Знак зодиака стрелец")


def capricorn(request):
    return HttpResponse("Знак зодиака козерог")


def aquarius(request):
    return HttpResponse("Знак зодиака водолей")


def pisces(request):
    return HttpResponse("Знак зодиака рыбы")
