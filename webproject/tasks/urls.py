from django.urls import path
from tasks.views.base import index_view
from tasks.views.tasks import add_view, del_view, edit_view

urlpatterns = [
    path('', index_view),
    path('add/', add_view),
    path('del/', del_view),
    path('edit/', edit_view)
]