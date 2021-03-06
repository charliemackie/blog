"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from posts.views import home, filter_category, story_like, The_Data_Supply_Chain
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('The_Data_Supply_Chain', The_Data_Supply_Chain, name='The Data Supply Chain'),
    path(r'<story_name>/liked/(<story_id>[0-9]+)/', story_like, name='story_like'),
    path('<category>/', filter_category, name='filter') 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
