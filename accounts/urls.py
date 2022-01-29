from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('personal', views.personal_info, name='personal'),
    path('update_info', views.update_info, name='update_info'),
    path('address', views.address_info, name='address'),
    path('address_update', views.address_update, name='address_update'),
    path('orders', views.orders, name='orders'),
    path('order_summary/<int:order_id>', views.order_summary, name='order_summary'),
    path('feedback', views.feedBack, name='feedback'),
]
