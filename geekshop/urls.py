from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from products.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('baskets/', include('baskets.urls', namespace='baskets')),
    path('admins/', include('admins.urls', namespace='admins')),
    path('', include('social_django.urls', namespace='social')),
    path('users/verify/google/oauth2/complete/', include("social_django.urls", namespace="social")),
    path('orders/', include('orders.urls', namespace='orders')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
