from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns=[
    path('producto/', views.product_list),
    path('productocreate/', csrf_exempt(views.producto_create), name='productoCreate'),
    re_path(r'^producto_delete/(?P<pk>\d+)/$', csrf_exempt(views.producto_delete), name='productoDelete'),

]