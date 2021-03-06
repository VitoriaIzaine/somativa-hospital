"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path('paciente/', include('paciente.urls')),
    path('consulta/', include('consulta.urls')),
    path('<int:idbusca>', views.mostrar, name='cursos'),
    path('buscar/', views.buscar, name='buscar'),
    path('login/', views.login, name='login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('logout/', views.logout, name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
