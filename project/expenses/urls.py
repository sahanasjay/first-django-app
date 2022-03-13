from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('categories/', views.categories, name='categories'),
  path('categories/<slug>/', views.category_detail, name='category_detail'),
  # example: /summary/1/
  path('summary/<int:summary_id>/', views.summary, name='summary'),
]
