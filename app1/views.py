from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'app1/inicio.html')

def acerca_de(request):
    return render(request, 'app1/acerca_de.html')