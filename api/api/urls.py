from django.contrib import admin
from django.urls import path,include,re_path
from users import urls as u_url
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home');


urlpatterns = [
    
    path('admin/', admin.site.urls),
    re_path(r'^$',home),
    path('users/',include(u_url))
]

