from django.urls import path
from messaging import views

urlpatterns = [
    path('messaging/', views.MessagingList.as_view()),
    path('messaging/<int:pk>/', views.MessagingDetail.as_view())
]