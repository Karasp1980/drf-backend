from django.urls import path
from adoptionlikes import views

urlpatterns = [
    path('adoptionlikes/', views.AdoptionlikeList.as_view()),
    path('adoptionlikes/<int:pk>/', views.AdoptionlikeDetail.as_view()),
]