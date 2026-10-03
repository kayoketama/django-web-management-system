from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Registration system
    path('accounts/', include('registration.backends.default.urls')),

    # Accounts pages
    path('accounts/', include('accounts.urls')),

    # Homepage and other pages
    path('', include('accounts.urls')),
]