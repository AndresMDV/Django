from django.http import HttpResponse
from django.shortcuts import render
from .models import Comments

def test(request):
    return HttpResponse("Funciona correctamente")

def create(request):
    #comment = Comments(name='Andres', score='5', comment='Este es un comentario de prueba.')
    #comment.save()
    comment = Comments.objects.create(name="Alex")
    return HttpResponse("Ruta para probar la creacion de modelos.")

def delete(request):
    #comment = Comments.objects.get(id=4)
    #comment.delete()
    Comments.objects.filter(id=2).delete()
    return HttpResponse("Ruta para probar la eliminacion de datos.")
