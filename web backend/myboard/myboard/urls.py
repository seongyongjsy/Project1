from django.contrib import admin
from django.urls import path, include

from django.views import generic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', generic.TemplateView.as_view(template_name='common/home.html'), name='home'),
    path('user/', include('user.urls')),
    path('board/', include('board.urls')),
]
