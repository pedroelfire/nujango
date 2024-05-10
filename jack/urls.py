from django.urls import path, include
from rest_framework import routers
from .views import *

router =  routers.DefaultRouter()
router.register(r'conversations', JackConversationViewSet)
router.register(r'questions', JackQuestionViewSet)


urlpatterns = [
    path("", include(router.urls)),
    ]