from django.urls.conf import path
from .views import view_b
from .views import view_c
from .views import product_list


app_name="prova_pratica1"

urlpatterns = [
    path('product_list/', product_list, name="product_list"),
    path("view_b",view_b,name="view_b"),
    path("view_c",view_c,name="view_c")
]