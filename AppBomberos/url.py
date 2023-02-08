


from django.urls import path

from AppBomberos.views import *

urlpatterns = [
    path("verbomberos/", ver_bomberos),
    path("agregarbombero/", agregar_bombero),

   

]
