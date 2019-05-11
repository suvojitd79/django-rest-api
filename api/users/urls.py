from django.urls import path,re_path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'^$',views.getAll)

urlpatterns = router.urls


# urlpatterns = [

#     #get all
#     # re_path(r'^$',views.getAll),

#     #post request    
#     #re_path(r'^create/$',views.sample2)  

#    re_path(r'^$',views.sample)

# ]