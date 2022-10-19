from django.urls import path

from django.views.generic import TemplateView
from . import views


app_name = 'files'
urlpatterns = [
    path('sendPage/', TemplateView.as_view(template_name='files/send.html'), name='sendPage'),
    path('sendFile/', views.send_file, name='sendFile'),
    path('list/', views.FileListView.as_view(), name='list'),
    path('upload/', views.file_upload, name='upload'),
    path('download/<int:pk>', views.file_download, name='download'),
]
