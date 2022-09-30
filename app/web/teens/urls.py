from django.urls import path
from . import views

urlpatterns={
    path('',views.index,name='index'),
    path("about/",views.about),
    path("contact/",views.contact),
    path("donate/",views.donate),
    path("gallery/",views.gallery),
    path("add/",views.add_volu),
    path("bedonor/",views.bedonor),
    path("done/",views.added)
}