from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('<str:model_name>/', views.ai_model_view, name='ai_model'),
]

