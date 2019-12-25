from django.urls import path

from . import views

urlpatterns = [
    path('api/create/', views.create_api, name='create_api'),
    path('api/view/<str:paste_id>', views.view_api, name='view_api'),
    path('create/', views.create, name='create'),
    path('view/<str:paste_id>', views.view, name='view'),
]
