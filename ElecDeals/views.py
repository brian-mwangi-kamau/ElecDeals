import requests
from django.shortcuts import render
from rest_framework import viewsets
from .models import Gadget
from .serializers import GadgetSerializer


class GadgetViewSet(viewsets.ModelViewSet):
    queryset = Gadget.objects.all()
    serializer_class = GadgetSerializer


def homepage(request):
    response = requests.get('http://127.0.0.1:8000/api/gadgets/')
    gadgets = response.json
    return render(request, 'homepage.html', {'gadgets': gadgets})

    