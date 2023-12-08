
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),  # Указываем путь к приложению user
    path('', include('main.urls')), path('admin/', admin.site.urls),
    path('', include('user.urls'))
]
