from django.contrib import admin

from django.urls import path, include  # Certifique-se de importar o include​


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('myapp.urls')),  # Inclui as URLs do seu app​

]