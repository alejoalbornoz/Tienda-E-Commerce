
from django.contrib import admin
from django.urls import path
from . import view
from products.views import ProductListViews
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ProductListViews.as_view(), name="index"),
    path("usuarios/login", view.login_view, name="login"),
    path("usuarios/logout", view.logout_view, name="logout"),
    path("usuarios/register", view.register, name="register"),
    path("productos/", include("products.urls")),
    path("carrito/", include("carts.urls")),
    path("orden/", include("orders.urls")),
    path("direcciones/", include("shipping_addresses.urls")),
    path("codigos/", include("promo_codes.urls")),
    path("pagos/", include("billing_profiles.urls"))



]


#esto permite poner imagenes en ADMIN
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)