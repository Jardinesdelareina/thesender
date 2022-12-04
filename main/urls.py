from django.urls import path
from .views import RecipientView

urlpatterns = [
    path('', RecipientView.as_view(), name='subscribe'),
]
