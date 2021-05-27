from django.urls import path
from pfc.views import get_data, home
from rest_framework.routers import DefaultRouter
# from pfc.views import pfcViewset
from django.urls import path, include



# router = DefaultRouter()
# router.register(r'', pfcViewset)

urlpatterns = [
      path('',  home, name='home'),
      path('upload_csv/',get_data, name = "get_data" ),
      
]
# urlpatterns += router.urls