from django.shortcuts import render
from .models import Genre, Authors, Compositions, Perfomances


def index(request):
    return render(request, 'index.html')


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

    return render(request, 'genre_table.html', context)


def authors(request):
    authors_list = list(Authors.objects.all())
    print(authors_list)
    name_table = 'Авторы'
    context = {}
    context['name_table'] = name_table
    context['objects'] = authors_list
    context['titles'] = ['#', 'Имя', 'Описание']
    context['columns_names'] = [i.name for i in Authors._meta.get_fields()]

    return render(request, 'author_table.html', context)


def author(request, author_id):
    author_object = Authors.objects.filter(id=author_id)[0]
    context = {}
    compositions_list = list(Compositions.objects.filter(author=author_object))
    print(author_object)
    print(compositions_list)
    context['objects'] = compositions_list
    context['author'] = author_object
    context['titles'] = ['#', 'Название', 'Жанр']

    return render(request, 'author.html', context)


def compositions(request):
    compositions_list = list(Compositions.objects.all())
    print(compositions_list)
    name_table = 'Произведения'
    context = {}
    context['name_table'] = name_table
    context['objects'] = compositions_list
    context['titles'] = ['#', 'Название', 'Жанр', 'Автор']

    context['columns_names'] = [i.name for i in Compositions._meta.get_fields() if i.name != 'path']

    return render(request, 'composition_table.html', context)


def perfomances(request):
    perfomances_list = list(Perfomances.objects.all())
    name_table = 'Исполнения'
    context = {}
    context['name_table'] = name_table
    context['objects'] = perfomances_list
    context['titles'] = ['#', 'Произведение', 'Исполнитель', 'Путь', 'Дата', 'Идеальное выступление']
    context['columns_names'] = [i.name for i in Perfomances._meta.get_fields()]

    return render(request, 'perfomances_table.html', context)
