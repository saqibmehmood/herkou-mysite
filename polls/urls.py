from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='name'),
    path('<int:question_id>/', views.detail, name='detail'),

]