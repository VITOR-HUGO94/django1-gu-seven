from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader


def index(request):
    # print(dir(request.headers))
    # print(f'Metodo: {request.headers}')
    # print(dir(request.user))
    # print(f"User: {request.user.email}")
    # print(f"User-Agent: {request.headers['User-Agent']}")
    if str(request.user) == 'AnonymousUser':
        teste = 'Usuario não logado'
    else:
        teste = 'Usuario logado'

    produtos = Produto.objects.all()

    context = {
        'dj': 'Django é massa',
        'logado': teste,
        'produtos': produtos

    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contato.html')


def produto(request, pk):
    print(f'PK: {pk}')
    prod = get_object_or_404 (Produto, id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)