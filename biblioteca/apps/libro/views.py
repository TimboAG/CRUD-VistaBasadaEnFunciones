from django.shortcuts import render, redirect
from .forms import AutorForms
from .models import Autor
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def crear_autor(request):
    if request.method == 'POST':
        autor_form= AutorForms(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
    else:
        autor_form= AutorForms()
    return render(request, 'crear_autor.html', {'autor_form': autor_form})

def listar_autor(request):
    autores = Autor.objects.all()
    return render(request, 'listar_autor.html', {'autores': autores})

def editar_autor(request, id):
    autor= Autor.objects.get(id=id)
    error=None
    try:
        if request.method == 'GET':
            autor_form= AutorForms(instance =autor)
        else:
            autor_form= AutorForms(request.POST, instance =autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('index')
    except ObjectDoesNotExist as ex:
       error=ex
    
    return render(request, 'crear_autor.html', {'autor_form': autor_form, 'error': error})
