# meu_projeto/urls.py
from django.contrib import admin
from django.urls import include, path
from aplicativo_login.views import default_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', default_redirect, name='default_redirect'),
    path('', include('aplicativo_login.urls')),
    # Adicione outras URLs conforme necessário
]
