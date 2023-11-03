from django.contrib import admin
from .models import Gadget, Type, Capacity, Feature

admin.site.register(Gadget)
admin.site.register(Type)
admin.site.register(Capacity)
admin.site.register(Feature)