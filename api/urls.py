from django.urls import path
from .views import OrderObjects,OrderDetail,ProductAPIView,FeedbacklistAPI,FeedbackAPI
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('product/', ProductAPIView.as_view()),
    path('order/', OrderObjects.as_view()),
    path('feedback/', FeedbacklistAPI.as_view()),
    path('feedback/<int:id>', FeedbackAPI.as_view()),
    path('order/<int:id>',OrderDetail.as_view()),
    path('token/',obtain_auth_token,name='api_token'),
]
