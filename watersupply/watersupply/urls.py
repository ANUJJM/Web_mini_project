from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

# import waterbottlesupply.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('waterbottlesupply.urls')),
    path('cart/', include('cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
