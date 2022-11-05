from django.urls import path
from . import views



urlpatterns = [
    path('file_data', views.GetFileData.as_view()),
    path('update_file', views.UpdateFile.as_view()),
]