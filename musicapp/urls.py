from django.urls import path
from . import views

urlpatterns = [
    path('get_recommendation',views.RecommendationAI.as_view(), name= "recommendation"),
]