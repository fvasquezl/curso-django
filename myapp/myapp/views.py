from django.http import HttpResponse


def hola(request):

    numeros = sorted([int(x) for x in request.GET["numeros"].split(",")])

    return HttpResponse(str(numeros))


def verificar(request, nombre, edad):
    if edad < 12:
        mensaje = f"Hola, {nombre} perdon no puede entrar a esta pagina"
    else:
        mensaje = f"Hola, {nombre} puede ingresar"

    return HttpResponse(mensaje)
