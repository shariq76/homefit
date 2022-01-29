from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('products/<slug:cat_slug>/', views.products, name='catproducts'),
    path('products/<slug:cat_slug>/<slug:prod_slug>/', views.selected1, name='single'),
    path('search', views.search, name='search'),
    path('about', views.about, name='about'),
    path('contact_us', views.contactus, name='contact_us'),
]