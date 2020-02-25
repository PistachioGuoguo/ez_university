from django.contrib import admin
from django.urls import path,include

from ez_university.views import redirect_root_view

urlpatterns = [
    path('',redirect_root_view), # /views.py
    path('admin/', admin.site.urls),
    path('',include('courseinfo.urls'))
]
