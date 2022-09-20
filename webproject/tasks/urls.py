from django.urls import path
from tasks.views.base import index_view

urlpatterns = [
    path('', index_view)
]