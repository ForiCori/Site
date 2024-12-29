from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.MainPage.as_view(), name='main'),
    path("cart/", views.CartPage.as_view(), name='cart'),
    path("product/<slug:product_slug>/", views.ProductPage.as_view(), name='product'),
    path("login/", views.LoginUser.as_view(), name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("registration/", views.UserRegistration.as_view(), name='registration'),
    path("profile/<slug:profile_name>/", views.ProfilePage.as_view(), name='profile'),
    path("delete/<int:pk>/", views.CartDelete.as_view(), name='delete'),
    path("outro/", views.Outro.as_view(), name='outro'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
