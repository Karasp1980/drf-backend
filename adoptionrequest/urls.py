from django.urls import path
from adoptionrequest import views

urlpatterns = [
    path('adoptionrequest/', views.AdoptionrequestList.as_view()),
    path('adoptionrequest/<int:pk>/', views.AdoptionrequestDetail.as_view())
]