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
    #listar todos
    #autores = Autor.objects.all()
    
    #listar solo los que tienen el estado en True
    autores = Autor.objects.filter(estado=True)
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

#Eliminacion directa
# def eliminar_autor(request,id):
#     autor= Autor.objects.get(id=id)
#     autor.delete()
#     return redirect('libro:listar_autor')

#eliminacion con metodo post
# def eliminar_autor(request,id):
#     autor= Autor.objects.get(id=id)
#     if request.method == 'POST':
#         autor.delete()
#         return redirect('libro:listar_autor')
#     return render(request,'eliminar_autor.html', {'autor': autor})

#baja logica
# def eliminar_autor(request,id):
#     autor= Autor.objects.get(id=id)
#     if request.method == 'POST':
#         autor.estado= False
#         autor.save()
#         return redirect('libro:listar_autor')
#     return render(request,'eliminar_autor.html', {'autor': autor})


#baja logica sin metodo post
def eliminar_autor(request,id):
    autor= Autor.objects.get(id=id)    
    autor.estado= False
    autor.save()
    return redirect('libro:listar_autor')
