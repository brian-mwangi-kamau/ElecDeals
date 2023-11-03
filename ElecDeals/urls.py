from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import GadgetViewSet
from . import views


router = routers.DefaultRouter()
router.register(r'gadgets', GadgetViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.homepage, name="homepage"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    