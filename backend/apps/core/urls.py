from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.portfolio_view, name='portfolio'),
    path('project/<slug:slug>/', views.mini_project_view, name='mini_project'),
]
