from django.urls import path
from adoptioncomments import views

urlpatterns = [
    path('adoptioncomments/', views.AdoptioncommentList.as_view()),
    path('adoptioncomments/<int:pk>/', views.AdoptioncommentDetail.as_view())
]