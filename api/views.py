from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Cake, Product, Material, Dessert, Insumos
import json

class Products(View):
    def get(self, request, *args, **kwargs):
        products = list(Product.objects.values())
        return JsonResponse({"products": products})

    def post(self, request, *args, **kwargs):
        jd = json.loads(request.body)
        Product.objects.create(**jd)
        return HttpResponse("exito", 200)

    def put(self, request, *args, **kwargs):
        jd = json.loads(request.body)
        Product.objects.filter(id=jd["id"]).update(**jd)
        return HttpResponse("exito", 200)

    def delete(self, request, *args, **kwargs):
        jd = json.loads(request.body)
        Product.objects.filter(id=jd["id"]).delete()
        return HttpResponse("exito", 200)

class Cakes(View):
    def get(self, request, *args, **kwargs):
        cakes = list(Cake.objects.values())
        return JsonResponse({"cakes": cakes})

    def post(self, request, *args, **kwargs):
        jd = json.loads(request.body)
        Cake.objects.create(**jd)
        return HttpResponse("exito", 200)

    def put(self, request, *args, **kwargs):
        jd = json.loads(request.body)
        Cake.objects.filter(id=jd["id"]).update(**jd)
        return HttpResponse("exito", 200)

    def delete(self, request, *args, **kwargs):
        jd = json.loads(request.body)
        Cake.objects.filter(id=jd["id"]).delete()
        return HttpResponse("exito", 200)

class Materials(View):
    def get(self, request, *args, **kwargs):
        materials = list(Material.objects.values())
        return JsonResponse({"materials": materials})

    def post(self, request, *args, **kwargs):
        jd = json.loads(request.body)
        Material.objects.create(**jd)
        return HttpResponse("exito", 200)

    def put(self, request, *args, **kwargs):
        jd = json.loads(request.body)
        Material.objects.filter(id=jd["id"]).update(**jd)
        return HttpResponse("exito", 200)

    def delete(self, request, *args, **kwargs):
        jd = json.loads(request.body)
        Material.objects.filter(id=jd["id"]).delete()
        return HttpResponse("exito", 200)

class Desserts(View):
    def get(self, request, *args, **kwargs):
        desserts = list(Dessert.objects.values())
        return JsonResponse({"desserts": desserts})

    def post(self, request, *args, **kwargs):
        jd = json.loads(request.body)
        Dessert.objects.create(**jd)
        return HttpResponse("exito", 200)

    def put(self, request, *args, **kwargs):
        jd = json.loads(request.body)
        Dessert.objects.filter(id=jd["id"]).update(**jd)
        return HttpResponse("exito", 200)

    def delete(self, request, *args, **kwargs):
        jd = json.loads(request.body)
        Dessert.objects.filter(id=jd["id"]).delete()
        return HttpResponse("exito", 200)

class InsumosView(View):
    def get(self, request, *args, **kwargs):
        insumos = list(Insumos.objects.values())
        return JsonResponse({"insumos": insumos})

    def post(self, request, *args, **kwargs):
        jd = json.loads(request.body)
        Insumos.objects.create(**jd)
        return HttpResponse("exito", 200)

    def put(self, request, *args, **kwargs):
        jd = json.loads(request.body)
        Insumos.objects.filter(id=jd["id"]).update(**jd)
        return HttpResponse("exito", 200)

    def delete(self, request, *args, **kwargs):
        jd = json.loads(request.body)
        Insumos.objects.filter(id=jd["id"]).delete()
        return HttpResponse("exito", 200)
