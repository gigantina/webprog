from django.shortcuts import render
from .models import Genre, Authors, Compositions, Perfomances
from .forms import PerfomanceForm, CompositionForm, GenreForm, AuthorForm
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


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


def composition(request, composition_id):
    composition_object = Compositions.objects.filter(id=composition_id)[0]
    perfomances_list = list(Perfomances.objects.filter(composition=composition_object))
    print(perfomances_list)
    name_table = 'Произведения'
    context = {}
    context['name_table'] = name_table
    context['objects'] = perfomances_list
    context['composition'] = composition_object
    context['titles'] = ['#', 'Исполнитель', 'Путь', 'Дата', 'Идеальное выступление']

    context['columns_names'] = [i.name for i in Perfomances._meta.get_fields() if i.name != 'name']

    return render(request, 'composition.html', context)


def perfomances(request):
    perfomances_list = list(Perfomances.objects.all())
    name_table = 'Исполнения'
    context = {}
    context['name_table'] = name_table
    context['objects'] = perfomances_list
    context['titles'] = ['#', 'Произведение', 'Исполнитель', 'Путь', 'Дата', 'Идеальное выступление']
    context['columns_names'] = [i.name for i in Perfomances._meta.get_fields()]

    return render(request, 'perfomances_table.html', context)


class PerfomanceCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': PerfomanceForm()}
        return render(request, 'create.html', context)

    def post(self, request, *args, **kwargs):
        form = PerfomanceForm(request.POST)
        if form.is_valid():
            perfomance = form.save()
            perfomance.save()
            return HttpResponseRedirect(reverse_lazy('perfomances'))
        return render(request, 'create.html', {'form': form})


class CompositionCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': CompositionForm()}
        return render(request, 'create.html', context)

    def post(self, request, *args, **kwargs):
        form = CompositionForm(request.POST)
        if form.is_valid():
            composition = form.save()
            composition.save()
            return HttpResponseRedirect(reverse_lazy('compositions'))
        return render(request, 'create.html', {'form': form})


class GenreCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': GenreForm()}
        return render(request, 'create.html', context)

    def post(self, request, *args, **kwargs):
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save()
            genre.save()
            return HttpResponseRedirect(reverse_lazy('dashboard'))
        return render(request, 'create.html', {'form': form})


class AuthorCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': AuthorForm()}
        return render(request, 'create.html', context)

    def post(self, request, *args, **kwargs):
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            author.save()
            return HttpResponseRedirect(reverse_lazy('authors'))
        return render(request, 'create.html', {'form': form})
