from django.shortcuts import render, redirect
from .forms import AutorForms

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