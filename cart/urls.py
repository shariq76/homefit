from django.urls import path
from . import views
urlpatterns = [
    path('', views.CartView, name='cart'),
    path('add_cart/<slug:prod_slug>/', views.add_to_cart, name='add_cart'),
    path('update_cart/<int:id>/', views.update_cart, name='update_cart'),
    path('delete_cart/<int:id>/', views.delete_cart, name='delete_cart'),
    path('place_order', views.place_order, name='place_order')
]