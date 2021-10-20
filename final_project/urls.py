from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('rest-api/', include('rest_framework.urls')),
                  path('admin/', admin.site.urls),
                  path('weight/', include('weigth.url')),
                  path('home/', include('app.url')),
                  path('', include('authentication.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
