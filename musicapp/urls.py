from django.urls import path
from . import views

urlpatterns = [
    # path('get_recommendation',views.RecommendationAI.as_view(), name= "recommendation"),
     path('get_recommendation', views.ModelPrediction.as_view(), name="recommendation"), 
    #  path('ai_recommendation', views.recommendation_ai, name="recommendation"), 
]