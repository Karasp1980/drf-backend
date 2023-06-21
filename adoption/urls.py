from django.urls import path
from adoption import views

urlpatterns = [
    path('adoption/', views.AdoptiontList.as_view()),
    path('adoption/<int:pk>/', views.AdoptionDetail.as_view())
]