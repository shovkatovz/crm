from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('create/', views.customer_create, name='customer_create'),
    path('update/<int:pk>/', views.customer_update, name='customer_update'),
    path('delete/<int:pk>/', views.customer_delete, name='customer_delete'),

    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/create/', views.contact_create, name='contact_create'),
    path('contacts/delete/<int:pk>/', views.contact_delete, name='contact_delete'),

    path('deals/', views.deal_list, name='deal_list'),
    path('deals/create/', views.deal_create, name='deal_create'),
    path('deals/delete/<int:pk>/', views.deal_delete, name='deal_delete'),

    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/delete/<int:pk>/', views.task_delete, name='task_delete'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]