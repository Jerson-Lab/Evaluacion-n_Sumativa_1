from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'app2/inicio.html')

def acerca_de(request):
    return render(request, 'app2/acerca_de.html')
