from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('senaraisistem/', views.senaraisistem, name='senaraisistem'),
    path('sistembaharu/', views.sistembaharu, name='sistembaharu'),
]