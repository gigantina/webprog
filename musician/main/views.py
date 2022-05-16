from django.shortcuts import render
from .models import Genre, Authors, Compositions, Perfomances


def index(request):
    return render(request, 'inde4x.html')


def faq(request):
    return render(request, 'faq.html')


def genres(request):
    genres_list = list(Genre.objects.all().values())
    name_table = 'Жанры'
    context = {}
    context['name_table'] = name_table
    context['objects'] = genres_list
    context['titles'] = ['#', 'Название']
    context['columns_names'] = [i.name for i in Genre._meta.get_fields()]

    return render(request, 'table.html', context)


def authors(request):
    authors_list = list(Authors.objects.all().values())
    name_table = 'Авторы'
    context = {}
    context['name_table'] = name_table
    context['objects'] = authors_list
    context['titles'] = ['#', 'Имя', 'Описание']
    context['columns_names'] = [i.name for i in Authors._meta.get_fields()]

    return render(request, 'table.html', context)


def compositions(request):
    compositions_list = list(Compositions.objects.all().values())
    name_table = 'Произведения'
    context = {}
    context['name_table'] = name_table
    context['objects'] = compositions_list
    context['titles'] = ['#', 'Название', 'Описание', 'Жанр', 'Автор']
    context['columns_names'] = [i.name for i in Compositions._meta.get_fields() if i.name != 'path']

    return render(request, 'table.html', context)


def perfomances(request):
    perfomances_list = list(Perfomances.objects.all().values())
    name_table = 'Исполнения'
    context = {}
    context['name_table'] = name_table
    context['objects'] = perfomances_list
    context['titles'] = ['#', 'Исполнитель', 'Путь', 'Дата']
    context['columns_names'] = [i.name for i in Perfomances._meta.get_fields()]

    return render(request, 'table.html', context)
