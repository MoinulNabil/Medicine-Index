from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user_account.urls')),
    path('api/medicine/', include('medicine.urls')),
]
