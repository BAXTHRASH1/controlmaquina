from django	.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
 	url(r'^inicio/$',views.index),
 	url(r'^estadomaquina/$',views.estado),
 	url(r'^buscarsocket/$',views.buscarsocket),
 	url(r'^soporte/$',views.Admin),
]
